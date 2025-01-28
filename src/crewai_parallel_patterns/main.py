#!/usr/bin/env python
import asyncio
import warnings
from datetime import datetime

from crewai_parallel_patterns.crews.content_crew import ContentCrew
from crewai_parallel_patterns.crews.research_crew import ResearchCrew
from crewai_parallel_patterns.flows.parallel_start_flow import ParallelStartFlow
from crewai_parallel_patterns.flows.parallel_listen_flow import ParallelListenFlow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


async def run_parallel_tasks_in_content_crew():
    """
    Demonstrates parallel execution of tasks within the Content Crew using async_execution and context.
    """
    print("-" * 50)
    print("Step 1: Parallel Execution of Tasks in Content Crew")

    content_crew = ContentCrew().crew()

    # Define the inputs for the crew
    inputs = {
        "content_topic": "AI in Content Creation",
        "current_year": "2025",
        "target_audience": "Marketing professionals",
        "content_type": "blog post",
        "word_count": "500",
    }

    # Kick off the crew asynchronously
    result = await content_crew.kickoff_async(inputs=inputs)
    print("\nFinal Output from Content Crew:\n", result.raw)
    print("-" * 50, "\n")


async def run_parallel_execution_of_multiple_crews():
    """
    Demonstrates parallel execution of multiple crews using asyncio.gather().
    """
    print("-" * 50)
    print("Step 2: Parallel Execution of Multiple Crews using asyncio.gather()")

    # Define inputs for each crew
    content_crew_inputs = {
        "content_topic": "AI in Content Creation",
        "current_year": "2025",
        "target_audience": "Marketing professionals",
        "content_type": "blog post",
        "word_count": "500",
    }
    research_crew_inputs = {
        "industry_topic": "Artificial Intelligence",
        "current_year": "2025",
    }

    # Instantiate crews
    content_crew = ContentCrew().crew()
    research_crew = ResearchCrew().crew()

    # Execute crews in parallel
    results = await asyncio.gather(
        content_crew.kickoff_async(inputs=content_crew_inputs),
        research_crew.kickoff_async(inputs=research_crew_inputs),
    )

    print("\nContent Crew Result:\n", results[0].raw)
    print("\nResearch Crew Result:\n", results[1].raw)
    print("-" * 50, "\n")


def run_parallel_execution_with_start_flow():
    """
    Demonstrates parallel execution of tasks in a flow using @start() methods.
    """
    print("-" * 50)
    print("Step 3: Parallel Execution within Flows using @start()")
    flow = ParallelStartFlow()
    final_output = flow.kickoff()
    print("---- Final Output ----")
    print(final_output)
    print("-" * 50, "\n")


def run_branching_with_listen_flow():
    """
    Demonstrates branching in a flow using @listen decorators.
    """
    print("-" * 50)
    print("Step 4: Branching in a Flow using @listen")
    flow = ParallelListenFlow()
    final_output = flow.kickoff()
    print("---- Final Output ----")
    print(final_output)
    print("-" * 50, "\n")


async def run_parallel_execution_of_multiple_flows():
    """
    Demonstrates parallel execution of multiple flows using asyncio.gather().
    """
    print("-" * 50)
    print("Step 5: Parallel Execution of Multiple Flows using asyncio.gather()")

    # Instantiate flows
    start_flow = ParallelStartFlow()
    listen_flow = ParallelListenFlow()

    # Execute flows in parallel
    results = await asyncio.gather(
        start_flow.kickoff_async(),
        listen_flow.kickoff_async(),
    )

    print("\nParallelStartFlow Result:\n", results[0])
    print("\nParallelListenFlow Result:\n", results[1])
    print("-" * 50, "\n")


def run():
    """
    Orchestrates and demonstrates various parallel execution and branching approaches in CrewAI.
    """
    current_year = str(datetime.now().year)
    print("\n=== Mastering Concurrency and Branching in CrewAI ===\n")
    print(f"Current Year: {current_year}")

    # Step 1: Run parallel tasks in Content Crew
    asyncio.run(run_parallel_tasks_in_content_crew())

    # Step 2: Run multiple crews in parallel
    asyncio.run(run_parallel_execution_of_multiple_crews())

    # Step 3: Run parallel execution in a flow with @start
    run_parallel_execution_with_start_flow()

    # Step 4: Run branching logic with @listen
    run_branching_with_listen_flow()

    # Step 5: Run multiple flows in parallel
    asyncio.run(run_parallel_execution_of_multiple_flows())


if __name__ == "__main__":
    run()
