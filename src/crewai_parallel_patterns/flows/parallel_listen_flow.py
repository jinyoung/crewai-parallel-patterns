import asyncio

from crewai.crew import Crew
from crewai.flow.flow import Flow, and_, listen, router, start
from pydantic import BaseModel

from ..crews.content_crew import ContentCrew
from ..crews.research_crew import ResearchCrew


# Define a state class to hold data that can be shared/accessed between tasks in the flow
class ParallelFlowState(BaseModel):
    market_research_result: str = ""
    competitor_analysis_result: str = ""
    content_feedback_result: str = ""
    combined_output: str = ""


class ParallelListenFlow(Flow[ParallelFlowState]):
    """
    Flow demonstrating the use of multiple @listen decorators to trigger parallel tasks.
    """

    def __init__(self):
        super().__init__(
            description="This flow triggers tasks in parallel from Research and Content Crews after an initial task is completed.",
            state_type=ParallelFlowState
        )

    @start()
    def initial_task(self):
        """
        Simulates an initial task that triggers subsequent tasks.
        """
        print("Initial task completed.")
        return "Initial task completed"

    @listen("initial_task")
    async def analyze_market(self):
        """
        Starts the market research task from the Content Crew, triggered by the initial task.
        """
        print("Starting market research task.")
        market_research_result = await Crew(
            agents=[ContentCrew().market_researcher()],
            tasks=[ContentCrew().research_market()]
        ).kickoff_async(inputs={
            "content_topic": "AI in Marketing",
            "current_year": "2025"
        })
        self.state.market_research_result = market_research_result.raw if market_research_result else ""
        print("Market research task completed.")
        return self.state.market_research_result

    @listen("initial_task")
    async def analyze_competitors(self):
        """
        Starts the competitor analysis task from the Research Crew, triggered by the initial task.
        """
        print("Starting competitor analysis task.")
        competitor_analysis_result = await Crew(
            agents=[ResearchCrew().competitor_analyst()],
            tasks=[ResearchCrew().analyze_competitors()]
        ).kickoff_async(inputs={
            "industry_topic": "Artificial Intelligence",
            "current_year": "2025"
        })
        self.state.competitor_analysis_result = competitor_analysis_result.raw if competitor_analysis_result else ""
        print("Competitor analysis task completed.")
        return self.state.competitor_analysis_result

    @listen("initial_task")
    async def analyze_feedback(self):
        """
        Starts the feedback analysis task from the Content Crew, triggered by the initial task.
        """
        print("Starting feedback analysis task.")
        content_feedback_result = await Crew(
            agents=[ContentCrew().feedback_analyst()],
            tasks=[ContentCrew().analyze_feedback()]
        ).kickoff_async(inputs={
            "content_topic": "AI in Marketing",
            "current_year": "2025"
        })
        self.state.content_feedback_result = content_feedback_result.raw if content_feedback_result else ""
        print("Feedback analysis task completed.")
        return self.state.content_feedback_result

    @listen(and_("analyze_market", "analyze_competitors", "analyze_feedback"))
    def combine_results(self):
        """
        Combines the results from the market research, competitor analysis, and feedback analysis tasks.
        """
        print("Combining results from all tasks.")
        self.state.combined_output = (
            f"Market Research Result:\n{self.state.market_research_result}\n\n"
            f"Competitor Analysis Result:\n{self.state.competitor_analysis_result}\n\n"
            f"Content Feedback Analysis Result:\n{self.state.content_feedback_result}"
        )
        print("\nCombined Results:\n", self.state.combined_output)
        return self.state.combined_output


def plot():
    parallel_listen_flow = ParallelListenFlow()
    parallel_listen_flow.plot()
