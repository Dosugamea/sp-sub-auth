from os import environ
from dotenv import load_dotenv
import Crypto.PublicKey.RSA as RSA

load_dotenv()

# Sonolus official public key to read the user signature.
# More info: https://wiki.sonolus.com/custom-server-specs/endpoints/post-sonolus-authenticate.html
with open("static/sonolus_public_key.pub", "r") as f:
    PUBLIC_KEY = RSA.importKey(f.read().strip())

CORS_ORIGINS = environ.get("CORS_ORIGINS", "*").split(",")
DISCORD_CALLBACK_ADDRESS = environ.get("DISCORD_CALLBACK_ADDRESS", None)
DISCORD_CALLBACK_REDIRECT = environ.get(
    "DISCORD_CALLBACK_REDIRECT", "https://example.com"
)
DISCORD_CLIENT_ID = environ.get("DISCORD_CLIENT_ID", None)
DISCORD_CLIENT_SECRET = environ.get("DISCORD_CLIENT_SECRET", None)
