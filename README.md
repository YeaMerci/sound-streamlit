<div class="alert alert-block alert-info" style="font-size:20px; background-color: #fffff; font-family:verdana; color: #ec4949; border-radius: 10px; border: 0px #533078 solid">
    <h1>streamlit-audio-widgets</h1>
</div>

**Ask any questions. I will be very grateful if you rate the repository ⭐️**

****

<div class="alert alert-block alert-info" style="font-size:20px; background-color: #0b0e22; font-family:verdana; color: #423a7f; border-radius: 10px; border: 0px #533078 solid">
    Need upload and preprocess an audio file with a crazy extension? 🫣 
    <br>We support converting all formats to a single standard, since ffmpeg is under the hood!<br>
    Do you need to record audio rather than download? 
    <br>This widget has a built-in recorder.<br>
</div>

![Screenshot 2022-05-16 at 16 58 36](https://user-images.githubusercontent.com/82606558/168626886-de128ffa-a3fe-422f-a748-395c29fa42f9.png) <br/>

****

## Installation & setup
1. **Install widget from PyPI**
```shell
pip install streamlit-audio-widgets
```
2. **Make sure that you have the C++ ffmpeg library installed on your computer. 
<br>Its absence will lead to an [error](https://stackoverflow.com/questions/62470863/ffmpeg-command-not-found-but-pip-list-shows-ffmpeg).<br> 
If you are not sure that you have it, then run the command below (only for Unix)**
```shell
sudo apt install ffmpeg
```

****

## How to use?
### import package with widget
```python
from audio_widgets import AudioWidget
```

### initialize component
```python
widget = AudioWidget()   
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

****

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

### 6. Build fronted comnponent
```shell
npm run build
```

### 7. Remove all dependencies unless you no longer need to change the style
#### on Unix-like (Linux, macOS)
```shell 
rm -rf node_modules
``` 
#### on Windows
```shell
npm i -g rm
rm -rf node_modules
```
