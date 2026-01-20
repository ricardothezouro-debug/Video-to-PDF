# Video to PDF Converter

This project converts video files into PDF documents by extracting frames at a specified rate.

## Files

- `main.py`: Command-line script to convert a hardcoded video to PDF.
- `gui.py`: Graphical user interface (GUI) using Tkinter for selecting video, setting frames per second, and generating PDF.

## Requirements

- Python 3.x
- opencv-python
- pillow

Install dependencies:
```
pip install opencv-python pillow
```

## Usage

### Command-line (main.py)
Run `python main.py` to convert the video in `Video/Joelma.mp4` to `PDF/output.pdf` at 2 frames per second.

### GUI (gui.py)
Run `python gui.py` to open the GUI, select a video file, set FPS, and generate PDF. The PDF folder will open automatically after generation.

## Notes
- The GUI supports MP4, AVI, MOV, MKV files.
- Adjust FPS to control the number of frames extracted.