# LangChain Runnables

Learning the core LangChain Runnable components for building composable LLM workflows.

## Learned

### RunnableSequence

Runs steps sequentially.

```text
Input → Prompt → LLM → Parser
```

```python
chain = prompt | llm | parser
```

### RunnableParallel

Runs multiple chains with the same input.

```text
       ┌→ Chain A
Input ─┼→ Chain B
       └→ Chain C
```

### RunnablePassthrough

Passes the original input without modification.

```python
RunnablePassthrough()
```

Useful when the original input needs to be preserved alongside processed results.

### RunnableLambda

Converts a Python function into a Runnable.

```python
from langchain_core.runnables import RunnableLambda

chain = RunnableLambda(lambda x: x.upper())
```

Useful for adding custom Python logic inside a LangChain pipeline.

## Quick Reference

| Runnable              | Purpose              |
| --------------------- | -------------------- |
| `RunnableSequence`    | Sequential execution |
| `RunnableParallel`    | Parallel execution   |
| `RunnablePassthrough` | Preserve input       |
| `RunnableLambda`      | Custom Python logic  |

