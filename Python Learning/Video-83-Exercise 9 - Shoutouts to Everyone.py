import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 150)

# Set the volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

# Text to speak
names=[]
while True:
    name = input("Enter a name (or type '0' to stop): ")

    if name == '0':
        break  # Exit the loop if the user enters '0'

    names.append(name)  # Add the name to the list

for name in names:
    # engine.say(f"Shoutout to {name}")
    engine.say(f"{name}")


# Run the speech engine
engine.runAndWait()


# using pywin32

import win32com.client

# Initialize the SAPI SpVoice object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Initialize an empty list to store names
names = []

# Input names until the user enters '0'
while True:
    name = input("Enter a name (or type '0' to stop): ")

    if name == '0':
        break  # Exit the loop if the user enters '0'

    names.append(name)  # Add the name to the list

# Loop through the names and use the TTS engine to speak each one
for name in names:
    speaker.Speak(f"Shoutout to {name}")

# the win32com.client module is part of the pywin32 package. pywin32 is a collection of modules that provide access to many of the
# Windows APIs from Python, and win32com.client is specifically used for working with COM (Component Object Model) objects, which are
# a part of the Windows operating system.