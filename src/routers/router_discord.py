from fastapi import APIRouter
from config import (
    DISCORD_CLIENT_ID,
    DISCORD_CLIENT_SECRET,
    DISCORD_CALLBACK_ADDRESS,
)
from lib.auth_discord import DiscordAuth

discord_router = APIRouter()
discord_auth = DiscordAuth(
    DISCORD_CLIENT_ID,
    DISCORD_CLIENT_SECRET,
    DISCORD_CALLBACK_ADDRESS,
)


@discord_router.get("/discord/login")
async def start_discord_auth():
    """認証開始エンドポイント(仮)"""
    return discord_auth.get_login_url()


@discord_router.get("/discord/callback")
async def auth_discord_auth(code: str):
    """認証エンドポイント(仮)"""
    token = await discord_auth.get_discord_token(code)
    return token
