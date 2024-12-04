from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
import time
import env

app = FastAPI()

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(f"Request took {process_time:.4f} seconds")
        return response

app.add_middleware(TimerMiddleware)
