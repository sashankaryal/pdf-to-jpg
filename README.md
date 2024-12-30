# PDF to JPG Converter

This script converts every page of a PDF file into JPEG images using the `pdf2image` library. The resulting images are saved in a folder named after the PDF file.

## Features
- Converts each page of a PDF into a separate JPEG image.
- Automatically creates an output folder named after the PDF file.
- Uses modern Python `pathlib` for clean and efficient path management.

## Requirements

- Python 3.6+
- The following Python libraries:
  - `pdf2image`
  - `Pillow` (installed as part of `pdf2image` dependencies)
- `poppler-utils` installed on your system for PDF rendering (required by `pdf2image`).

## Installation

1. Install Python 3.6 or newer.
2. Install the required Python libraries:
   ```bash
   pip install pdf2image
   ```
3. Install `poppler-utils`:
   - On Debian/Ubuntu:
     ```bash
     sudo apt install poppler-utils
     ```
   - On macOS (using Homebrew):
     ```bash
     brew install poppler
     ```
   - On Windows:
     Download and install the Poppler binaries from [Poppler for Windows](https://blog.alivate.com.au/poppler-windows/).

## Usage

Run the script from the command line:

```bash
python pdf_to_jpg.py <path_to_pdf>
```

### Example

If you have a PDF file named `example.pdf`, run the following command:

```bash
python pdf_to_jpg.py example.pdf
```

The script will create a folder named `example` in the same directory as the PDF and save each page as a JPEG image (e.g., `page_1.jpg`, `page_2.jpg`, etc.).

## Notes
- Ensure `poppler-utils` is installed and accessible in your system's PATH.
- Input file paths can be absolute or relative.
- The script does not overwrite existing images if the folder already exists.

## License

This script is provided under the MIT License. Feel free to use, modify, and distribute it as needed.

