import tkinter as tk
from tkinter import *
import time
import random
from os.path import dirname


# defining the class - the main application class
class EyeResterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EYE rester")

        self.countdown_seconds = 20

        # calling methods to load image, create GUI and center the app
        self.load_images()
        self.create_widgets()
        self.center_window()

        # initialize the timer
        self.update_timer()

    # Defining a method, to change background color of the GUI every time it runs 
    def color_generator(self):
        self.colors = [
            "#856ff8",
            "#46ACC0",
            "#9CD4FE",
            "#78bdf5",
            "#348a4d",
            "#217947",
            "#CE6190",
            "#991a20",
            "#E6B6BB",
            "#CEBC61",
            "#ffc02e",
            "#8D4545",
        ]
        self.bg_color = random.choice(self.colors)
        
    # method to then trace the location of the images
    def folder_path(self):
        return dirname(__file__)

    # finding the images and calling them
    def load_images(self):
        image_path = str(self.folder_path()) + "/images/option_2--.png"
        image_path = image_path.replace("\\", "/")

        self.image = PhotoImage(file=image_path)

    # Defining a method to create GUI widgets, but this time making them scalable!
    # the rest is just basic tkinter syntax
    def create_widgets(self):
        self.color_generator()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        screen_height = self.root.winfo_screenheight()
        font_size_welcome = int(screen_height * 0.013)

        self.image_label = tk.Label(self.root, image=self.image)
        self.image_label.pack(
            side=tk.LEFT,
            anchor=tk.NW,
            pady=int(screen_height * 0.035),
            padx=(int(screen_width * 0.038), int(screen_width * 0.01)),
        )
        self.image_label.configure(bg=self.bg_color)

        self.welcome_label = Label(
            self.root,
            text="It's time to give your eyes a rest!\n\nLook ~20 feet away",
            font=(
                "Sans Seriff",
                font_size_welcome,
            ),
            anchor=CENTER,
            pady=int(screen_height * 0.04),
        )
        self.welcome_label.configure(bg=self.bg_color)
        self.welcome_label.pack()

        self.timer_label = Label(
            self.root, text=f"Time left: {self.countdown_seconds} seconds", anchor=S
        )
        self.timer_label.configure(bg=self.bg_color)
        self.timer_label.pack()

    # definign a method to center the window on every screen
    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        app_width = int(screen_width * 0.3)
        app_height = int(screen_height * 0.17)

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        self.root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.root.configure(bg=self.bg_color)
    
    # method for a timer
    def update_timer(self):
        screen_height = self.root.winfo_screenheight()
        font_size_timer = int(screen_height * 0.17 / 18)

        if self.countdown_seconds > 0:
            self.countdown_seconds -= 1
            self.timer_label.config(
                text=f"Time left: {self.countdown_seconds} seconds",
                font=("Optima", font_size_timer),
            )
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")

# run
if __name__ == "__main__":
    root = tk.Tk()
    app = EyeResterApp(root)
    root.mainloop()
