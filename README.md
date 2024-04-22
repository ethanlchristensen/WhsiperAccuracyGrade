# Whisper Test

## Setup
Run the `setup.bat` file first.

```bash
setup.bat
```

When prompted, drag a sample call `.wav` file into the `audio_data` folder and press enter. This will chunk the audio into 15 second chunks and call a service to transcribe each chunk.

## Grading the results
After running the setup with an audio file, run the `run.bat` file to run the streamlit app and make a grade.

```bash
run.bat
```

You will have a site with rows for each 15-second chunk. For each chunk, listen to the audio and compare it against the transcription.
- Rate the transcription as accurate or not.
- Give the transcription an accuracy 0% - 100%
- Leave comments about the transcription / reason for grade.

Once finished with this, click the `Save Results` button at the top of the page to save your grade to a csv in the results folder.