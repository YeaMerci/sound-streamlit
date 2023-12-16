"""Streamlit component for audio recording and uploading."""

__all__ = ["AudioWidget"]

from typing import Union, AnyStr, Optional
from pathlib import Path
import os
import io
from io import BytesIO

import librosa
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from .recorder import st_audiorec
from .converter import AudioConverter


class AudioWidget(AudioConverter):
    """
    Custom streamlit component for audio recording and uploading.
    :param min_duration: minimum duration of audio file (By default: 0 seconds)
    :param max_duration: maximum duration of audio file (By default: 60_000 seconds)
    :param available_formats: audio files with which formats available for uploading
    :param convert_to: what format to convert an audio file into if it needs to be converted (By default .wav)
    :param execlude_convert: audio files with which formats do not require conversion to a supported format
    :param sample_rate: sampling rate to which the audio file will be resampled
    :param mono: convert waveform to mono format with one channel if True else load 2 channels
    """

    __default_extensions = [
        ".wav", ".aac",
        ".ogg", ".mp3",
        ".aiff", ".flac",
        ".ape", ".dsd",
        ".mqa", ".wma",
        ".m4a"
    ]

    def __init__(self,
                 min_duration: Optional[int] = None,
                 max_duration: Optional[int] = None,
                 available_formats: Optional[str] = None,
                 convert_to: Optional[str] = "wav",
                 execlude_convert: Optional[list[str]] = None,
                 sample_rate: Optional[int] = 22050,
                 mono: Optional[bool] = True
                 ):
        super().__init__(execlude_convert, convert_to, (1 if mono else 2))
        if not available_formats:
            available_formats = self.__default_extensions

        self.available_formats = available_formats
        self.min_duration = min_duration if min_duration else 0
        self.max_duration = max_duration if max_duration else int(60e+3)
        self.sample_rate = sample_rate
        self.mono = mono

    def _safe_load(self, data: io.BytesIO) -> tuple[np.ndarray, int]:
        return librosa.load(data, sr=self.sample_rate, mono=self.mono)

    def __check_duration(self, data: AnyStr | bytes) -> tuple[np.ndarray, int]:
        audio, sr = librosa.load(io.BytesIO(data), sr=None)
        duration = librosa.get_duration(y=audio, sr=sr)
        if (duration >= self.min_duration) and (duration <= self.max_duration):
            return self._safe_load(io.BytesIO(data))
        if duration > self.max_duration:
            st.error(
                f"Oops! Length of the heartbeat audio recording "
                f"must be less than {self.max_duration} seconds, "
                f"but the length is {round(duration, 2)} seconds. "
                f"Please try again.",
                icon="😮"
            )
        if duration < self.min_duration:
            st.error(
                f"Oops! Length of the heartbeat audio recording "
                f"must be at least {self.min_duration} seconds, "
                f"but the length is {round(duration, 2)} seconds. "
                f"Please try again.",
                icon="😮"
            )

    def record_audio(self) -> tuple[np.ndarray, int]:
        data = st_audiorec()
        if data is not None:
            return self.__check_duration(data)

    def load_audio(self) -> Union[bytes, None]:
        data = st.file_uploader(
            label=f"Upload an audio file of your heartbeat "
                  f"that more or equal {self.min_duration} and "
                  f"less or equal {self.max_duration} seconds.",
            type=self.available_formats
        )
        if data:
            st.audio(data)
            data = self.__call__(data)
            return self.__check_duration(data)

    def get_audio(self, sidebar: Optional[bool] = True) -> tuple[np.ndarray, int]:
        placeholder = st.sidebar if sidebar else st
        choice = placeholder.selectbox(
            label="Do you want to upload or record an audio file?",
            options=["Upload 📁", "Record 🎤"]
        )
        if choice == "Upload 📁":
            return self.load_audio()
        return self.record_audio()
