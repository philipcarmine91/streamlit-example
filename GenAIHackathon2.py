import streamlit as st
import pyaudio
import wave
import speech_recognition as sr
import tempfile
import os
from pydub import AudioSegment
from pydub.playback import play

# Initialize the recognizer
recognizer = sr.Recognizer()
audio_stream = None

# Function to start recording
def start_recording():
    global audio_stream
    audio_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    st.text("Recording...")

# Function to stop recording and generate transcript
def stop_recording():
    global audio_stream
    if audio_stream is not None:
        st.text("Recording stopped.")
        audio_stream.stop_stream()
        audio_stream.close()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            temp_audio_filename = temp_audio.name
            temp_audio.close()
            audio_file = wave.open(temp_audio_filename, 'wb')
            audio_file.setnchannels(1)
            audio_file.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
            audio_file.setframerate(16000)

            audio_data = []
            while True:
                chunk = audio_stream.read(1024)
                if not chunk:
                    break
                audio_file.writeframes(chunk)
                audio_data.append(chunk)

            audio_file.close()

        audio_file = sr.AudioFile(temp_audio_filename)
        with audio_file as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                st.text("Transcript:")
                st.write(text)
            except sr.UnknownValueError:
                st.text("Google Speech Recognition could not understand the audio.")
            except sr.RequestError as e:
                st.text(f"Could not request results from Google Speech Recognition service; {e}")

        # Play the recorded audio back
        audio = AudioSegment.from_wav(temp_audio_filename)
        play(audio)

        os.remove(temp_audio_filename)

# Streamlit UI
st.title("Audio Recording and Transcript Generation")

if st.button("Start Recording"):
    start_recording()

if st.button("Stop Recording and Generate Transcript"):
    stop_recording()
