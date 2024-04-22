from google.cloud import speech
import json
import io
import os

# create a client
client = speech.SpeechClient()

audio_chunk_transcriptions = {}

for audio_file_name in os.listdir('audio_chunks'):
    print(f'transcribing {audio_file_name}')
    # load audio file
    with io.open(f'audio_chunks\\{audio_file_name}', 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US',
        audio_channel_count = 2,
    )

    # detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    text = ''

    for result in response.results:
        text += result.alternatives[0].transcript
    
    audio_chunk_transcriptions[audio_file_name] = text

with open('audio_data\\chunk_transcriptions.json', 'w') as file:
    json.dump(audio_chunk_transcriptions, file, indent=4)