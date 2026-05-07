"""
Groq LLM Service wrapper — Pipecat 0.0.108 compatible.

Factory that constructs a GroqLLMService and an OpenAI-style context
aggregator pair for conversation memory.

In Pipecat >=0.0.105, create_context_aggregator() returns a single
aggregator pair object with .user() and .assistant() methods.
"""

from loguru import logger

from pipecat.services.groq.llm import GroqLLMService
from pipecat.processors.aggregators.llm_context import LLMContext

from src.config import AgentConfig


def build_groq_llm(config: AgentConfig):
    """Construct a GroqLLMService plus a context aggregator pair.

    Returns:
        Tuple of (llm, context_aggregator) where context_aggregator
        exposes .user() and .assistant() pipeline processors.
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

    # Seed the conversation with the system prompt.
    messages = [{"role": "system", "content": config.system_prompt}]
    context = LLMContext(messages=messages)

    # create_context_aggregator returns a pair object (not a tuple).
    # Use  ctx.user()      in the pipeline before the LLM.
    # Use  ctx.assistant() in the pipeline after the LLM.
    context_aggregator = llm.create_context_aggregator(context)

    logger.info(
        "Groq LLM service ready",
        model=config.groq_model,
        system_prompt_chars=len(config.system_prompt),
    )
    return llm, context_aggregator
