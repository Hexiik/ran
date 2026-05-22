from tkinter import *
import random
import time

root = Tk()
root.title("terminal")
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
    padx=12,
    pady=12
)
terminal.pack(fill=BOTH, expand=True)

terminal.config(state=NORMAL)
terminal.focus_set()

hexchars = "0123456789ABCDEF"

boot_lines = [
    "Booting kernel...",
    "Loading system modules...",
    "Checking memory...",
    "Initializing network stack...",
    "Starting background services...",
    "Mounting virtual filesystem...",
    "Connecting to localhost...",
    "Loading terminal interface...",
    "Reading configuration files...",
    "Starting matrix renderer...",
    "Authenticating session...",
    "Accessing secure shell...",
    "Syncing HEXIIK protocols...",
    "Terminal online."
]

commands = [
    "ls",
    "whoami",
    "pwd",
    "date",
    "clear",
    "help",
    "exit"
]

def fake_hex(length=32):
    return "".join(random.choice(hexchars) for _ in range(length))

def write(text):
    terminal.insert(END, text)
    terminal.see(END)

def write_line(text=""):
    write(text + "\n")

def prompt():
    write("root@hexiik:~$ ")

def loading_sequence(i=0):
    if i < 80:
        line_type = random.randint(1, 5)

        if line_type == 1:
            line = "[ OK ] " + random.choice(boot_lines)
        elif line_type == 2:
            line = "[HEX] " + fake_hex()
        elif line_type == 3:
            line = "[SYS] addr=0x" + fake_hex(8)
        elif line_type == 4:
            line = "[NET] packet id=" + str(random.randint(1000, 9999))
        else:
            line = "[EXEC] /usr/bin/" + random.choice([
                "matrix",
                "shell",
                "boot",
                "trace",
                "render"
            ])

        write_line(line)
        root.after(random.randint(25, 70), lambda: loading_sequence(i + 1))
    else:
        write_line()
        write_line("Welcome to HEXIIK Terminal")
        write_line("Type 'help' for commands.")
        write_line()
        prompt()

def run_command(cmd):
    cmd = cmd.strip()

    if cmd == "help":
        write_line("Commands: " + ", ".join(commands))

    elif cmd == "ls":
        write_line("face.png  logs.txt  system.cfg  payload.py")

    elif cmd == "whoami":
        write_line("hexiik")

    elif cmd == "pwd":
        write_line("/home/hexiik")

    elif cmd == "date":
        write_line(time.strftime("%Y-%m-%d %H:%M:%S"))

    elif cmd == "clear":
        terminal.delete("1.0", END)

    elif cmd == "exit":
        root.destroy()
        return

    elif cmd == "":
        pass

    else:
        write_line("command not found: " + cmd)

    prompt()

def on_enter(event):
    line = terminal.get("insert linestart", "insert lineend")
    if "$ " in line:
        cmd = line.split("$ ", 1)[1]
        write_line()
        run_command(cmd)
    return "break"

terminal.bind("<Return>", on_enter)

loading_sequence()
root.mainloop()