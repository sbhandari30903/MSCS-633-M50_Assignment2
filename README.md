# MSCS-633-M50_Assignment2
# QR Code Generator

A simple Python application that generates QR codes for URLs or any text input. The generated QR codes are saved as PNG image files with customizable settings.

## Author
**Shimon Bhandari**  
Date: 2025-09-21

## Description

This script generates QR codes using the `qrcode` library with the following features:
- High error correction for better reliability
- Customizable QR code size and appearance
- Interactive command-line interface
- PNG output format
- Configurable file naming

## Features

- **High Error Correction**: Uses ERROR_CORRECT_H for maximum reliability
- **Customizable Size**: Adjustable box size and border width
- **Interactive Input**: Prompts user for URL/text input
- **PNG Output**: Saves QR codes as high-quality PNG images
- **Flexible Naming**: Customizable output filename

## Requirements

- Python 3.6+
- qrcode library
- Pillow (PIL) library (dependency of qrcode)

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install qrcode[pil]
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Run the script directly:

```bash
python qr_generator.py
```

The script will prompt you to enter a URL or text, then generate and save the QR code.

### Programmatic Usage

You can also import and use the function in your own Python scripts:

```python
from qr_generator import generate_qr_code

# Generate QR code with default filename
generate_qr_code("https://www.example.com")

# Generate QR code with custom filename
generate_qr_code("https://www.example.com", "my_qr_code.png")
```

## Configuration

The QR code generator uses the following default settings:

- **Version**: 1 (auto-adjusts for longer data)
- **Error Correction**: High (ERROR_CORRECT_H)
- **Box Size**: 10 pixels
- **Border**: 4 boxes
- **Fill Color**: Black
- **Background Color**: White

## Function Reference

### `generate_qr_code(url: str, file_name: str = "qrcode.png") -> None`

Generates a QR code for the given URL or text and saves it as an image file.

**Parameters:**
- `url` (str): The URL or text to encode in the QR code
- `file_name` (str): The name of the output QR code image file (default: "qrcode.png")

**Returns:**
- None

**Example:**
```python
generate_qr_code("https://github.com", "github_qr.png")
```

## Output

The application generates a PNG image file containing the QR code. The default filename is `qrcode.png`, but you can specify a custom name when using the function programmatically.

## Error Handling

The application includes basic error handling for:
- Invalid input validation
- File writing permissions
- QR code generation errors

## Dependencies

- `qrcode`: QR code generation library
- `Pillow`: Python Imaging Library (PIL) for image processing