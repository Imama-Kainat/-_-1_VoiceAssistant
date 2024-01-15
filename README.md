# -_-1_VoiceAssistant
voice assistant part of python internship oasis infobyte

This is a Python program that acts as a voice-controlled assistant using the `pyttsx3` library for text-to-speech, `speech_recognition` library for speech recognition, and other modules for various tasks.

Here's a breakdown of the code:

1. **Importing Libraries:**
   - `pyttsx3`: For text-to-speech conversion.
   - `speech_recognition`: For recognizing speech.
   - `datetime`: For working with date and time.
   - `wikipedia`: For fetching information from Wikipedia.
   - `webbrowser`: For opening web pages.
   - `os`: For interacting with the operating system.
   - `smtplib`: For sending emails.
   - `pyaudio`: Required by the `speech_recognition` library.

2. **Initializing Text-to-Speech Engine:**
   - The `pyttsx3` engine is initialized with the default 'sapi5' backend.

3. **Greeting Function (`wishMe`):**
   - Greets the user based on the time of day.

4. **Speech Recognition Function (`takeCommand`):**
   - Captures audio input from the user using the microphone.
   - Uses Google's speech recognition to convert the audio into text.
   - Returns the recognized text.

5. **Sending Email Function (`sendEmail`):**
   - Sends an email using the Gmail SMTP server.

6. **Main Script (`__main__`):**
   - Greets the user at the beginning.

   - **Infinite Loop for Continuous Listening:**
     - Continuously listens for user commands using `takeCommand`.

   - **Logic for Executing Tasks:**
     - If the recognized command contains specific keywords (`'wikipedia'`, `'open youtube'`, etc.), it performs corresponding tasks.

   - **Tasks Include:**
     - Searching Wikipedia and speaking about a topic.
     - Opening YouTube, Google, or Stack Overflow in the default web browser.
     - Playing music from a specified directory.
     - Speaking the current time.
     - Opening Visual Studio Code.
     - Sending an email to a predefined recipient.

   - **Exception Handling:**
     - Handles exceptions, like when sending an email fails.

**Note:**
- Make sure you have the required libraries installed (`pip install pyttsx3 speechRecognition wikipedia`).
- Some functionalities, like sending emails, might require additional configurations (e.g., enabling less secure apps in your Gmail account for sending emails).

This code essentially allows you to interact with your computer using voice commands for various tasks.
