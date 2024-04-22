from streamlit_extras.colored_header import colored_header
import streamlit as st
import pandas as pd
import datetime
import json
import os

COLUMN_SPEC = [0.6, 1, 1, 0.5, 1]
SCROLLABLE_TEXTBOX_HEIGHT = 100
SUBMIT = None


def header():
    global SUBMIT
    title_columns = st.columns([1, 0.10])
    with title_columns[0]:
        colored_header(
            label="Whisper Accuracy Test",
            description="Site to listen to audio chunks and read generated transcripts and mark them as accurate or not accurate.",
            color_name="blue-green-50",
        )
    with title_columns[1]:
        SUBMIT = st.button(label='Save Results')
    
    header_columns = st.columns(COLUMN_SPEC)
    with header_columns[0]:
        colored_header(label="Chunk Name", description="", color_name="blue-30")
    with header_columns[1]:
        colored_header(label="Chunk Audio", description="", color_name="blue-40")
    with header_columns[2]:
        colored_header(
            label="Whisper Transcription", description="", color_name="blue-60"
        )
    with header_columns[3]:
        colored_header(label="Accurate?", description="", color_name="blue-70")
    with header_columns[4]:
        colored_header(label="Comments", description="", color_name="blue-80")

st.set_page_config(page_title="Whisper Test", layout="wide")
header()

containers = []
whisper_transcripts = json.loads(open("audio_data\\chunk_transcriptions.json", "r").read())

for audio_file_name in os.listdir("audio_chunks"):
    container = st.container()
    columns = st.columns(COLUMN_SPEC)
    container.columns = columns

    with columns[0]:
        st.markdown(f"#### {audio_file_name}")
    with columns[1]:
        st.audio(data=open(f"audio_chunks\\{audio_file_name}", "rb").read())
    with columns[2]:
        st.markdown(f"```{whisper_transcripts[audio_file_name]}```")
    with columns[3]:
        st.toggle(label="Accurate", key=f"accurate_{audio_file_name}")
        st.number_input(
            label="% Accurate",
            key=f"accuracy_{audio_file_name}",
            min_value=0.00,
            max_value=1.00,
            step=0.01,
        )
    with columns[4]:
        st.text_area(
            label="Comment / Justification",
            key=f"comments_{audio_file_name}",
        )

    st.divider()


if SUBMIT:
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    out_data = []
    for audio_file_name in os.listdir('audio_chunks'):
        file_data = {'name': audio_file_name}
        for key in st.session_state:
            if audio_file_name in key:
                if 'comments' in key:
                    file_data['comments'] = st.session_state[key]
                elif 'accurate' in key:
                    file_data['is_accurate'] = st.session_state[key]
                elif 'accuracy' in key:
                    file_data['accuracy'] = st.session_state[key]
        out_data.append(file_data)
    df = pd.DataFrame(out_data)
    df.to_csv(f'results\\{current_datetime}_result.csv', index=False)
        
    