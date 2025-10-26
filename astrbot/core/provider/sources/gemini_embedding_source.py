import random
import asyncio
from google import genai
from google.genai import types
from google.genai.errors import APIError
from astrbot import logger
from ..provider import EmbeddingProvider
from ..register import register_provider_adapter
from ..entities import ProviderType


@register_provider_adapter(
    "gemini_embedding",
    "Google Gemini Embedding 提供商适配器",
    provider_type=ProviderType.EMBEDDING,
)
class GeminiEmbeddingProvider(EmbeddingProvider):
    def __init__(self, provider_config: dict, provider_settings: dict) -> None:
        super().__init__(provider_config, provider_settings)
        self.provider_config = provider_config
        self.provider_settings = provider_settings

        api_key = provider_config.get("embedding_api_key")
        if isinstance(api_key, list):
            self.api_keys = api_key
        else:
            self.api_keys = [api_key] if api_key else []
        
        self.chosen_api_key = self.api_keys[0] if self.api_keys else None
        
        api_base: str = provider_config.get("embedding_api_base", None)
        timeout: int = int(provider_config.get("timeout", 20))

        http_options = types.HttpOptions(timeout=timeout * 1000)
        if api_base:
            if api_base.endswith("/"):
                api_base = api_base[:-1]
            http_options.base_url = api_base

        self.client = genai.Client(api_key=self.chosen_api_key, http_options=http_options).aio
        self.http_options = http_options

        self.model = provider_config.get(
            "embedding_model", "gemini-embedding-exp-03-07"
        )
        self.dimension = provider_config.get("embedding_dimensions", 768)
        self.max_retries = 5

    async def get_embedding(self, text: str) -> list[float]:
        """
        获取文本的嵌入，支持重试和 API Key 轮换
        """
        available_api_keys = self.api_keys.copy()
        chosen_key = random.choice(available_api_keys) if available_api_keys else None
        
        last_exception = None
        for retry_cnt in range(self.max_retries):
            try:
                if chosen_key:
                    self.client = genai.Client(api_key=chosen_key, http_options=self.http_options).aio
                result = await self.client.models.embed_content(
                    model=self.model, contents=text
                )
                return result.embeddings[0].values
            except APIError as e:
                last_exception = e
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    logger.warning(
                        f"Gemini Embedding API 调用过于频繁(429)，尝试使用其他 Key 重试。当前 Key: {chosen_key[:12] if chosen_key else 'None'}"
                    )
                    if retry_cnt < self.max_retries - 1:
                        await asyncio.sleep(min(2 ** retry_cnt, 10))
                    if chosen_key and chosen_key in available_api_keys:
                        available_api_keys.remove(chosen_key)
                    if available_api_keys:
                        chosen_key = random.choice(available_api_keys)
                    else:
                        logger.error("所有 API Key 都已耗尽，无法重试")
                        raise Exception(f"Gemini Embedding API请求失败: {e.message}")
                else:
                    raise Exception(f"Gemini Embedding API请求失败: {e.message}")
            except Exception as e:
                last_exception = e
                raise e
        
        if last_exception:
            if isinstance(last_exception, APIError):
                raise Exception(f"Gemini Embedding API请求失败: {last_exception.message}")
            raise last_exception

    async def get_embeddings(self, texts: list[str]) -> list[list[float]]:
        """
        批量获取文本的嵌入，支持重试和 API Key 轮换
        """
        available_api_keys = self.api_keys.copy()
        chosen_key = random.choice(available_api_keys) if available_api_keys else None
        
        last_exception = None
        for retry_cnt in range(self.max_retries):
            try:
                if chosen_key:
                    self.client = genai.Client(api_key=chosen_key, http_options=self.http_options).aio
                result = await self.client.models.embed_content(
                    model=self.model, contents=texts
                )
                return [embedding.values for embedding in result.embeddings]
            except APIError as e:
                last_exception = e
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    logger.warning(
                        f"Gemini Embedding API 批量调用过于频繁(429)，尝试使用其他 Key 重试。当前 Key: {chosen_key[:12] if chosen_key else 'None'}"
                    )
                    if retry_cnt < self.max_retries - 1:
                        await asyncio.sleep(min(2 ** retry_cnt, 10))
                    if chosen_key and chosen_key in available_api_keys:
                        available_api_keys.remove(chosen_key)
                    if available_api_keys:
                        chosen_key = random.choice(available_api_keys)
                    else:
                        logger.error("所有 API Key 都已耗尽，无法重试")
                        raise Exception(f"Gemini Embedding API批量请求失败: {e.message}")
                else:
                    raise Exception(f"Gemini Embedding API批量请求失败: {e.message}")
            except Exception as e:
                last_exception = e
                raise e
        
        if last_exception:
            if isinstance(last_exception, APIError):
                raise Exception(f"Gemini Embedding API批量请求失败: {last_exception.message}")
            raise last_exception

    def get_dim(self) -> int:
        """获取向量的维度"""
        return self.dimension
