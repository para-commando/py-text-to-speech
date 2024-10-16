# Py-Text-to-Speech Project

This project is a basic command-line text-to-speech application built in Python using `espeak` for speech synthesis. Users can type text, and the program will read it out loud using the `espeak` TTS engine. Voice properties like speed, pitch, and volume are customizable.

## Features
- Converts user input to speech using the `espeak` TTS engine.
- Adjustable voice settings: language, speed, pitch, and volume.
- Simple and easy-to-use command-line interface.

## Requirements

- Ensure you have `espeak` installed on your system if you are on linux or if you are using mac then make sure `say` is accessible and if you're on windows then please find the equivalent
- installing poetry is optional as of the latest commit refer (https://python-poetry.org/docs/#installation)

## Usage
- Run the script, and type the text you want to convert to speech.
- Press `q` to quit the program.

## Running this project locally

clone this repo and execute the file named `speakUpForMe.py` and enter your inputs in the terminal to get audio output

### Customizable Options:
- **Voice**: You can change the `voice` variable (e.g., `en`, `en+f3` for a female voice).
- **Speed**: Adjust the speech speed by modifying the `speed` variable (default is 135).
- **Pitch**: Change the `pitch` variable to modify the pitch (default is 70).
- **Volume**: Adjust the `volume` variable to change the volume (default is 100).
