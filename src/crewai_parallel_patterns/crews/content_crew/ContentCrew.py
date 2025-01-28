from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ContentCrew:
    """Crew for creating content based on market research, feedback analysis, and brainstorming."""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def market_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['market_researcher'],
            verbose=True
        )

    @agent
    def feedback_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['feedback_analyst'],
            verbose=True
        )

    @agent
    def idea_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['idea_generator'],
            verbose=True
        )

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer'],
            verbose=True
        )

    @task
    def research_market(self) -> Task:
        return Task(
            config=self.tasks_config['research_market'],
            async_execution=True
        )

    @task
    def analyze_feedback(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_feedback'],
            async_execution=True
        )

    @task
    def generate_ideas(self) -> Task:
        return Task(
            config=self.tasks_config['generate_ideas'],
            async_execution=True
        )

    @task
    def write_content(self) -> Task:
        return Task(
            config=self.tasks_config['write_content'],
            context=[self.research_market(), self.analyze_feedback(), self.generate_ideas()]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.market_researcher(), self.feedback_analyst(), self.idea_generator(), self.content_writer()],
            tasks=[self.research_market(), self.analyze_feedback(), self.generate_ideas(), self.write_content()],
            process=Process.sequential,
            verbose=True
        )