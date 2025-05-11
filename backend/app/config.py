from typing_extensions import NotRequired, TypedDict

from app.models import (
    DEFAULT_DEEP_SEEK_GENERATION_CONFIG,
    DEFAULT_GENERATION_CONFIG,
    DEFAULT_LLAMA_GENERATION_CONFIG,
    DEFAULT_MISTRAL_GENERATION_CONFIG,
)


class GenerationParams(TypedDict):
    max_tokens: int
    top_k: NotRequired[int]
    top_p: float
    temperature: float
    stop_sequences: list[str]
    reasoning_params: NotRequired[dict[str, int]]


class EmbeddingConfig(TypedDict):
    model_id: str
    chunk_size: int
    chunk_overlap: int
    enable_partition_pdf: bool
