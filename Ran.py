from tkinter import *
from PIL import Image
import random

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

terminal = Text(
    root,
    bg="black",
    fg="#00ff66",
    insertbackground="#00ff66",
    font=("Courier", 12),
    borderwidth=0,
    highlightthickness=0,
    padx=10,
    pady=10
)
terminal.pack(fill=BOTH, expand=True)

def fake_hex():
    return "".join(random.choice("0123456789ABCDEF") for _ in range(32))

def terminal_write(line=""):
    terminal.insert(END, line + "\n")
    terminal.see(END)

def start_main_ui():
    terminal.destroy()

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

    top_text = Label(main, text="LARP//LARP", fg="#00ff66", bg="black", font=("Courier", 16, "bold"))
    top_text.pack(pady=12)

    ascii_label = Label(main, text=ascii_art, fg="#00ff66", bg="black", font=("Courier", 6), justify=LEFT)
    ascii_label.pack(pady=5)

    status = Label(main, text="", fg="#00ff66", bg="black", font=("Courier", 13))
    status.pack(pady=5)

    warning = Label(main, text="", fg="red", bg="black", font=("Impact", 34, "bold"))
    warning.pack(pady=10)

    sub1 = Label(main, text="", fg="white", bg="black", font=("Courier", 18, "bold"))
    sub1.pack(pady=5)

    sub2 = Label(main, text="", fg="#00ff66", bg="black", font=("Courier", 15))
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

    bottom = Label(root, text="[F0LL0W PLZ]", fg="#333333", bg="black", font=("Courier", 10))
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

    state = {"warning": "", "warning_i": 0, "log_i": 0}

    def add_log(text):
        log_box.config(state=NORMAL)
        log_box.insert(END, text + "\n")
        log_box.see(END)
        log_box.config(state=DISABLED)

    def animate_logs():
        if state["log_i"] < len(boot_logs):
            add_log(boot_logs[state["log_i"]])
            state["log_i"] += 1
            root.after(random.randint(250, 650), animate_logs)
        else:
            root.after(400, type_warning)

    def type_warning():
        if state["warning_i"] < len(final1):
            state["warning"] += final1[state["warning_i"]]
            warning.config(text=state["warning"])
            state["warning_i"] += 1
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
        ascii_label.config(fg=random.choice(["#00ff66", "#00cc55", "#66ff99", "#009944"]))
        warning.config(fg=random.choice(["red", "#ff3333", "#990000", "white"]) if random.randint(1, 8) == 1 else "red")
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
    animate_logs()
    root.after(7000, random_log_spam)

def loading_sequence(i=0):
    lines = [
        "[BOOT] Booting Pi Pico 2....",
        "[OK] Execute done...",
        "[OK] Larping mr robot...",
        "[LARP] Enjoying the larp...",
        "[WARN] Follow me on tiktok",
        "[OK] Injecting dramatic nonsense...",
        "[WARN] Leave a like...",
        "[DONE] Larp loaded."
    ]

    if i < 45:
        line = random.choice(lines)

        if random.randint(1, 3) == 1:
            line += " :: " + fake_hex()

        terminal_write(line)
        root.after(random.randint(35, 80), lambda: loading_sequence(i + 1))
    else:
        root.after(300, start_main_ui)

loading_sequence()
root.mainloop()