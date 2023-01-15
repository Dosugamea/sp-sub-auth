from dataclasses import dataclass
from fastapi import FastAPI


@dataclass
class AuthResponse:
    text: str


app = FastAPI(
    title="SweetPotato Authorization Server",
    description="Discord and sonolus authorization",
    version="0.1.0",
)


@app.get("/health_check")
async def health_check():
    """生存確認用エンドポイント"""
    return {"message": "Server is working"}


@app.post("/auth")
async def authorization():
    """認証エンドポイント(仮)"""
    return "Not yet implemented!"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True)
