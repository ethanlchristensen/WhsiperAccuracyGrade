"""
File to take a sample audio file and split it into
15 second chunks and save those chunks to the 
'audio_chunks' folder.
"""


from pydub import AudioSegment
import os

def split_wav(input_file, output_folder, chunk_length_ms=15000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    sound = AudioSegment.from_wav(input_file)
    
    total_duration = len(sound)

    for i, start in enumerate(range(0, total_duration, chunk_length_ms)):
        end = min(start + chunk_length_ms, total_duration)
        chunk = sound[start:end]
        output_file = os.path.join(output_folder, f'chunk_{i}.wav')
        chunk.export(output_file, format='wav')

input_wav = None
for file in os.listdir('audio_data'):
    if file.endswith('.wav'):
        input_wav = f'audio_data\\{file}'

if not input_wav:
    print('No .wav was found in the \'audio_data\' folder. Exiting.')
    exit(1)
output_folder = 'audio_chunks'
split_wav(input_wav, output_folder)
