# sound-streamlit

**sound-streamlit is a custom widget for working with audio built into streamlit. 
You only need to import one class that will allow you to record or load audio. 
Any audio format is supported, and in the parameters you can set the sample rate, 
minimum or maximum audio length and much more.
Ask any questions. I will be very grateful if you rate the repository ⭐️**


## Installation & setup
### 1. Install widget from PyPI
```shell
pip install sound-streamlit
```
### 2. Make sure that you have the C++ ffmpeg library installed on your computer. 
<br>Its absence will lead to an [error](https://stackoverflow.com/questions/62470863/ffmpeg-command-not-found-but-pip-list-shows-ffmpeg).<br> 
If you are not sure that you have it, then run the command below (only for Unix)
```shell
sudo apt install ffmpeg
```

## How to use?
### import package with widget
```python
from soundlit import AudioWidget
```

### initialize component
```python
# Custom streamlit component for audio recording and uploading
widget = AudioWidget()  

# You can see params of AudioWidget belove:
# min_duration: minimum duration of audio file (By default: 0 seconds)
# max_duration: maximum duration of audio file (By default: 60_000 seconds)
# available_formats: audio files with which formats available for uploading
# convert_to: what format to convert an audio file into if it needs to be converted (By default .wav)
# execlude_convert: audio files with which formats do not require conversion to a supported format
# sample_rate: sampling rate to which the audio file will be resampled
# mono: convert waveform to mono format with one channel if True else load 2 channels
```

### use only recorder 
```python
audio = widget.record_audio()
```

### or only uploader for all audio formats
```python
audio = widget.load_audio()
```

### and finally you can use the whole widget
```python
audio = widget.get_audio()
```

## How change recoder style?
### 1. Install [node](https://nodejs.org/en/download) >= 16
### 2. Go to the cloned project directory, then to the audio_widgets package, and finally to the fronted folder.
```shell
cd ./audio_widgets/frontend
```
### 3. Install all fronted dependencies 
```npm
npm i
```
### 4. Set Node options for legacy support 
#### on Unix-like (Linux, macOS, Git bash, etc.)
```shell
export NODE_OPTIONS=--openssl-legacy-provider
```

#### on Windows command prompt
```shell
set NODE_OPTIONS=--openssl-legacy-provider
```

#### on PowerShell
```shell
$env:NODE_OPTIONS = "--openssl-legacy-provider"
```

### 5. Change component style
#### go to the file at the path below in any text editor
```shell
cd ./audio_widgets/frontend/src/StreamlitAudioRecorder.tsx
```
#### and change the styles that start from line 59
```html
<AudioReactRecorder
state={recordState}
onStop={this.onStop_audio}
type='audio/wav'
backgroundColor='#000000'
foregroundColor='#6633CC'
canvasWidth={450}
canvasHeight={100}
/>
```

### 6. Remove current frontend build
```shell
rm -rf ./audio_widgets/frontend/build
```

### 7. Build new fronted comnponent
```shell
npm run build
```

### 8. Remove all dependencies unless you no longer need to change the style
#### on Unix-like (Linux, macOS)
```shell 
rm -rf node_modules
``` 
#### on Windows
```shell
npm i -g rm
rm -rf node_modules
```
