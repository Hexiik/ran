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

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

canvas = Canvas(root, bg="black", highlightthickness=0)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

matrix_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&@"
font_size = 16
columns = screen_w // font_size
drops = [random.randint(-screen_h, 0) for _ in range(columns)]

def matrix_rain():
    canvas.delete("rain")

    for i in range(columns):
        x = i * font_size
        y = drops[i]

        char = random.choice(matrix_chars)

        canvas.create_text(
            x,
            y,
            text=char,
            fill="#003f1f",
            font=("Courier", font_size, "bold"),
            tags="rain"
        )

        drops[i] += font_size

        if drops[i] > screen_h and random.random() > 0.96:
            drops[i] = random.randint(-300, 0)

    root.after(45, matrix_rain)

main = Frame(root, bg="black")
main.place(relx=0.5, rely=0.5, anchor=CENTER)

top_text = Label(
    main,
    text="",
    fg="#00ff66",
    bg="black",
    font=("Courier", 16, "bold")
)
top_text.pack(pady=12)

ascii_label = Label(
    main,
    text="",
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
    height=12,
    width=95,
    borderwidth=0,
    highlightthickness=1,
    highlightbackground="#00ff66"
)
log_box.pack(pady=15)
log_box.config(state=DISABLED)

bottom = Label(
    root,
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

final1 = "LARP DETECTED"
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

def clear_log():
    log_box.config(state=NORMAL)
    log_box.delete("1.0", END)
    log_box.config(state=DISABLED)

def fake_hex():
    return "".join(random.choice("0123456789ABCDEF") for _ in range(32))

def terminal_loading():
    loading_lines = [
        "Booting kernel...",
        "Loading modules...",
        "Starting services...",
        "Mounting filesystem...",
        "Authenticating session...",
        "Checking memory...",
        "Opening terminal...",
        "Initializing renderer...",
        "Loading matrix engine...",
        "Connecting localhost..."
    ]

    def spam(i=0):
        if i < 60:
            style = random.randint(1, 5)

            if style == 1:
                line = "[ OK ] " + random.choice(loading_lines)

            elif style == 2:
                line = "[HEX] " + fake_hex()

            elif style == 3:
                line = "root@system:~# " + random.choice([
                    "chmod",
                    "inject",
                    "trace",
                    "mount",
                    "boot"
                ])

            elif style == 4:
                line = "[SYS] addr=0x" + fake_hex(8)

            else:
                line = "[NET] packet id=" + str(random.randint(1000, 9999))

            add_log(line)

            dots = "." * ((i % 3) + 1)
            status.config(text="LOADING TERMINAL" + dots)

            root.after(random.randint(35, 70), lambda: spam(i + 1))

        else:
            clear_log()

            top_text.config(text="LARP//LARP")
            ascii_label.config(text=ascii_art)

            root.after(200, animate_logs)

    spam()

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

matrix_rain()
flicker()
terminal_loading()

root.after(7000, random_log_spam)

root.mainloop()