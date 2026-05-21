from tkinter import *
from PIL import Image
import random
import time

ASCII_CHARS = " .:-=+*#%@"

IMAGE_PATH = "face.png"

def resize_image(image, new_width=85):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.45)
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

ascii_art = image_to_ascii(IMAGE_PATH)

root = Tk()
root.title("")
root.configure(bg="black")
root.attributes("-fullscreen", True)

root.bind("<Escape>", lambda e: root.destroy())

main = Frame(root, bg="black")
main.pack(expand=True, fill=BOTH)

top_text = Label(
    main,
    text="LARP//LARP",
    fg="#00ff66",
    bg="black",
    font=("Courier", 16, "bold")
)
top_text.pack(pady=12)

ascii_label = Label(
    main,
    text=ascii_art,
    fg="#00ff66",
    bg="black",
    font=("Courier", 6),
    justify=LEFT
)
ascii_label.pack(pady=5)

status = Label(
    main,
    text="",
    fg="#00ff66",
    bg="black",
    font=("Courier", 13)
)
status.pack(pady=5)

warning = Label(
    main,
    text="",
    fg="red",
    bg="black",
    font=("Impact", 34, "bold")
)
warning.pack(pady=10)

sub1 = Label(
    main,
    text="",
    fg="white",
    bg="black",
    font=("Courier", 18, "bold")
)
sub1.pack(pady=5)

sub2 = Label(
    main,
    text="",
    fg="#00ff66",
    bg="black",
    font=("Courier", 15)
)
sub2.pack(pady=5)

log_box = Text(
    main,
    bg="black",
    fg="#00ff66",
    insertbackground="#00ff66",
    font=("Courier", 11),
    height=10,
    width=90,
    borderwidth=0,
    highlightthickness=0
)
log_box.pack(pady=15)
log_box.config(state=DISABLED)

bottom = Label(
    main,
    text="[F0LL0W PLZ]",
    fg="#333333",
    bg="black",
    font=("Courier", 10)
)
bottom.pack(side=BOTTOM, pady=10)

boot_logs = [
    "[BOOT] Booting Pi Pico 2....",
    "[OK] Execute done...",
    "[OK] Larping mr robot...",
    "[LARP] Enjoying the larp...",
    "[WARN] Follow me on tiktok",
    "[OK] Injecting dramatic nonsense...",
    "[WARN] Leave a like...",
    "[DONE] Larp loaded."
]

final1 = "THIS SYSTEM HAS BEEN LARPED"
final2 = "//HEXIIK//"
final3 = "Enjoy the larp."

current_warning = ""
warning_index = 0
log_index = 0

def add_log(text):
    log_box.config(state=NORMAL)
    log_box.insert(END, text + "\n")
    log_box.see(END)
    log_box.config(state=DISABLED)

def fake_hex():
    return "".join(random.choice("0123456789ABCDEF") for _ in range(32))

def animate_logs():
    global log_index

    if log_index < len(boot_logs):
        add_log(boot_logs[log_index])
        log_index += 1
        root.after(random.randint(250, 650), animate_logs)
    else:
        root.after(400, type_warning)

def type_warning():
    global current_warning, warning_index

    if warning_index < len(final1):
        current_warning += final1[warning_index]
        warning.config(text=current_warning)
        warning_index += 1
        root.after(65, type_warning)
    else:
        root.after(300, show_subtitles)

def show_subtitles():
    sub1.config(text=final2)
    root.after(500, lambda: sub2.config(text=final3))
    root.after(700, matrix_noise)

def matrix_noise():
    status.config(text="SIGNATURE: " + fake_hex())
    root.after(120, matrix_noise)

def flicker():
    colors = ["#00ff66", "#00cc55", "#66ff99", "#009944"]
    ascii_label.config(fg=random.choice(colors))

    if random.randint(1, 8) == 1:
        warning.config(fg=random.choice(["red", "#ff3333", "#990000", "white"]))
    else:
        warning.config(fg="red")

    root.after(random.randint(80, 180), flicker)

def random_log_spam():
    lines = [
        "[TRACE] " + fake_hex(),
        "[PING] Localhost is larping.",
        "[SYS] Follow pls",
        "[LOCK] Locked in",
        "[NULL] No larp found",
        "[DATA] " + fake_hex()
    ]

    add_log(random.choice(lines))
    root.after(random.randint(900, 1600), random_log_spam)

animate_logs()
flicker()
random_log_spam()

root.mainloop()