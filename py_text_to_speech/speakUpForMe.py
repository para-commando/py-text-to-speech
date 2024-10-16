import os
# Basic configuration
voice = "en"  # Set to en+f3 or other values to change the voice
speed = 135  # can be changed
pitch = 70  # can be changed
volume = 100  # can be changed

print("py-text-to-speech project version 1")
print("press q to quit")
os.system(f"espeak -v {voice} -s {speed} -p {pitch} -a {volume} 'welcome to py-text-to-speech project version 1'")

while True:
    inputCommand = input("please enter what you want to speak: ")
    if inputCommand == "q":
        os.system(f"espeak -v {voice} -s {speed} -p {pitch} -a {volume} 'closing this program, bye'")
        break
    command = f"espeak -v {voice} -s {speed} -p {pitch} -a {volume} '{inputCommand}'"
    os.system(command)
