"""
Groq LLM Service wrapper.

Factory that constructs a GroqLLMService and an OpenAI-style context
aggregator pair for conversation memory.
"""

from loguru import logger

from pipecat.services.groq.llm import GroqLLMService

# Pipecat compatibility:
# - 0.0.x expects OpenAILLMContext (has set_llm_adapter)
# - 1.x uses LLMContext
try:
    from pipecat.processors.aggregators.openai_llm_context import OpenAILLMContext as _Context
except ImportError:
    from pipecat.processors.aggregators.llm_context import LLMContext as _Context

from src.config import AgentConfig


def build_groq_llm(config: AgentConfig):
    """Construct a GroqLLMService plus a context aggregator pair."""
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

    messages = [{"role": "system", "content": config.system_prompt}]
    context = _Context(messages=messages)
    context_aggregator = llm.create_context_aggregator(context)

    logger.info(
        "Groq LLM service ready",
        model=config.groq_model,
        system_prompt_chars=len(config.system_prompt),
    )
    return llm, context_aggregator
