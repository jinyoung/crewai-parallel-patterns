from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ResearchCrew:
    """Crew for researching industry trends and analyzing competitor strategies."""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def trend_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_analyst'],
            verbose=True
        )

    @agent
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['competitor_analyst'],
            verbose=True
        )

    @task
    def analyze_trends(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_trends']
        )

    @task
    def analyze_competitors(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_competitors']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.trend_analyst(), self.competitor_analyst()],
            tasks=[self.analyze_trends(), self.analyze_competitors()],
            process=Process.sequential,
            verbose=True
        )