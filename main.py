
import random
import tkinter as tk
from tkinter import font


# ---------- Apollo's personality ----------

FORTUNES = [
    (
        "THE PROPHECY",
        "A breakthrough approaches. It will occur immediately "
        "after you stop staring at the problem.",
    ),
    (
        "DIVINE SHADE",
        "I gave mortals the gift of reason. And yet, here you "
        "are, opening the same tab again.",
    ),
    (
        "THE BLESSING",
        "You need not conquer the entire day. Begin with the "
        "next hour. Even the sun rises one dawn at a time.",
    ),
    (
        "THE WARNING",
        "Beware the task you call 'a quick one.' I have seen "
        "how this story ends.",
    ),
    (
        "ANCIENT WISDOM",
        "You have gathered enough information to begin. "
        "Further procrastination will not become research "
        "merely because you rename it.",
    ),
    (
        "DIVINE OBSERVATION",
        "You have checked that same thing three times. "
        "The fourth inspection shall surely alter reality.",
    ),
    (
        "THE MYSTERY",
        "Someone may think of you today. Whether they reply "
        "to your message remains beyond my jurisdiction.",
    ),
    (
        "A RARE ACT OF KINDNESS",
        "Rest is not a reward you must earn by becoming "
        "extraordinary. Even a god knows when to pause.",
    ),
]


# ---------- Visual design ----------

BG = "#171717"
PANEL = "#211F1B"
GOLD = "#E7BD69"
BRIGHT_GOLD = "#FFE6A1"
TEXT = "#E9E1D2"
MUTED = "#9A907F"
COOKIE_DARK = "#80501F"
COOKIE_MID = "#D99A3D"
COOKIE_LIGHT = "#FFD778"


class ApolloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Apollo")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        # A compact desktop window.
        self.root.geometry("360x440")
        self.root.minsize(360, 440)

        self.current_fortune = None
        self.is_animating = False

        self.title_font = font.Font(
            family="Georgia", size=19, weight="bold"
        )
        self.body_font = font.Font(
            family="Georgia", size=11
        )
        self.small_font = font.Font(
            family="Segoe UI", size=9
        )

        self.build_interface()
        self.draw_cookie("closed")

    def build_interface(self):
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", pady=(18, 0))

        tk.Label(
            header,
            text="☼",
            font=("Georgia", 22),
            fg=GOLD,
            bg=BG,
        ).pack()

        tk.Label(
            header,
            text="APOLLO",
            font=self.title_font,
            fg=GOLD,
            bg=BG,
        ).pack()

        tk.Label(
            header,
            text="THE ORACLE AWAITS",
            font=self.small_font,
            fg=MUTED,
            bg=BG,
        ).pack(pady=(3, 0))

        self.canvas = tk.Canvas(
            self.root,
            width=240,
            height=150,
            bg=PANEL,
            highlightthickness=0,
            cursor="hand2",
        )
        self.canvas.pack(pady=(16, 10))
        self.canvas.bind("<Button-1>", self.on_cookie_click)

        self.instruction = tk.Label(
            self.root,
            text="Click the cookie. Receive your prophecy.",
            font=self.small_font,
            fg=TEXT,
            bg=BG,
        )
        self.instruction.pack(pady=(0, 8))

        self.message_title = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 9, "bold"),
            fg=GOLD,
            bg=BG,
            wraplength=310,
        )
        self.message_title.pack(pady=(2, 4))

        self.message = tk.Label(
            self.root,
            text="",
            font=self.body_font,
            fg=TEXT,
            bg=BG,
            wraplength=310,
            justify="center",
        )
        self.message.pack(padx=22, pady=(0, 8))

        self.footer = tk.Label(
            self.root,
            text="A GOD OF PROPHECY. A GOD OF PATIENCE.\n"
                 "YOUR PATIENCE IS NOT REQUIRED.",
            font=("Segoe UI", 7),
            fg=MUTED,
            bg=BG,
            justify="center",
        )
        self.footer.pack(side="bottom", pady=(4, 14))

    # ---------- Pixel-art cookie ----------

    def draw_pixel(self, x, y, color, size=10):
        self.canvas.create_rectangle(
            x, y, x + size, y + size,
            fill=color,
            outline=color,
        )

    def draw_cookie(self, state):
        self.canvas.delete("all")

        # Each letter is one pixel in the cookie sprite.
        # '.' means transparent.
        sprite = [
            "......DDDDD......",
            "....DDYYYYYDD....",
            "...DYYYYYYYYYD...",
            "..DYYYYYYYYYYYD..",
            ".DYYYYYYYYYYYYYD.",
            "DYYYYYYYYYYYYYYYD",
            "DYYYYYYYYYYYYYYYD",
            ".DYYYYYYYYYYYYYD.",
            "..DYYYYYYYYYYYD..",
            "...DDYYYYYYYDD...",
            ".....DDDDD.......",
        ]

        palette = {
            "D": COOKIE_DARK,
            "Y": COOKIE_MID,
        }

        pixel = 8
        start_x = 52
        start_y = 23

        # Cracking is shown as successive pixel-art frames.
        if state in ("crack1", "crack2"):
            sprite = [
                "......DDDDD......",
                "....DDYYYYYDD....",
                "...DYYYYYBYYYD...",
                "..DYYYYBYYYYYYD..",
                ".DYYYYYBYYYYYYYD.",
                "DYYYYYBYYYYYYYYYD",
                "DYYYYBYYYYYYYYYYD",
                ".DYYBYYYYYYYYYYD.",
                "..DBYYYYYYYYYYD..",
                "...DDYYYYYYYDD...",
                ".....DDDDD.......",
            ]
            palette["B"] = "#392719"

        if state == "open":
            sprite = [
                "....DDDD...DDDD....",
                "...DYYYYD.DYYYYD...",
                "..DYYYYYYDYYYYYYD..",
                ".DYYYYYYYYYYYYYYD.",
                "DYYYYYYYYYYYYYYYYYD",
                ".DYYYYYYYYYYYYYYD.",
                "..DYYYYYYYYYYYYD...",
                "...DDDD....DDDD....",
            ]
            start_x = 40
            start_y = 45

        for row, line in enumerate(sprite):
            for col, character in enumerate(line):
                if character != ".":
                    self.draw_pixel(
                        start_x + col * pixel,
                        start_y + row * pixel,
                        palette[character],
                        pixel,
                    )

        # Tiny chocolate chips / golden flecks.
        if state == "closed":
            for x, y in [
                (100, 62), (124, 78), (148, 54),
                (140, 94), (92, 86),
            ]:
                self.draw_pixel(x, y, COOKIE_LIGHT, 4)

        if state == "open":
            # The fortune slip appears between the halves.
            self.canvas.create_rectangle(
                104, 42, 136, 104,
                fill="#F1E6C9",
                outline=GOLD,
                width=2,
            )
            for y in (54, 66, 78, 90):
                self.canvas.create_line(
                    110, y, 130, y,
                    fill=COOKIE_DARK,
                    width=2,
                )

    # ---------- Interaction ----------

    def on_cookie_click(self, event=None):
        if self.is_animating:
            return

        self.is_animating = True
        self.current_fortune = random.choice(FORTUNES)

        self.message_title.config(text="")
        self.message.config(text="")
        self.instruction.config(text="The oracle is considering your fate...")

        self.draw_cookie("crack1")
        self.root.after(160, self.crack_second_frame)

    def crack_second_frame(self):
        self.draw_cookie("crack2")
        self.root.after(180, self.reveal_fortune)

    def reveal_fortune(self):
        self.draw_cookie("open")

        title, message = self.current_fortune
        self.message_title.config(text=title)
        self.message.config(text=f"“{message}”")
        self.instruction.config(
            text="Apollo has spoken. Try to keep up."
        )

        self.is_animating = False


if __name__ == "__main__":
    root = tk.Tk()
    app = ApolloApp(root)
    root.mainloop()
