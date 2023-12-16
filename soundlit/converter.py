"""AudioConverter it's classs for converting audio files to only supported formats"""

__all__ = ["AudioConverter"]

from typing import Union, AnyStr, Optional
import os
import io
from pathlib import Path
from subprocess import Popen, PIPE
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
import ffmpeg


class AudioConverter:
    __common_extensions = [
        "wav", "mp3",
        "ogg", "flac"
    ]

    def __init__(self,
                 common_extensions: Optional[list[str, ...]] = None,
                 convert_to: Optional[str] = "wav",
                 ac: Optional[int] = 1,
                 ):
        if not isinstance(common_extensions, list):
            common_extensions = self.__common_extensions
        self.common_extensions = common_extensions
        self.convert_to = convert_to
        self.ac = ac
        self.root_dir = os.getcwd()

    def convert(self, path: str | Path) -> AnyStr:
        return Popen(
            ["ffmpeg", "-hide_banner", "-i", f"{path}", "-f", f"{self.convert_to}", "-"],
            stdout=PIPE
        ).stdout.read()

    def check_extension(self, filename: str | Path) -> Union[None, str]:
        if filename.split(".")[-1] not in self.common_extensions:
            return filename

    def define_location(self, file_id: str, extension: str) -> str:
        return os.path.join(self.root_dir, f"{file_id}.{extension}")

    @staticmethod
    def write(path: Union[str, Path], data: io.BytesIO | bytes) -> None:
        with open(path, "wb") as f:
            f.write(data)

    def __call__(self, source: UploadedFile) -> bytes | AnyStr:
        data = source.getvalue()
        if not self.check_extension(source.name):
            return data
        else:
            in_path = self.define_location(source.file_id, source.name.split(".")[-1])
            try:
                self.write(in_path, source.getbuffer())
                data = self.convert(in_path)
            except Exception as e:
                st.error(f"We're sorry, something happened to the server ⚡️ \n{e}")
            else:
                return data
            finally:
                if os.path.exists(in_path):
                    os.remove(in_path)
