# PDF Splitter

A simple, user-friendly desktop application that splits PDF files into multiple documents with customizable pages per document. Works on both macOS and Windows.

## Features

- 🖱️ Easy-to-use graphical interface
- 📄 Split PDF files into multiple documents
- 🔢 Customizable pages per document (1, 2, 5, 10, etc.)
- 📁 Customizable output directory
- 💻 Cross-platform (macOS and Windows)
- 📦 Can be built as a standalone executable
- 🎯 Smart file naming: `filename_part1.pdf`, `filename_part2.pdf`, etc.

## Project Structure

```
pdf-splitter/
├── pdf_splitter.py       # Main application code
├── build.py             # Build script for executables
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Installation

### Option 1: Run from Source

1. **Clone or download this repository**

2. **Install Python 3.9 or higher**
   - Download from [python.org](https://www.python.org/downloads/)
   - Or use Homebrew on macOS: `brew install python@3.14`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python pdf_splitter.py
   ```

### Option 2: Build Standalone Executable

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build the executable**
   ```bash
   python build.py
   ```

3. **Find your executable**
   - The executable will be in the `dist/` folder
   - **Windows**: `dist/PDF-Splitter.exe`
   - **macOS**: `dist/PDF-Splitter`

4. **Distribute**
   - Copy the executable from the `dist/` folder
   - Share it with others - no Python installation required!

## Usage

1. **Launch the application**
   - Run `python pdf_splitter.py` or double-click the executable

2. **Select a PDF file**
   - Click "Browse..." to choose your PDF file

3. **Choose output directory (optional)**
   - By default, pages are saved in a new folder next to the original PDF
   - Click "Change..." to select a different location

4. **Split the PDF**
   - Click "Split PDF" button
   - Progress bar shows the splitting progress
   - Output folder opens automatically when complete

## Output

- Each page is saved as a separate PDF file
- Files are named: `filename_part1.pdf`, `filename_part2.pdf`, etc.
- All pages are saved in a folder named: `[original_filename]_split`

## Requirements

- Python 3.8 or higher
- PyPDF2 (for PDF manipulation)
- PyInstaller (for building executables)
- tkinter (included with Python)

## Building for Different Platforms

### macOS
```bash
python build.py
```
Creates: `dist/PDF-Splitter` (macOS app)

### Windows
```bash
python build.py
```
Creates: `dist/PDF-Splitter.exe` (Windows executable)

**Note**: You must build the executable on the target platform. Build on Windows for Windows executable, and on macOS for macOS executable.

## Troubleshooting

### "No module named 'tkinter'" error
- **macOS**: tkinter comes with Python. If missing, reinstall Python from python.org
- **Linux**: Install with `sudo apt-get install python3-tk`
- **Windows**: tkinter is included with Python

### Permission denied on macOS
```bash
chmod +x dist/PDF-Splitter
```

### Antivirus blocking executable
- Some antivirus software may flag PyInstaller executables as suspicious
- This is a false positive - you can whitelist the application

## License

This project is free to use and modify for personal and commercial purposes.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Roadmap

Potential future enhancements:
- [ ] Custom icon for the application
- [ ] Split by page ranges (e.g., pages 1-5, 10-15)
- [ ] Merge multiple PDFs
- [ ] Password-protected PDF support
- [ ] Drag and drop file support
- [ ] Dark mode theme

---

Made with ❤️ using Python and PyPDF2

## Releases

- **Quick download (ZIP)**: [![Download PDF-Splitter v1.0.0](https://img.shields.io/badge/Download-v1.0.0-blue?logo=download)](https://github.com/javierdpt/pdf-splitter/raw/main/versions/PDF-Splitter-v1.0.0.zip)

- Direct ZIP link: [Download PDF-Splitter v1.0.0](https://github.com/javierdpt/pdf-splitter/raw/main/versions/PDF-Splitter-v1.0.0.zip)

Notes:
- The above link downloads the packaged macOS app (`.app`) inside a ZIP file.
- Alternatively, use the Releases page to view and download assets:
   https://github.com/javierdpt/pdf-splitter/releases

How to install on macOS:
1. Double-click the downloaded ZIP to extract `PDF-Splitter-v1.0.0.app`.
2. Move the `.app` into your `Applications` folder (or run from Finder).
3. If macOS blocks the app on first run, right-click the app and choose "Open" to bypass Gatekeeper.

