import Crypto.PublicKey.RSA as RSA

# Sonolus official public key to read the user signature.
# More info: https://wiki.sonolus.com/custom-server-specs/endpoints/post-sonolus-authenticate.html
with open("static/sonolus_public_key.pub", "r") as f:
    PUBLIC_KEY = RSA.importKey(f.read().strip())
