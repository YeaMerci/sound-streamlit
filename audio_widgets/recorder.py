"""Docstring"""

__all__ = ["AudioRecorder"]

from typing import Union, AnyStr, Optional
from pathlib import Path
import os
import io
from io import BytesIO

import librosa
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1.components import CustomComponent
from .converter import AudioConverter
from utils.variables import ROOT_DIR


class AudioRecorder(AudioConverter):
    __default_extensions = [
        ".wav", ".aac",
        ".ogg", ".mp3",
        ".aiff", ".flac",
        ".ape", ".dsd",
        ".mqa", ".wma",
        ".m4a"
    ]

    def __init__(self,
                 duration: Optional[int] = 10,
                 valid_extensions: Optional[list[str]] = None,
                 convert_to: Optional[str] = "wav",
                 sample_rate: Optional[int] = 22050,
                 mono: Optional[bool] = True
                 ):
        super().__init__(valid_extensions, convert_to, (1 if mono else 2), ROOT_DIR)
        self.duration = duration
        self.sample_rate = sample_rate
        self.mono = mono

    @staticmethod
    def __init_audiorec() -> CustomComponent:
        # get parent directory relative to current directory
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        # custom REACT-based component for recording client audio in browser
        build_dir = os.path.join(parent_dir, "frontend/build")
        # specify directory and initialize st_audiorec object functionality
        return components.declare_component("st_audiorec", path=build_dir)

    def st_audiorec(self) -> bytes:
        st_audiorec = self.__init_audiorec()
        # Create an instance of the component: STREAMLIT AUDIO RECORDER
        raw_audio_data = st_audiorec()  # raw_audio_data: stores all the data returned from the streamlit frontend
        wav_bytes = None  # wav_bytes: contains the recorded audio in .WAV format after conversion

        # the frontend returns raw audio data in the form of arraybuffer
        # (this arraybuffer is derived from web-media API WAV-blob data)

        if isinstance(raw_audio_data, dict):  # retrieve audio data
            with st.spinner('retrieving audio-recording...'):
                ind, raw_audio_data = zip(*raw_audio_data['arr'].items())
                ind = np.array(ind, dtype=int)  # convert to np array
                raw_audio_data = np.array(raw_audio_data)  # convert to np array
                sorted_ints = raw_audio_data[ind]
                stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
                # wav_bytes contains audio data in byte format, ready to be processed further
                wav_bytes = stream.read()
        return wav_bytes

    def __check_duration(self, data: AnyStr | bytes) -> io.BytesIO:
        audio, sr = librosa.load(io.BytesIO(data), sr=self.sample_rate, mono=self.mono)
        duration = librosa.get_duration(y=audio, sr=self.sample_rate)
        if duration >= self.duration:
            return io.BytesIO(data)
        else:
            st.error(
                f"Oops! Length of the heartbeat audio recording "
                f"must be at least {self.duration} seconds, "
                f"but the length is {round(duration, 2)} seconds. "
                f"Please try again.",
                icon="😮"
            )

    def _record_audio(self) -> AnyStr:
        data = self.st_audiorec()
        if data is not None:
            return self.__check_duration(data)

    def _load_audio(self) -> Union[bytes, None]:
        data = st.file_uploader(
            label=f"Upload an audio file of your heartbeat "
                  f"that is at least {self.duration} seconds long.",
            type=self.__default_extensions
        )
        if data:
            st.audio(data)
            data = self.__call__(data)
            return self.__check_duration(data)

    def get_audio(self) -> io.BytesIO:
        choice = st.sidebar.selectbox(
            label="Do you want to upload or record an audio file?",
            options=["Upload 📁", "Record 🎤"]
        )
        if choice == "Upload 📁":
            return self._load_audio()
        return self._record_audio()
