import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageDraw,ImageFont
def add_watermark():
    image_path = filedialog.askopenfilename()
    if not image_path:
        return
    
    text = watermark_entry.get()
    image = Image.open(image_path).convert('RGBA')

    watermark = Image.new('RGBA',image.size,(255,255,255,0))
    draw = ImageDraw.Draw(watermark)

    width, heigth = image.size
    font_size = int(min(width,heigth)/15)
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)

    draw.text((width - font_size* len(text),heigth-font_size),text,fill=(255,255,255,128),font=font)

    watermarked = Image.alpha_composite(image,watermark)
    output_path = "watermarked_image.png"
    watermarked.save(output_path)
    status_label.config(text=f"Saved as {output_path}")

root = tk.Tk()
root.title("image Watermark App")
root.geometry("400x200")

tk.Label(root,text="Watermark Text:",font=("Arial",12)).pack(pady10)
watermark_entry = tk.Entry(root,font=("Arial",12),width=20)
watermark_entry.pack()

tk.Button(root,text="Choose image & Add watermark",font=('Arial',12),command=add_watermark).pack(pady=20)
status_label = tk.Label(root,text="",font=("Arial",10))
status_label.pack()

root.mainloop()
    