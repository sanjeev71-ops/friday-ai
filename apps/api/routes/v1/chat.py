from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services.llm.ollama_service import OllamaService
from apps.api.schemas.chat import ChatRequest

router = APIRouter()

llm_service = OllamaService()

chat_history = []


@router.post("/chat")
async def chat(request: ChatRequest):

    chat_history.append({"role": "user", "content": request.message})

    async def response_generator():

        full_response = ""

        async for chunk in llm_service.stream_generate(chat_history):

            full_response += chunk

            yield chunk

        chat_history.append({"role": "assistant", "content": full_response})

    return StreamingResponse(response_generator(), media_type="text/plain")
