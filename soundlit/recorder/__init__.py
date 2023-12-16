import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components
from streamlit.components.v1.components import CustomComponent


def _build_component() -> CustomComponent:
    """
    Get parent directory relative to current directory.
    Custom REACT-based component for recording client audio in browser.
    Specify directory and initialize st_audiorec object functionality.
    """
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    return components.declare_component("recorder", path=build_dir)


def st_audiorec():
    st_audiorec = _build_component()
    # Create an instance of the component: STREAMLIT AUDIO RECORDER
    raw_audio_data = st_audiorec()  # raw_audio_data: stores all the data returned from the streamlit frontend
    wav_bytes = None                # wav_bytes: contains the recorded audio in .WAV format after conversion

    # the frontend returns raw audio data in the form of arraybuffer
    # (this arraybuffer is derived from web-media API WAV-blob data)

    if isinstance(raw_audio_data, dict):  # retrieve audio data
        with st.spinner("retrieving audio-recording..."):
            ind, raw_audio_data = zip(*raw_audio_data["arr"].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            raw_audio_data = np.array(raw_audio_data)  # convert to np array
            sorted_ints = raw_audio_data[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            # wav_bytes contains audio data in byte format, ready to be processed further
            wav_bytes = stream.read()
    return wav_bytes
