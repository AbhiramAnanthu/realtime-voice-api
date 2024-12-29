import asyncio
import websockets
import pyaudio

# WebSocket server URL
SERVER_URL = "ws://127.0.0.1:5050/audio-stream"

# PyAudio configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

async def send_audio(websocket):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    try:
        while True:
            data = stream.read(CHUNK)
            await websocket.send(data)
    except asyncio.CancelledError:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

async def receive_audio(websocket):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=16000, output=True, frames_per_buffer=CHUNK)
    
    try:
        async for message in websocket:
            stream.write(message)
    except asyncio.CancelledError:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

async def main():
    async with websockets.connect(SERVER_URL) as websocket:
        send_task = asyncio.create_task(send_audio(websocket))
        receive_task = asyncio.create_task(receive_audio(websocket))
        
        await asyncio.gather(send_task, receive_task)

if __name__ == "__main__":
    asyncio.run(main())