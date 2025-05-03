"""
Model settings for the application.
This module contains configuration settings for all supported models.
"""

from typing import Dict, List, Literal, Optional, TypedDict, Union

from typing_extensions import NotRequired


class GenerationParams(TypedDict):
    """Generation parameters for models."""
    max_tokens: int
    top_k: NotRequired[int]
    top_p: float
    temperature: float
    stop_sequences: list[str]
    reasoning_params: NotRequired[dict[str, int]]


class ModelConfig(TypedDict):
    """Configuration for a model."""
    name: str                      # e.g., "claude-v3-haiku"
    model_id: str                  # e.g., "anthropic.claude-3-haiku-20240307-v1:0"
    model_type: str                # e.g., "claude", "nova", "deepseek", "llama", "mistral"
    generation_config: GenerationParams  # Default generation parameters for this model
    pricing: Dict[str, Dict[str, float]]  # Dict of region -> {input: float, output: float}
    supported_regions: List[str]   # List of regions where this model is available
    supports_tool_use: bool        # Whether the model supports tool use
    max_context_length: NotRequired[int]  # Maximum context length in tokens


# Default generation configurations
DEFAULT_GENERATION_CONFIG: GenerationParams = {
    "max_tokens": 4096,
    "top_k": 250,
    "top_p": 0.999,
    "temperature": 1.0,
    "stop_sequences": ["Human: ", "Assistant: "],
    "reasoning_params": {"budget_tokens": 1024},
}

DEFAULT_MISTRAL_GENERATION_CONFIG: GenerationParams = {
    "max_tokens": 4096,
    "top_k": 250,
    "top_p": 0.9,
    "temperature": 0.5,
    "stop_sequences": ["[INST]", "[/INST]"],
}

DEFAULT_DEEP_SEEK_GENERATION_CONFIG: GenerationParams = {
    "max_tokens": 4096,
    "top_p": 0.9,
    "temperature": 1.0,
    "stop_sequences": [],
}

DEFAULT_LLAMA_GENERATION_CONFIG: GenerationParams = {
    "max_tokens": 2048,
    "top_p": 0.9,
    "temperature": 0.7,
    "stop_sequences": [],
}

# List of all supported models with their configurations
MODELS: List[ModelConfig] = [
    # Claude models
    {
        "name": "claude-v3-haiku",
        "model_id": "anthropic.claude-3-haiku-20240307-v1:0",
        "model_type": "claude",
        "generation_config": DEFAULT_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00025, "output": 0.00125},
            "default": {"input": 0.00025, "output": 0.00125},
        },
        "supported_regions": ["us-east-1", "us-east-2", "us-west-2"],
        "supports_tool_use": True,
    },
    {
        "name": "claude-v3-opus",
        "model_id": "anthropic.claude-3-opus-20240229-v1:0",
        "model_type": "claude",
        "generation_config": DEFAULT_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.01500, "output": 0.07500},
            "us-west-2": {"input": 0.01500, "output": 0.07500},
            "default": {"input": 0.01500, "output": 0.07500},
        },
        "supported_regions": ["us-east-1", "us-west-2"],
        "supports_tool_use": True,
    },
    {
        "name": "claude-v3.5-sonnet",
        "model_id": "anthropic.claude-3-5-sonnet-20240620-v1:0",
        "model_type": "claude",
        "generation_config": DEFAULT_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00300, "output": 0.01500},
            "us-east-2": {"input": 0.00300, "output": 0.01500},
            "us-west-2": {"input": 0.00300, "output": 0.01500},
            "eu-central-1": {"input": 0.00300, "output": 0.01500},
            "eu-west-1": {"input": 0.00300, "output": 0.01500},
            "eu-west-3": {"input": 0.00300, "output": 0.01500},
            "ap-south-1": {"input": 0.00300, "output": 0.01500},
            "ap-northeast-1": {"input": 0.00300, "output": 0.01500},
            "ap-northeast-2": {"input": 0.00300, "output": 0.01500},
            "ap-southeast-1": {"input": 0.00300, "output": 0.01500},
            "ap-southeast-2": {"input": 0.00300, "output": 0.01500},
            "default": {"input": 0.00300, "output": 0.01500},
        },
        "supported_regions": [
            "us-east-1", "us-east-2", "us-west-2", 
            "eu-central-1", "eu-west-1", "eu-west-3",
            "ap-south-1", "ap-northeast-1", "ap-northeast-2", 
            "ap-southeast-1", "ap-southeast-2"
        ],
        "supports_tool_use": True,
    },
    {
        "name": "claude-v3.5-sonnet-v2",
        "model_id": "anthropic.claude-3-5-sonnet-20241022-v2:0",
        "model_type": "claude",
        "generation_config": DEFAULT_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00300, "output": 0.01500},
            "us-east-2": {"input": 0.00300, "output": 0.01500},
            "us-west-2": {"input": 0.00300, "output": 0.01500},
            "ap-south-1": {"input": 0.00300, "output": 0.01500},
            "ap-northeast-1": {"input": 0.00300, "output": 0.01500},
            "ap-northeast-2": {"input": 0.00300, "output": 0.01500},
            "ap-northeast-3": {"input": 0.00300, "output": 0.01500},
            "ap-southeast-1": {"input": 0.00300, "output": 0.01500},
            "ap-southeast-2": {"input": 0.00300, "output": 0.01500},
            "default": {"input": 0.00300, "output": 0.01500},
        },
        "supported_regions": [
            "us-east-1", "us-east-2", "us-west-2",
            "ap-south-1", "ap-northeast-1", "ap-northeast-2", 
            "ap-northeast-3", "ap-southeast-1", "ap-southeast-2"
        ],
        "supports_tool_use": True,
    },
    {
        "name": "claude-v3.5-haiku",
        "model_id": "anthropic.claude-3-5-haiku-20241022-v1:0",
        "model_type": "claude",
        "generation_config": DEFAULT_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.001, "output": 0.005},
            "us-east-2": {"input": 0.001, "output": 0.005},
            "us-west-2": {"input": 0.001, "output": 0.005},
            "eu-central-1": {"input": 0.001, "output": 0.005},
            "eu-west-1": {"input": 0.001, "output": 0.005},
            "eu-west-3": {"input": 0.001, "output": 0.005},
            "default": {"input": 0.001, "output": 0.005},
        },
        "supported_regions": [
            "us-east-1", "us-east-2", "us-west-2",
            "eu-central-1", "eu-west-1", "eu-west-3"
        ],
        "supports_tool_use": True,
    },
    {
        "name": "claude-v3.7-sonnet",
        "model_id": "anthropic.claude-3-7-sonnet-20250219-v1:0",
        "model_type": "claude",
        "generation_config": DEFAULT_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00300, "output": 0.01500},
            "us-east-2": {"input": 0.00300, "output": 0.01500},
            "us-west-2": {"input": 0.00300, "output": 0.01500},
            "eu-central-1": {"input": 0.00300, "output": 0.01500},
            "eu-west-1": {"input": 0.00300, "output": 0.01500},
            "eu-west-3": {"input": 0.00300, "output": 0.01500},
            "default": {"input": 0.00300, "output": 0.01500},
        },
        "supported_regions": [
            "us-east-1", "us-east-2", "us-west-2",
            "eu-central-1", "eu-west-1", "eu-west-3"
        ],
        "supports_tool_use": True,
    },
    
    # Mistral models
    {
        "name": "mistral-7b-instruct",
        "model_id": "mistral.mistral-7b-instruct-v0:2",
        "model_type": "mistral",
        "generation_config": DEFAULT_MISTRAL_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00015, "output": 0.0002},
            "us-west-2": {"input": 0.00015, "output": 0.0002},
            "default": {"input": 0.00015, "output": 0.0002},
        },
        "supported_regions": ["us-east-1", "us-west-2"],
        "supports_tool_use": True,
    },
    {
        "name": "mixtral-8x7b-instruct",
        "model_id": "mistral.mixtral-8x7b-instruct-v0:1",
        "model_type": "mistral",
        "generation_config": DEFAULT_MISTRAL_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00045, "output": 0.0007},
            "us-west-2": {"input": 0.00045, "output": 0.0007},
            "default": {"input": 0.00045, "output": 0.0007},
        },
        "supported_regions": ["us-east-1", "us-west-2"],
        "supports_tool_use": True,
    },
    {
        "name": "mistral-large",
        "model_id": "mistral.mistral-large-2402-v1:0",
        "model_type": "mistral",
        "generation_config": DEFAULT_MISTRAL_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.004, "output": 0.012},
            "us-west-2": {"input": 0.004, "output": 0.012},
            "default": {"input": 0.004, "output": 0.012},
        },
        "supported_regions": ["us-east-1", "us-west-2"],
        "supports_tool_use": True,
    },
    {
        "name": "mistral-large-2",
        "model_id": "mistral.mistral-large-2407-v1:0",
        "model_type": "mistral",
        "generation_config": DEFAULT_MISTRAL_GENERATION_CONFIG,
        "pricing": {
            "us-west-2": {"input": 0.002, "output": 0.06},
            "default": {"input": 0.002, "output": 0.06},
        },
        "supported_regions": ["us-west-2"],
        "supports_tool_use": True,
    },
    
    # Amazon Nova models
    {
        "name": "amazon-nova-pro",
        "model_id": "amazon.nova-pro-v1:0",
        "model_type": "nova",
        "generation_config": DEFAULT_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.0008, "output": 0.0032},
            "us-east-2": {"input": 0.0008, "output": 0.0032},
            "us-west-2": {"input": 0.0008, "output": 0.0032},
            "eu-central-1": {"input": 0.0008, "output": 0.0032},
            "eu-west-1": {"input": 0.0008, "output": 0.0032},
            "eu-west-3": {"input": 0.0008, "output": 0.0032},
            "eu-north-1": {"input": 0.0008, "output": 0.0032},
            "ap-south-1": {"input": 0.0008, "output": 0.0032},
            "ap-northeast-1": {"input": 0.0008, "output": 0.0032},
            "ap-northeast-2": {"input": 0.0008, "output": 0.0032},
            "ap-southeast-1": {"input": 0.0008, "output": 0.0032},
            "ap-southeast-2": {"input": 0.0008, "output": 0.0032},
            "default": {"input": 0.0008, "output": 0.0032},
        },
        "supported_regions": [
            "us-east-1", "us-east-2", "us-west-2",
            "eu-central-1", "eu-west-1", "eu-west-3", "eu-north-1",
            "ap-south-1", "ap-northeast-1", "ap-northeast-2",
            "ap-southeast-1", "ap-southeast-2"
        ],
        "supports_tool_use": True,
    },
    {
        "name": "amazon-nova-lite",
        "model_id": "amazon.nova-lite-v1:0",
        "model_type": "nova",
        "generation_config": DEFAULT_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00006, "output": 0.00024},
            "us-east-2": {"input": 0.00006, "output": 0.00024},
            "us-west-2": {"input": 0.00006, "output": 0.00024},
            "eu-central-1": {"input": 0.00006, "output": 0.00024},
            "eu-west-1": {"input": 0.00006, "output": 0.00024},
            "eu-west-3": {"input": 0.00006, "output": 0.00024},
            "eu-north-1": {"input": 0.00006, "output": 0.00024},
            "ap-south-1": {"input": 0.00006, "output": 0.00024},
            "ap-northeast-1": {"input": 0.00006, "output": 0.00024},
            "ap-northeast-2": {"input": 0.00006, "output": 0.00024},
            "ap-southeast-1": {"input": 0.00006, "output": 0.00024},
            "ap-southeast-2": {"input": 0.00006, "output": 0.00024},
            "default": {"input": 0.00006, "output": 0.00024},
        },
        "supported_regions": [
            "us-east-1", "us-east-2", "us-west-2",
            "eu-central-1", "eu-west-1", "eu-west-3", "eu-north-1",
            "ap-south-1", "ap-northeast-1", "ap-northeast-2",
            "ap-southeast-1", "ap-southeast-2"
        ],
        "supports_tool_use": True,
    },
    {
        "name": "amazon-nova-micro",
        "model_id": "amazon.nova-micro-v1:0",
        "model_type": "nova",
        "generation_config": DEFAULT_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.000035, "output": 0.00014},
            "us-east-2": {"input": 0.000035, "output": 0.00014},
            "us-west-2": {"input": 0.000035, "output": 0.00014},
            "eu-central-1": {"input": 0.000035, "output": 0.00014},
            "eu-west-1": {"input": 0.000035, "output": 0.00014},
            "eu-west-3": {"input": 0.000035, "output": 0.00014},
            "eu-north-1": {"input": 0.000035, "output": 0.00014},
            "ap-south-1": {"input": 0.000035, "output": 0.00014},
            "ap-northeast-1": {"input": 0.000035, "output": 0.00014},
            "ap-northeast-2": {"input": 0.000035, "output": 0.00014},
            "ap-southeast-1": {"input": 0.000035, "output": 0.00014},
            "ap-southeast-2": {"input": 0.000035, "output": 0.00014},
            "default": {"input": 0.000035, "output": 0.00014},
        },
        "supported_regions": [
            "us-east-1", "us-east-2", "us-west-2",
            "eu-central-1", "eu-west-1", "eu-west-3", "eu-north-1",
            "ap-south-1", "ap-northeast-1", "ap-northeast-2",
            "ap-southeast-1", "ap-southeast-2"
        ],
        "supports_tool_use": True,
    },
    
    # DeepSeek models
    {
        "name": "deepseek-r1",
        "model_id": "deepseek.r1-v1:0",
        "model_type": "deepseek",
        "generation_config": DEFAULT_DEEP_SEEK_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00135, "output": 0.0054},
            "us-east-2": {"input": 0.00135, "output": 0.0054},
            "us-west-2": {"input": 0.00135, "output": 0.0054},
            "default": {"input": 0.00135, "output": 0.0054},
        },
        "supported_regions": ["us-east-1", "us-east-2", "us-west-2"],
        "supports_tool_use": False,
    },
    
    # Meta Llama 3 models
    {
        "name": "llama3-3-70b-instruct",
        "model_id": "meta.llama3-3-70b-instruct-v1:0",
        "model_type": "llama",
        "generation_config": DEFAULT_LLAMA_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00072, "output": 0.00072},
            "us-east-2": {"input": 0.00072, "output": 0.00072},
            "us-west-2": {"input": 0.00072, "output": 0.00072},
            "default": {"input": 0.00072, "output": 0.00072},
        },
        "supported_regions": ["us-east-1", "us-east-2", "us-west-2"],
        "supports_tool_use": True,
    },
    {
        "name": "llama3-2-1b-instruct",
        "model_id": "meta.llama3-2-1b-instruct-v1:0",
        "model_type": "llama",
        "generation_config": DEFAULT_LLAMA_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.0001, "output": 0.0001},
            "us-east-2": {"input": 0.0001, "output": 0.0001},
            "us-west-2": {"input": 0.0001, "output": 0.0001},
            "eu-central-1": {"input": 0.00013, "output": 0.00013},
            "eu-west-1": {"input": 0.00013, "output": 0.00013},
            "eu-west-3": {"input": 0.00013, "output": 0.00013},
            "default": {"input": 0.0001, "output": 0.0001},
        },
        "supported_regions": [
            "us-east-1", "us-east-2", "us-west-2",
            "eu-central-1", "eu-west-1", "eu-west-3"
        ],
        "supports_tool_use": False,
    },
    {
        "name": "llama3-2-3b-instruct",
        "model_id": "meta.llama3-2-3b-instruct-v1:0",
        "model_type": "llama",
        "generation_config": DEFAULT_LLAMA_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00015, "output": 0.00015},
            "us-east-2": {"input": 0.00015, "output": 0.00015},
            "us-west-2": {"input": 0.00015, "output": 0.00015},
            "eu-central-1": {"input": 0.00019, "output": 0.00019},
            "eu-west-1": {"input": 0.00019, "output": 0.00019},
            "eu-west-3": {"input": 0.00019, "output": 0.00019},
            "default": {"input": 0.00015, "output": 0.00015},
        },
        "supported_regions": [
            "us-east-1", "us-east-2", "us-west-2",
            "eu-central-1", "eu-west-1", "eu-west-3"
        ],
        "supports_tool_use": False,
    },
    {
        "name": "llama3-2-11b-instruct",
        "model_id": "meta.llama3-2-11b-instruct-v1:0",
        "model_type": "llama",
        "generation_config": DEFAULT_LLAMA_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00016, "output": 0.00016},
            "us-east-2": {"input": 0.00016, "output": 0.00016},
            "us-west-2": {"input": 0.00016, "output": 0.00016},
            "default": {"input": 0.00016, "output": 0.00016},
        },
        "supported_regions": ["us-east-1", "us-east-2", "us-west-2"],
        "supports_tool_use": True,
    },
    {
        "name": "llama3-2-90b-instruct",
        "model_id": "meta.llama3-2-90b-instruct-v1:0",
        "model_type": "llama",
        "generation_config": DEFAULT_LLAMA_GENERATION_CONFIG,
        "pricing": {
            "us-east-1": {"input": 0.00072, "output": 0.00072},
            "us-east-2": {"input": 0.00072, "output": 0.00072},
            "us-west-2": {"input": 0.00072, "output": 0.00072},
            "default": {"input": 0.00072, "output": 0.00072},
        },
        "supported_regions": ["us-east-1", "us-east-2", "us-west-2"],
        "supports_tool_use": True,
    },
]


def get_model_by_name(name: str) -> Optional[ModelConfig]:
    """Get model configuration by name."""
    for model in MODELS:
        if model["name"] == name:
            return model
    return None


def get_models_by_type(model_type: str) -> List[ModelConfig]:
    """Get all models of a specific type."""
    return [model for model in MODELS if model["model_type"] == model_type]


def get_model_id(name: str, region: str = "us-east-1") -> str:
    """Get the model ID for a given model name and region."""
    model = get_model_by_name(name)
    if not model:
        raise ValueError(f"Unsupported model: {name}")
    
    return model["model_id"]


def get_model_pricing(name: str, region: str = "us-east-1") -> Dict[str, float]:
    """Get pricing information for a model in a specific region."""
    model = get_model_by_name(name)
    if not model:
        raise ValueError(f"Unsupported model: {name}")
    
    # Return region-specific pricing if available, otherwise default
    return model["pricing"].get(region, model["pricing"]["default"])


def get_default_generation_config(name: str) -> GenerationParams:
    """Get the default generation configuration for a model."""
    model = get_model_by_name(name)
    if not model:
        raise ValueError(f"Unsupported model: {name}")
    
    return model["generation_config"]


def is_tool_use_supported(name: str) -> bool:
    """Check if a model supports tool use."""
    model = get_model_by_name(name)
    if not model:
        raise ValueError(f"Unsupported model: {name}")
    
    return model["supports_tool_use"]


def is_model_type(name: str, model_type: str) -> bool:
    """Check if a model is of a specific type."""
    model = get_model_by_name(name)
    if not model:
        raise ValueError(f"Unsupported model: {name}")
    
    return model["model_type"] == model_type


def is_nova_model(name: str) -> bool:
    """Check if the model is an Amazon Nova model."""
    return is_model_type(name, "nova")


def is_deepseek_model(name: str) -> bool:
    """Check if the model is a DeepSeek model."""
    return is_model_type(name, "deepseek")


def is_llama_model(name: str) -> bool:
    """Check if the model is a Meta Llama model."""
    return is_model_type(name, "llama")


def is_mistral(name: str) -> bool:
    """Check if the model is a Mistral model."""
    return is_model_type(name, "mistral")


def is_claude_model(name: str) -> bool:
    """Check if the model is a Claude model."""
    return is_model_type(name, "claude")


def calculate_price(
    model: str,
    input_tokens: int,
    output_tokens: int,
    region: str = "us-east-1",
) -> float:
    """Calculate the price for a model based on input and output tokens."""
    pricing = get_model_pricing(model, region)
    
    return pricing["input"] * input_tokens / 1000.0 + pricing["output"] * output_tokens / 1000.0
