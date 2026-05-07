"""
Groq LLM Service wrapper.

Factory layer that constructs a ``GroqLLMService`` and injects
the agent's system prompt as the first message in every conversation.

Design decisions:
- Context aggregators (OpenAI-style) are created here and returned alongside
  the LLM service so the pipeline can wire them correctly around the LLM.
- Temperature and max_tokens are passed through OpenAI-compat kwargs.
- A custom ``LLMUserResponseAggregator`` captures user speech and a
  ``LLMAssistantResponseAggregator`` captures bot responses for memory.
"""

from loguru import logger

from pipecat.services.groq import GroqLLMService
from pipecat.processors.aggregators.openai_llm_context import (
    OpenAILLMContext,
    OpenAILLMContextAggregator,
)

from src.config import AgentConfig


def build_groq_llm(
    config: AgentConfig,
) -> tuple[GroqLLMService, OpenAILLMContextAggregator, OpenAILLMContextAggregator]:
    """Construct a GroqLLMService plus paired context aggregators.

    The context aggregators maintain conversation history (user + assistant
    turns) so the LLM always has the full conversation in its context window.

    Args:
        config: Validated agent configuration object.

    Returns:
        Tuple of:
          - ``llm``: configured GroqLLMService
          - ``user_aggregator``: aggregates user speech turns
          - ``assistant_aggregator``: aggregates assistant response turns
    """
    logger.debug(
        "Building Groq LLM service",
        model=config.groq_model,
        temperature=config.llm_temperature,
        max_tokens=config.llm_max_tokens,
    )

    llm = GroqLLMService(
        api_key=config.groq_api_key,
        settings=GroqLLMService.Settings(
            model=config.groq_model,
            temperature=config.llm_temperature,
            max_tokens=config.llm_max_tokens,
        ),
    )

    # Initialise conversation context with the system prompt.
    # OpenAILLMContext is the standard Pipecat context object; it tracks
    # all messages and is automatically passed between aggregators and LLM.
    messages = [
        {
            "role": "system",
            "content": config.system_prompt,
        }
    ]
    context = OpenAILLMContext(messages=messages)

    # Create paired aggregators. These act as Frame Processors in the pipeline:
    #   user_aggregator   → collects TranscriptionFrames → emits LLMMessagesFrame
    #   assistant_aggregator → collects LLM text tokens → stores them in context
    user_aggregator, assistant_aggregator = llm.create_context_aggregator(context)

    logger.info(
        "Groq LLM service ready",
        model=config.groq_model,
        system_prompt_chars=len(config.system_prompt),
    )
    return llm, user_aggregator, assistant_aggregator
