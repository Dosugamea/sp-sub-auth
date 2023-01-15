from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from config import CORS_ORIGINS
from routers.router_discord import discord_router

app = FastAPI(
    title="SweetPotato Authorization Server",
    description="Discord and sonolus authorization",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health_check")
async def health_check():
    """生存確認用エンドポイント"""
    return {"message": "Server is working"}


app.include_router(discord_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
