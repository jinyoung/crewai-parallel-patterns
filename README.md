<a href="https://idx.google.com/import?url=https%3A%2F%2Fgithub.com%2Fapappascs%2Fcrewai-parallel-patterns">
  <picture>
    <source
      media="(prefers-color-scheme: dark)"
      srcset="https://cdn.idx.dev/btn/open_dark_32.svg">
    <source
      media="(prefers-color-scheme: light)"
      srcset="https://cdn.idx.dev/btn/open_light_32.svg">
    <img
      height="32"
      alt="Open in IDX"
      src="https://cdn.idx.dev/btn/open_purple_32.svg">
  </picture>
</a>

# Mastering Concurrency and Branching in CrewAI: A Deep Dive into Parallel Workflows

This repository showcases advanced techniques for leveraging concurrency and branching within the CrewAI framework. It provides practical examples and patterns for designing sophisticated, parallel workflows that can significantly enhance the efficiency and capabilities of your AI crews.

## Key Features and Concepts

This project demonstrates the following powerful CrewAI features:

-   **Parallel Task Execution within a Crew:** Execute multiple tasks concurrently within a single crew using `async_execution` and task `context`.
-   **Parallel Execution of Multiple Crews:** Run multiple crews simultaneously using `asyncio.gather()`, enabling complex, multi-faceted workflows.
-   **Parallel Execution within Flows using `@start()`:** Initiate tasks from different crews in parallel at the start of a flow, maximizing efficiency.
-   **Branching in Flows using `@listen`:** Dynamically trigger tasks based on the completion of other tasks, creating flexible and responsive workflows.
-   **Combining Results from Parallel Tasks:** Aggregate outputs from concurrently executed tasks for comprehensive analysis and decision-making.

## Project Structure

The repository is organized into the following key directories:

-   `src/parallel_workflows/crews/`: Contains definitions for different crews, each with its own set of agents and tasks.
    -   `research_crew/`:  A crew focused on industry trend analysis and competitor research.
    -   `content_crew/`: A crew responsible for market research, feedback analysis, idea generation, and content creation.
-   `src/parallel_workflows/flows/`:  Demonstrates different flow patterns for parallel execution and branching.
    -   `parallel_start_flow.py`:  Illustrates parallel task execution using the `@start()` decorator.
    -   `parallel_listen_flow.py`: Showcases branching logic using the `@listen` decorator.
-   `src/parallel_workflows/main.py`:  The main entry point for running the examples and orchestrating the parallel workflows.

## Getting Started

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

**Install uv:**

```bash
pip install uv
```

**Install CrewAI:**

```bash
pip install crewai crewai-tools
```

**Clone the Repository:**

```bash
git clone https://github.com/apappascs/crewai-parallel-patterns.git
```

**Install Dependencies:**

```bash
crewai install
```

**Set your API Key:**
Add your `API_KEY` (you can use OpenAI, Gemini or any other supported by CrewAI) into the `.env` file in the root of the project:
```
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

## Running the Examples

This project showcases different ways of running crews and flows in parallel, you can run them all at once using:

```bash
crewai run
```

This will execute all the examples in `main.py` demonstrating different aspects of parallel execution and branching in CrewAI.

## Examples and Use Cases

The `main.py` file provides a comprehensive set of examples demonstrating various parallel execution and branching scenarios:

### 1. Parallel Tasks within a Crew

This example showcases how to execute multiple tasks concurrently within the `ContentCrew` using `async_execution=True` and providing `context` to later tasks. It demonstrates how to research a market, analyze feedback, and generate ideas in parallel, then combine the results to write a content piece.

### 2. Parallel Execution of Multiple Crews

This section demonstrates running the `ContentCrew` and `ResearchCrew` simultaneously using `asyncio.gather()`. This approach is useful for scenarios where independent research and content creation processes can run in parallel, significantly reducing overall execution time.

### 3. Parallel Execution within Flows using `@start()`

The `ParallelStartFlow` example illustrates how to use the `@start()` decorator to initiate tasks from different crews in parallel at the beginning of a flow. This allows for concurrent execution of independent tasks, improving efficiency.

### 4. Branching in Flows using `@listen`

The `ParallelListenFlow` example demonstrates the use of `@listen` to trigger tasks based on the completion of other tasks. This enables the creation of dynamic, branching workflows where tasks can be executed conditionally and in parallel based on the flow's state.

### 5. Parallel Execution of Multiple Flows

This example shows how to run multiple flows concurrently using `asyncio.gather()`, allowing for complex, multi-stage workflows to be executed in parallel.
