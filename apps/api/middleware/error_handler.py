from fastapi import Request
from fastapi.responses import JSONResponse

from core.logging.logger import logger


async def global_exception_handler(request: Request, exc: Exception):

    logger.error(f"Unhandled error: {str(exc)}")

    return JSONResponse(status_code=500, content={"error": "Internal server error"})
