import os
import json
from fastapi import FastAPI, WebSocket
from fastapi.websockets import WebSocketDisconnect
from dotenv import load_dotenv

path = "./env"
load_dotenv(dotenv_path=path)

app = FastAPI()


@app.get("/")
def index_page():
    return {"message": "Websocket for audio streaming started"}


@app.websocket("/audio-stream")
async def stream_audio(websocket: WebSocket):
    print("[CONNECTED] Client Connected")

    await websocket.accept()

    try:
        async for message in websocket.iter_bytes():
            pass
    except WebSocketDisconnect:
        print("[DISCONNECTED] Client disconnected")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5050)
