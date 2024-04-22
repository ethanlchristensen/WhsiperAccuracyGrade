from dotenv import load_dotenv
import openai
import json
import io
import os

load_dotenv()
client = openai.OpenAI()
audio_chunk_transcriptions = {}

if len(os.listdir('audio_chunks')) == 0:
    print('No audio chunks to transcibe. Exiting.')
    exit(1)

for audio_file_name in os.listdir('audio_chunks'):
    print(f'transcribing {audio_file_name}')
    
    audio_file = open(f'audio_chunks\\{audio_file_name}', 'rb')
    transcription = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_file,
    )

    audio_chunk_transcriptions[audio_file_name] = transcription.text

with open('audio_data\\chunk_transcriptions.json', 'w') as file:
    json.dump(audio_chunk_transcriptions, file, indent=4)