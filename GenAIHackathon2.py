import streamlit as st
import pyaudio
import wave
import threading
import speech_recognition as sr

# Function to start and stop recording
def record_audio(filename, frames, p):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    st.text("Recording...")

    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    st.text("Recording stopped.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

# Initialize Streamlit
st.title("Build your CV")

# Control variable for recording
recording = False

# Initialize recording frames
frames = []

# Create a button to start and stop recording
if not recording:
    if st.button("Start Recording"):
        recording = True
        frames = []
        thread = threading.Thread(target=record_audio, args=("recording.wav", frames, p))
        thread.start()
else:
    if st.button("Stop Recording"):
        recording = False

if st.checkbox("Play Recorded Audio"):
    if frames:
        audio = b''.join(frames)
        st.audio(audio, format="audio/wav")

# Create a button to transcribe the recorded audio
if st.button("Transcribe Recorded Audio"):
    audio = b''.join(frames)
    r = sr.Recognizer()
    with sr.AudioData(audio, sample_rate=44100) as source:
        try:
            transcript = r.recognize_google(source)
            st.subheader("Transcript:")
            st.write(transcript)
        except sr.UnknownValueError:
            st.write("Could not understand audio")
        except sr.RequestError as e:
            st.write(f"Could not request results: {e}")