
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

import mysql


class ListItemsRunningOut(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame3")


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
        canvas.create_text(
            15.0,
            9.0,
            anchor="nw",
            text="List items running out ",
            fill="#FFFFFF",
            font=("JacquesFrancois Regular", 24 * -1)
        )

        from gui8 import MainMenu
        from gui10 import HeadChefNormalMenu

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_current_frame(HeadChefNormalMenu) if controller.account_type=="HeadChef" else controller.show_current_frame(MainMenu),
            relief="flat"
        )
        button_1.place(
            x=249.0,
            y=755.0,
            width=111.0,
            height=45.0
        )
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        sub_frame = tk.ttk.Frame(canvas)

        sub_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=sub_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", expand=True, fill="both")

        canvas.create_rectangle(
            0.0,
            80.0,
            360.0,
            207.0,
            fill="#F0FCE1",
            outline="")

        canvas.create_rectangle(
            21.0,
            104.0,
            118.0,
            189.0,
            fill="#D9D9D9",
            outline="")

        def load_data():
            # Retrieve and display data
            cnx = mysql.connector.connect(
                host="ba4wmpjwd2fynuzr9vvq-mysql.services.clever-cloud.com",
                user="u8xcfo4ko24ym54s",
                password="QP4QNTpnWNYLP0uJMahz",
                database="ba4wmpjwd2fynuzr9vvq"
            )
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM items_quantity_running_out")
            result = cursor.fetchall()

            # Insert the result into the treeview
            current_y = 50
            for row in result:
                canvas.create_rectangle(
                    0.0,
                    current_y,
                    360.0,
                    current_y + 127,
                    fill="#FFFFFF",
                    outline=""
                )
                canvas.create_rectangle(
                    21.0,
                    current_y + 28,
                    118.0,
                    current_y + 113,
                    fill="#FF98BD",
                    outline=""
                )

                canvas.create_text(
                    134.0,
                    current_y + 29,
                    anchor="nw",
                    text="Item:" + row[1],
                    fill="#000000",
                    font=("JacquesFrancois Regular", 20 * -1)
                )

                canvas.create_text(
                    134.0,
                    current_y + 59,
                    anchor="nw",
                    text="Quantity: " + row[7],
                    fill="#000000",
                    font=("JacquesFrancois Regular", 20 * -1)
                )

                canvas.create_text(
                    134.0,
                    current_y + 89,
                    anchor="nw",
                    text="Expiry: " + str(row[4]),
                    fill="#000000",
                    font=("JacquesFrancois Regular", 20 * -1)
                )
                current_y += 127

            cnx.close()
            # Call this function again after 4 seconds
            self.after(4000, load_data)

        # Call the load_data function for the first time
        load_data()

        canvas.configure(scrollregion=canvas.bbox("all"))

        controller.resizable(False, False)
