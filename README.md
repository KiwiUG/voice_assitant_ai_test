# Voice Assistant AI (Python Prototype)

A lightweight Python voice assistant prototype with speech recognition, text-to-speech, and modular command handling.

---

##  Features
- Live **speech-to-text** (using libraries like `SpeechRecognition` or `whisper`)
- Text-to-speech responses via `pyttsx3` or similar
- **Modular structure** for adding tools or commands (e.g., open websites, play music)

---

##  Tech Stack
- **Python**  
- Speech recognition: `SpeechRecognition`, `openai-whisper`, or similar  
- TTS: `pyttsx3` or alternative  
- Other tools/libraries: Describe any additional dependencies

---

## ​ How to Run
```bash
git clone https://github.com/KiwiUG/voice_assitant_ai_test.git
cd voice_assitant_ai_test
python -m venv venv
source venv/bin/activate  # on Windows, use `venv\\Scripts\\activate`
pip install -r requirements.txt
python main.py
```
---


##  Next Enhancements
- Add command parsing (e.g., custom “skills” or control routines)
- Support for external APIs (e.g., weather, reminders)
- Implement logging of voice inputs/commands
- Package as a CLI or background service

---

##  License
MIT License © 2025 **Utsav Gautam**

Feel free to use, modify, or build upon this project with attribution.
