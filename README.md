# Real-Time Voice Chat API

A **Real-Time Voice Chat API** built in Python, leveraging WebSockets for communication, FastAPI for backend functionality, LangChain and Google Generative AI for natural language processing (NLP), Vosk for speech-to-text transcription, and Amazon Polly for voice response generation.

---

## Features

- **Real-Time Audio Streaming**: Facilitates seamless bi-directional audio communication using WebSockets.
- **Speech-to-Text**: Transcribes real-time audio to text with high accuracy using the Vosk library.
- **Language Understanding**: Utilizes LangChain and Google Generative AI for processing user queries and generating intelligent responses.
- **Text-to-Speech**: Converts responses into natural-sounding speech using Amazon Polly.
- **Fast and Scalable**: Built with FastAPI to ensure low-latency and high-performance communication.

---

## Tech Stack

- **Python**: Core programming language for backend development.
- **FastAPI**: Framework for building APIs efficiently.
- **WebSockets**: Enables real-time, bi-directional communication.
- **LangChain**: Framework for combining language models with external tools.
- **Google Generative AI**: Provides the power of advanced large language models (LLMs).
- **Vosk**: Offline speech recognition toolkit for real-time transcription.
- **Amazon Polly**: Generates human-like voice responses.

---

## Architecture Overview

1. **Client**:
   - Streams audio data to the server via WebSockets.
   - Receives synthesized voice responses from the server.

2. **Server**:
   - **Audio Processing**:
     - Accepts incoming audio streams.
     - Uses Vosk to transcribe speech into text.
   - **Query Handling**:
     - Processes transcribed text using LangChain and Google Generative AI.
     - Generates meaningful responses based on user input.
   - **Voice Generation**:
     - Converts textual responses to audio using Amazon Polly.
   - Streams the synthesized audio back to the client.

---
## Demo video 
[LINK]("https://drive.google.com/file/d/1HvX8YjZ_DtHc44eRGdLWxqg_B6S9tLV3/view?usp=sharing")

- Python 3.9 or higher
- `pip` package manager
- AWS credentials for Amazon Polly
- Access to Google Generative AI API
