
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
from gui import LoginFrame
from gui1 import RemoveItem
from gui2 import RemoveItemSelectItem
from gui3 import ListItemsRunningOut
from gui4 import PersonNameDelivery
from gui5 import ItemsDeliveredOrRecorded
from gui6 import AdminMenu
from gui7 import AddItem
from gui9 import ListItemsReachingExpiry

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

class DeliveryPersonMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller #self.
        self.MenuCanvas = ""

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame16")


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
        self.MenuCanvas = canvas

        canvas.place(x = 0, y = 0)

        self.button_image_1 = PhotoImage(file=r"assets\frame16\button_1.png")
        button_1 = Button(
            canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_current_frame(AddItem),
            relief="flat"
        )
        button_1.place(
            x=30.0,
            y=89.0,
            width=140.0,
            height=191.0
        )

        self.username_display = canvas.create_text(
            17.0,
            18.0,
            anchor="nw",
            text=f"{controller.username} - Chef",
            fill="#FFFFFF",
            font=("JacquesFrancois Regular", 20 * -1)
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            canvas,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [controller.show_current_frame(LoginFrame), controller.logout()],
            relief="flat"
        )
        button_6.place(
            x=3.0,
            y=755.0,
            width=366.0,
            height=53.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            canvas,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        button_7.place(
            x=302.0,
            y=8.0,
            width=54.0,
            height=34.0
        )

    def updateUsername(self):
        self.MenuCanvas.itemconfig(self.username_display, text = self.controller.username)

