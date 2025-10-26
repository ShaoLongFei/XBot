import random
import asyncio
from openai import AsyncOpenAI
from astrbot import logger
from ..provider import EmbeddingProvider
from ..register import register_provider_adapter
from ..entities import ProviderType


@register_provider_adapter(
    "openai_embedding",
    "OpenAI API Embedding 提供商适配器",
    provider_type=ProviderType.EMBEDDING,
)
class OpenAIEmbeddingProvider(EmbeddingProvider):
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
        
        self.client = AsyncOpenAI(
            api_key=self.chosen_api_key,
            base_url=provider_config.get(
                "embedding_api_base", "https://api.openai.com/v1"
            ),
            timeout=int(provider_config.get("timeout", 20)),
        )
        self.model = provider_config.get("embedding_model", "text-embedding-3-small")
        self.dimension = provider_config.get("embedding_dimensions", 1024)
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
                    self.client.api_key = chosen_key
                embedding = await self.client.embeddings.create(input=text, model=self.model)
                return embedding.data[0].embedding
            except Exception as e:
                last_exception = e
                if "429" in str(e):
                    logger.warning(
                        f"Embedding API 调用过于频繁(429)，尝试使用其他 Key 重试。当前 Key: {chosen_key[:12] if chosen_key else 'None'}"
                    )
                    if retry_cnt < self.max_retries - 1:
                        await asyncio.sleep(min(2 ** retry_cnt, 10))
                    if chosen_key and chosen_key in available_api_keys:
                        available_api_keys.remove(chosen_key)
                    if available_api_keys:
                        chosen_key = random.choice(available_api_keys)
                    else:
                        logger.error("所有 API Key 都已耗尽，无法重试")
                        raise e
                else:
                    raise e
        
        if last_exception:
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
                    self.client.api_key = chosen_key
                embeddings = await self.client.embeddings.create(input=texts, model=self.model)
                return [item.embedding for item in embeddings.data]
            except Exception as e:
                last_exception = e
                if "429" in str(e):
                    logger.warning(
                        f"Embedding API 批量调用过于频繁(429)，尝试使用其他 Key 重试。当前 Key: {chosen_key[:12] if chosen_key else 'None'}"
                    )
                    if retry_cnt < self.max_retries - 1:
                        await asyncio.sleep(min(2 ** retry_cnt, 10))
                    if chosen_key and chosen_key in available_api_keys:
                        available_api_keys.remove(chosen_key)
                    if available_api_keys:
                        chosen_key = random.choice(available_api_keys)
                    else:
                        logger.error("所有 API Key 都已耗尽，无法重试")
                        raise e
                else:
                    raise e
        
        if last_exception:
            raise last_exception

    def get_dim(self) -> int:
        """获取向量的维度"""
        return self.dimension
