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


# 한국어 설명

1. **전체 아키텍처**
- 이 시스템은 CrewAI를 기반으로 한 병렬 처리 패턴을 구현한 프레임워크입니다.
- 크게 두 가지 주요 컴포넌트로 구성됩니다:
  - Crews: 특정 도메인의 작업을 수행하는 에이전트 그룹
  - Flows: 작업의 흐름을 관리하는 패턴

2. **주요 Crew 구성**
- **ContentCrew**: 콘텐츠 생성에 특화된 crew
  - 입력: content_topic, current_year, target_audience, content_type, word_count
  - 목적: 특정 주제에 대한 콘텐츠 생성

- **ResearchCrew**: 리서치에 특화된 crew
  - 입력: industry_topic, current_year
  - 목적: 특정 산업/주제에 대한 리서치 수행

3. **병렬 처리 패턴**
시스템은 5가지 주요 병렬 처리 패턴을 구현하고 있습니다:

a) **Content Crew 내부 병렬 처리**
```python
async def run_parallel_tasks_in_content_crew():
    content_crew = ContentCrew().crew()
    result = await content_crew.kickoff_async(inputs=inputs)
```
- ContentCrew 내부의 여러 작업들이 비동기적으로 실행됩니다.

b) **여러 Crew의 병렬 실행**
```python
async def run_parallel_execution_of_multiple_crews():
    results = await asyncio.gather(
        content_crew.kickoff_async(inputs=content_crew_inputs),
        research_crew.kickoff_async(inputs=research_crew_inputs),
    )
```
- ContentCrew와 ResearchCrew가 동시에 실행되어 결과를 병렬로 수집합니다.

c) **Flow 내부의 병렬 실행**
```python
def run_parallel_execution_with_start_flow():
    flow = ParallelStartFlow()
    final_output = flow.kickoff()
```
- @start() 데코레이터를 사용하여 Flow 내부의 작업들을 병렬로 실행합니다.

d) **Flow의 분기 처리**
```python
def run_branching_with_listen_flow():
    flow = ParallelListenFlow()
    final_output = flow.kickoff()
```
- @listen 데코레이터를 사용하여 Flow 내에서 조건에 따른 분기 처리를 수행합니다.

e) **여러 Flow의 병렬 실행**
```python
async def run_parallel_execution_of_multiple_flows():
    results = await asyncio.gather(
        start_flow.kickoff_async(),
        listen_flow.kickoff_async(),
    )
```
- 여러 Flow를 동시에 실행하여 결과를 병렬로 수집합니다.

4. **작동 프로세스**
1. 사용자가 특정 주제나 산업에 대한 레포트 생성을 요청
2. 시스템은 자동으로:
   - ContentCrew를 통해 관련 콘텐츠 생성
   - ResearchCrew를 통해 관련 리서치 수행
   - 각 Crew 내부의 작업들은 병렬로 처리
   - 여러 Flow를 통해 작업의 흐름을 관리하고 분기 처리
3. 모든 결과가 수집되면 최종 레포트로 통합

5. **장점**
- **효율성**: 병렬 처리를 통해 작업 시간 단축
- **확장성**: 새로운 Crew나 Flow를 쉽게 추가 가능
- **유연성**: 다양한 패턴의 병렬 처리 지원
- **모듈성**: 각 Crew와 Flow가 독립적으로 작동

이 시스템은 CrewAI의 강력한 기능을 활용하여 복잡한 레포트 생성 작업을 효율적으로 수행할 수 있도록 설계되었습니다. 각각의 Crew와 Flow는 독립적으로 작동하면서도 전체적으로는 조화롭게 협력하여 최종 결과물을 만들어냅니다.
