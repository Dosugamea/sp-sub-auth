from dataclasses import dataclass
import urllib.parse
import httpx


@dataclass
class DiscordTokenResponse:
    access_token: str
    expire_in: int
    refresh_token: str
    scope: str
    token_type: str


class DiscordAuth:
    client_id: str
    client_secret: str
    redirect_uri: str
    SCOPE = ["identify", "email"]
    DISCORD_AUTH_START_URL = "https://discord.com/api/oauth2/authorize"
    DISCORD_AUTH_TOKEN_URL = "https://discordapp.com/api/oauth2/token"

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_login_url(self) -> str:
        params = urllib.parse.urlencode(
            {
                "client_id": self.client_id,
                "redirect_uri": self.redirect_uri,
                "response_type": "code",
                "scope": self.SCOPE,
            }
        )
        return f"{self.DISCORD_AUTH_START_URL}?{params}"

    async def get_discord_token(self, code: str) -> str:
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri,
            "scope": self.SCOPE,
        }
        async with httpx.AsyncClient() as client:
            resp = await client.get(self.DISCORD_AUTH_TOKEN_URL, params=params)
        if resp.status_code != 200:
            return "Failed to get access token"
        token = DiscordTokenResponse(**resp.json())
        return token.access_token
