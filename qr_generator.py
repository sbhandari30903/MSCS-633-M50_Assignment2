"""
QR Code Generator Application
Author: Shimon Bhandari
Date: 2025-09-21
Description:
    This script generates a QR code for a given URL.
    The generated QR code is saved as an image file.
"""

import qrcode

def generate_qr_code(url: str, file_name: str = "qrcode.png") -> None:
    """
    Generates a QR code for the given URL and saves it as an image file.

    Args:
        url (str): The URL or text to encode in the QR code.
        file_name (str): The name of the output QR code image file.
    """

    # Create a QR code instance with configuration
    qr = qrcode.QRCode(
        version=1,  # QR code size (1 = smallest, auto-adjust for longer data)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Pixel size of each box in QR code
        border=4,  # Border size around the QR code
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as a PNG file
    img.save(file_name)

    print(f"QR Code successfully generated and saved as {file_name}")


if __name__ == "__main__":
    # Example usage
    input_url = input("Enter a URL to generate QR Code: ").strip()
    generate_qr_code(input_url)

