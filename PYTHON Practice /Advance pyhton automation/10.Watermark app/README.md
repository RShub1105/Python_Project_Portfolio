
# 🖋️ Watermark App
A simple and intuitive Python application for adding text watermarks to your images. Built with Tkinter and Pillow, this GUI-based tool lets you upload an image, insert a watermark, and save the new watermarked image with ease.



## Features

🖼️ Upload any image (JPEG, PNG, etc.)

✍️ Add custom watermark text

💾 Save the watermarked image

🧰 Easy-to-use graphical interface




## 📦 Requirements

-  Python 3.7+
- Dependencies (install with pip):

bash
-     pip install pillow

 tkinter usually comes pre-installed with Python. If not, install it using your system's package manager.
## 🚀 Getting Started

1. Clone the repository or download the script.



-     git clone https://github.com/yourusername/watermark-app.git cd watermark-app Run the application:

bash

-     python watermark_app.py

3. Use the GUI to:

-   Click Upload Image to select an image file.

-   Enter your watermark text.

-   Click Add Watermark to apply it.

-   Click Save Image to store the result.


## 🛠️ How It Works

The script uses:

-     Tkinter for the GUI

-     Pillow (PIL) for image manipulation

Watermarks are applied by overlaying semi-transparent text on the bottom right of the uploaded image, resized dynamically.
## 📁 Project Structure

-     watermark_app.py
-     README.md
## License

This project is licenses under [MIT](https://choosealicense.com/licenses/mit/).

