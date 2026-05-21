from tkinter import *
from PIL import Image

ASCII_CHARS = " .:-=+*#%@"

def resize_image(image, new_width=70):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    ascii_str = ""

    for pixel in image.getdata():
        index = pixel * (len(ASCII_CHARS) - 1) // 255
        ascii_str += ASCII_CHARS[index]

    return ascii_str

def image_to_ascii(path):
    image = Image.open(path)
    image = resize_image(image)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    width = image.width

    ascii_image = ""
    for i in range(0, len(ascii_str), width):
        ascii_image += ascii_str[i:i + width] + "\n"

    return ascii_image

IMAGE_PATH = "face.png"

ascii_art = image_to_ascii(IMAGE_PATH)

root = Tk()
root.title("")
root.configure(bg="black")
root.attributes("-fullscreen",True)

ascii_label = Label(
    root,
    text=ascii_art,
    fg="white",
    bg="black",
    font=("Courier", 6),
    justify=LEFT
)
ascii_label.pack(pady=20)

label1 = Label(root, text="", fg="red", bg="black", font=("Impact", 28, "bold"))
label1.pack(pady=10)

label2 = Label(root, text="", fg="white", bg="black", font=("Courier", 18))
label2.pack(pady=5)

label3 = Label(root, text="", fg="cyan", bg="black", font=("Courier", 16))
label3.pack(pady=5)

text1 = "This system has been seized!!!"
text2 = "By Hexiik"
text3 = ""

current_text = ""
text_index = 0

def animate():
    global current_text, text_index

    if text_index < len(text1):
        current_text += text1[text_index]
        label1.config(text=current_text)
        text_index += 1
        root.after(50, animate)
    else:
        label2.config(text=text2)
        label3.config(text=text3)

animate()
root.mainloop()