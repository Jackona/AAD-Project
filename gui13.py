
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkcalendar import DateEntry
import tkinter as tk
from DbConnectionClass import DatabaseConnection


class NewOrder(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame131415")

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
            19.0,
            166.0,
            342.0,
            531.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            38.0,
            245.0,
            323.0,
            332.0,
            fill="#B485FD",
            outline="")

        item_code = canvas.create_text(
            55.0,
            262.0,
            anchor="nw",
            text="Enter Item code",
            fill="#FFFFFF",
            font=("JacquesFrancois Regular", 20 * -1)
        )

        self.options = ""
        self.labels = ""

        #self.item_code = tk.Label(canvas).place(x=99.0, y=272.0)

        def combobox_field_change(*args):
            print("combo box update to ", self.selected_label.get())
            # item_code['text'] = str(combobox.get())
            self.item_no_id = self.selected_label.get().split(" ", 1)
            canvas.itemconfigure(item_code, text=self.item_no_id[1])

        self.selected_label = tk.StringVar()
        self.combobox = ttk.Combobox(canvas, values=self.labels, textvariable=self.selected_label)

        self.combobox.pack()
        self.combobox.place(x=110,y=284)

        self.selected_label.trace('w', combobox_field_change)


        canvas.create_text(
            15.0,
            9.0,
            anchor="nw",
            text="New Order ",
            fill="#FFFFFF",
            font=("JacquesFrancois Regular", 24 * -1)
        )

        canvas.create_rectangle(
            63.0,
            308.0,
            295.0,
            309.0,
            fill="#000000",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [print("insert button clicked"), insert_item_button_event()],
            relief="flat"
        )
        button_1.place(
            x=64.0,
            y=419.0,
            width=231.0,
            height=59.0
        )

        canvas.create_rectangle(
            136.0,
            355.0,
            214.0,
            400.0,
            fill="#F24B4B",
            outline="")

        from gui11 import HeadChefAdvancedMenu
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [controller.show_current_frame(HeadChefAdvancedMenu), print("back button (add item) clicked")],
            relief="flat"
        )
        button_2.place(
            x=125.0,
            y=574.0,
            width=111.0,
            height=45.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [new_order_button_event(), print("New Order button clicked")],
            relief="flat"
        )
        button_4.place(
            x=125.0,
            y=485.0,
            width=111.0,
            height=45.0
        )

        canvas.create_text(
            140.0,
            362.0,
            anchor="nw",
            text="Q",
            fill="#FFFFFF",
            font=("JacquesFrancois Regular", 20 * -1)
        )

        self.unit_quantity = Entry(canvas)
        canvas.create_window(
            192.0,
            372.0,
            width=50,
            window=self.unit_quantity)

        controller.resizable(False, False)

        def new_order_button_event():
            db_conn = DatabaseConnection()
            db_conn.connect()
            query = """INSERT INTO `ba4wmpjwd2fynuzr9vvq`.`orders`(`order_orderdate`) VALUES (now())"""
            users_exists_check = db_conn.execute_no_data(query)
            query_last_insert = """SELECT LAST_INSERT_ID()"""
            last_insert_id = db_conn.query_no_data(query_last_insert)
            print(f"Last insert id: {last_insert_id}")
            db_conn.close()
            controller.order_id = last_insert_id[0][0]



        def insert_item_button_event():

            #get controller order_id
            order_id = str( controller.order_id )
            #get item id
            item_id = str( int(self.item_no_id[0]) )
            #get unit quantity
            unit_quantity = str(self.unit_quantity.get() )
            #send sql insert to orders table
            db_conn = DatabaseConnection()
            db_conn.connect()
            query = """INSERT INTO `ba4wmpjwd2fynuzr9vvq`.`order_items`(`order_id`,`product_id`,`quantity`)VALUES(%s, %s, %s)"""
            query_data = (order_id, item_id, unit_quantity ) #"order_id","input","input"
            users_exists_check = db_conn.execute(query, query_data)
            db_conn.close()


    def update_fridge_items(self):
        db_conn = DatabaseConnection()
        db_conn.connect()
        query = ("SELECT * FROM product")
        query_data = ""
        self.product_details = db_conn.query(query, query_data)
        db_conn.close()

        self.options = [row[0] for row in self.product_details]
        self.labels = [row for row in self.product_details]
        print(f"lables to be put in combobox: {self.labels}")
        self.combobox['values'] = (self.labels)
