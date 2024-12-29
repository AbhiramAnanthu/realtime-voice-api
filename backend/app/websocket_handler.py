import os
import json
import boto3
import pyaudio
import numpy as np
from fastapi import FastAPI, WebSocket
from fastapi.websockets import WebSocketDisconnect
from vosk import KaldiRecognizer, Model
from langchain_google_genai import ChatGoogleGenerativeAI
from chain_config import query_with_llm
from dotenv import load_dotenv

RATE = 44100
FORMAT = pyaudio.paInt16
FRAMES_PER_BUFFER = 1024
CHANNELS = 1

path = "./.env"
load_dotenv(dotenv_path=path)

model_path = "../models/vosk-model-en-in-0.5"
app = FastAPI()
model = Model(model_path=model_path)
recognizer = KaldiRecognizer(model, RATE)

llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("GOOGLE_API_KEY"), model="gemini-1.5-flash"
)
polly = boto3.client(
    "polly",
    region_name="us-east-1",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS"),
)

audio = pyaudio.PyAudio()
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=16000,
    frames_per_buffer=FRAMES_PER_BUFFER,
    output=True,
)


@app.get("/")
def index_page():
    return {"message": "Websocket for audio streaming started"}


@app.websocket("/audio-stream")
async def stream_audio(websocket: WebSocket):
    print("[CONNECTED] Client Connected")

    await websocket.accept()

    try:
        async for message in websocket.iter_bytes():
            if recognizer.AcceptWaveform(message):
                input_transcript = json.loads(recognizer.Result())
                if input_transcript["text"] != "":
                    prompt = input_transcript["text"]
                    response_llm_text = query_with_llm(prompt)
                    response_speech = polly.synthesize_speech(
                        Text=response_llm_text,
                        OutputFormat="pcm",
                        VoiceId="Joanna",
                    )

                    if "AudioStream" in response_speech:
                        data = response_speech["AudioStream"].read()
                        await websocket.send_bytes(data)

    except WebSocketDisconnect:
        print("[DISCONNECTED] Client disconnected")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5050)
