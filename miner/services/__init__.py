from typing import Union
from .prompt import PromptService
from .image import ImageService
from .embedding import EmbeddingService

ALL_SERVICE_TYPE = Union[PromptService, ImageService, EmbeddingService]
__all__ = [PromptService, ImageService, EmbeddingService, ALL_SERVICE_TYPE]
