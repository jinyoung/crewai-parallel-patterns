import asyncio

from crewai.crew import Crew
from crewai.flow.flow import Flow, and_, listen, router, start
from pydantic import BaseModel

from ..crews.content_crew import ContentCrew
from ..crews.research_crew import ResearchCrew


# Define a state class to hold data that can be shared/accessed between tasks in the flow
class ParallelFlowState(BaseModel):
    content_crew_research_output: str = ""
    content_crew_ideas_output: str = ""
    research_crew_trends_output: str = ""
    research_crew_competitors_output: str = ""


class ParallelStartFlow(Flow[ParallelFlowState]):
    """
    Flow demonstrating parallel execution of tasks from different crews using @start.
    """

    def __init__(self):
        super().__init__(
            description="This flow executes tasks from Content and Research Crews in parallel.",
            state_type=ParallelFlowState
        )

    @start()
    async def research_market_and_trends(self):
        """Starts the market research task of the Content Crew."""
        print("Starting market research task from Content Crew")
        research_result = await Crew(
            agents=[ContentCrew().market_researcher()],
            tasks=[ContentCrew().research_market()]
        ).kickoff_async(
            inputs={"content_topic": "AI in Content Creation", "current_year": "2025"}
        )
        self.state.content_crew_research_output = research_result if research_result else ""

    @start()
    async def brainstorm_ideas_and_analyze_competitors(self):
        """Starts the trends analysis task of the ResearchCrew Crew."""
        print("Starting trends analysis task from Research Crew")
        research_result = await Crew(
            agents=[ResearchCrew().trend_analyst()],
            tasks=[ResearchCrew().analyze_trends()]
        ).kickoff_async(
            inputs={"industry_topic": "Artificial Intelligence", "current_year": "2025"}
        )
        self.state.content_crew_ideas_output = research_result if research_result else ""

    @listen(and_("research_market_and_trends", "brainstorm_ideas_and_analyze_competitors"))
    async def combine_results(self):
        results = f"Market Research: {self.state.content_crew_research_output}\n" \
                  f"Idea Brainstorming: {self.state.content_crew_ideas_output}"
        print("\nCombined Results:\n", results)
        return results


def plot():
    parallel_start_flow = ParallelStartFlow()
    parallel_start_flow.plot()
