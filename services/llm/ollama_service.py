import json
import httpx

from core.config.settings import settings
from core.logging.logger import logger


class OllamaService:
    def __init__(self, model: str = "mistral"):
        self.model = model

    async def generate(self, messages: list):

        logger.info(f"Sending request to model: {self.model}")

        async with httpx.AsyncClient() as client:

            response = await client.post(
                f"{settings.OLLAMA_BASE_URL}/api/chat",
                json={"model": self.model, "messages": messages, "stream": False},
            )

        logger.info("Response received")

        data = response.json()

        return data["message"]["content"]

    async def stream_generate(self, messages: list):

        logger.info(f"Streaming response from model: {self.model}")

        async with httpx.AsyncClient(timeout=None) as client:

            async with client.stream(
                "POST",
                f"{settings.OLLAMA_BASE_URL}/api/chat",
                json={"model": self.model, "messages": messages, "stream": True},
            ) as response:

                async for line in response.aiter_lines():

                    if line:

                        try:
                            data = json.loads(line)

                            content = data.get("message", {}).get("content", "")

                            if content:
                                yield content

                        except Exception:
                            continue
