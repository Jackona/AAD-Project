
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
from reportlab.pdfgen import canvas as canvas2
import datetime
import os
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller #self.
        self.MenuCanvas = ""

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame8")


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

        self.button_image_1 = PhotoImage(file=r"assets\frame8\button_1.png")
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

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [print("items running out button clicked"), controller.show_current_frame(ListItemsReachingExpiry)],
            relief="flat"
        )
        button_2.place(
            x=185.0,
            y=537.0,
            width=144.0,
            height=191.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_current_frame(RemoveItem),
            relief="flat"
        )
        button_3.place(
            x=185.0,
            y=89.0,
            width=140.0,
            height=191.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_current_frame(ItemsDeliveredOrRecorded),
            relief="flat"
        )
        button_4.place(
            x=30.0,
            y=319.0,
            width=140.0,
            height=191.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            canvas,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_current_frame(ListItemsRunningOut),
            relief="flat"
        )
        button_5.place(
            x=185.0,
            y=319.0,
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

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            canvas,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [print("health button clicked"), init_pdf_gen()],
            relief="flat"
        )
        button_8.place(
            x=30.0,
            y=537.0,
            width=140.0,
            height=191.0
        )
        controller.resizable(False, False)

        def generate_pdf(file_name):
            # if the file exists it will be deleted
            if os.path.exists(file_name):
                os.remove(file_name)
            # Create a canvas object
            pdf_file = canvas2.Canvas(file_name)
            # Write "Hello" to the PDF file
            now = datetime.datetime.now()
            date_str = now.strftime("%Y-%m-%d %H:%M:%S")
            # Create a canvas object
            pdf_file = canvas2.Canvas(file_name)
            # title
            pdf_file.drawString(250, 720, "Health and Safety Report")
            # Write the current date to the PDF file
            pdf_file.drawString(72, 680, "Date: " + date_str)
            # ------------------------------------make current user variable which will get the current user------------------------------------------
            # ------------------------------------current user will go here
            pdf_file.drawString(72, 660, "Inspector Name: " + controller.username)
            # write the observations
            pdf_file.drawString(72, 640, "Observations: " + "Ok")

            # ------------------------------------current user will go here
            pdf_file.drawString(450, 500, "Signed: " + controller.username)
            # Save the file
            pdf_file.save()
            # open the pdf
            os.startfile(file_name)
        def init_pdf_gen():
            # get the current date-time
            now = datetime.datetime.now()
            # get only the date
            current_date_str = now.strftime("%Y-%m-%d")
            # Prepare the filename
            filename = current_date_str + "#HS.pdf"
            # Generate the PDF file
            generate_pdf(filename)

    def updateUsername(self):
        self.MenuCanvas.itemconfig(self.username_display, text = self.controller.username)




