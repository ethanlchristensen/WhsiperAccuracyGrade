import os

def is_wav_in():
    for file in os.listdir('audio_data'):
        if file.endswith('.wav'):
            return True
    return False

if not os.path.exists('audio_chunks'):
    os.makedirs('audio_chunks')
if not os.path.exists('audio_data'):
    os.makedirs('audio_data')
if not os.path.exists('results'):
    os.makedirs('results')

while not is_wav_in():
    input('Place a sample wav file in the \'audio_data\' folder. Press [ENTER] when done.')

print('Splitting the audio into 15 second chunks.')
os.system('python prep_sample.py')
print('Transcribing the 15 second chunks using whisper websocket.')
os.system('python transcribe_chunks.py')
print('Done.')
