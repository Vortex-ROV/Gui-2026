"""TTS announcements using Windows SAPI via win32com.
Each call is fire-and-forget in a daemon thread so it never blocks the GUI."""

import threading
import win32com.client


class VoiceAnnouncer:

    def welcome(self):
        self._speak("Welcome to Titan ROV control system. All systems are initializing.")

    def say_gain(self, gain: int):
        self._speak(f"Gain set to {gain} percent.")

    def say(self, text: str):
        self._speak(text)

    def _speak(self, text: str):
        threading.Thread(target=self._worker, args=(text,), daemon=True).start()

    def _worker(self, text: str):
        # SpVoice must be created on the thread that uses it (COM requirement)
        try:
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(text)
        except Exception as e:
            print(f"[VoiceAnnouncer] TTS error: {e}")