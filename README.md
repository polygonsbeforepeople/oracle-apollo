# Apollo.exe

*The Oracle Awaits.*

A tiny, offline fortune-cookie app for Windows, powered by Python, pixel art, and the questionable generosity of an ancient Greek god.

Apollo delivers randomly selected commentary ranging from divine arrogance and academic warfare to ominous prophecies, pure nonsense, and the occasional moment of suspiciously genuine kindness.

Crack the cookie. Receive your wisdom. Question your life choices.

## Features

- **Random commentary** — Apollo draws from a catalogue of original lines.
- **Weighted categories** — divine shade, ominous prophecies, Olympian arrogance, academic warfare, rare kindness, and pure nonsense each have different chances of appearing.
- **Animated pixel-art cookie** — because divine revelations deserve presentation.
- **Standalone Windows executable** — launch `Apollo.exe` without manually running Python.
- **Offline operation** — no internet connection or API key required.

## Built With

- Python
- Tkinter
- PyInstaller
- Pixel art and an unreasonable amount of divine ego

## Running Apollo

### Option 1: Windows executable

Run `Apollo.exe` to open the app.

No separate Python installation is needed to run the packaged executable.

### Option 2: Run from source

You will need Python installed on Windows.

1. Clone the repository:

   ```powershell
   git clone https://github.com/polygonsbeforepeople/oracle-apollo.git
   cd oracle-apollo
   ```

2. Launch the application:

   ```powershell
   python main.py
   ```

## Building the Executable

Install PyInstaller:

```powershell
python -m pip install pyinstaller
```

Build Apollo:

```powershell
python -m PyInstaller --clean --noconfirm --onefile --windowed --icon="assets/apollo.ico" --name Apollo main.py
```

The executable will be generated at:

```text
dist/Apollo.exe
```

## Project Structure

```text
oracle-apollo/
├── assets/
│   └── apollo.ico
├── main.py
├── commentary.py
├── .gitignore
└── README.md
```

- `main.py` — application window, cookie animation, and commentary display.
- `commentary.py` — commentary catalogue and weighted random selection.
- `assets/apollo.ico` — application icon.

## The Oracle's Policy

Apollo does not predict the future. He makes remarks about it with the confidence of someone who has never been wrong in his own mind.

His wisdom is random, his ego is immeasurable, and his kindness is rare enough to be suspicious.

## Status

**Version 1 — functional and gloriously opinionated.**

This is a small personal project built to experiment with Python, Tkinter, random selection, desktop application packaging, and giving a program a distinct personality.

---

*The gods have spoken. Whether you listen is your problem.*