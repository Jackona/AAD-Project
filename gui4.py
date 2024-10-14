
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

class PersonNameDelivery (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame4")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        controller.geometry("360x800")
        controller.configure(bg = "#373361")


        canvas = Canvas(
            self,
            bg = "#373361",
            height = 800,
            width = 360,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            18.0,
            190.0,
            341.0,
            555.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            37.0,
            269.0,
            322.0,
            356.0,
            fill="#B485FD",
            outline="")

        canvas.create_text(
            98.0,
            296.0,
            anchor="nw",
            text="Enter delivery code",
            fill="#FFFFFF",
            font=("JacquesFrancois Regular", 20 * -1)
        )

        canvas.create_text(
            18.0,
            17.0,
            anchor="nw",
            text="Person name - Delivery",
            fill="#FFFFFF",
            font=("JacquesFrancois Regular", 20 * -1)
        )

        canvas.create_rectangle(
            62.0,
            332.0,
            294.0,
            333.0,
            fill="#000000",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=63.0,
            y=443.0,
            width=231.0,
            height=59.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=302.0,
            y=6.0,
            width=54.0,
            height=34.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=0.0,
            y=747.0,
            width=360.0,
            height=53.0
        )
        controller.resizable(False, False)
    def updateUsername(self):
        self.MenuCanvas.itemconfig(self.username_display, text = self.controller.username)
