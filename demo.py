from soundlit import AudioWidget
import streamlit as st


st.image("./assets/sound.gif")
audio_widget = AudioWidget()
audio_widget.get_audio()
