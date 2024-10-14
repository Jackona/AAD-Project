#import gui, gui1, gui2, gui3, gui4, gui5, gui6, gui7, gui8
from gui import LoginFrame
from gui1 import RemoveItem
from gui2 import RemoveItemSelectItem
from gui3 import ListItemsRunningOut
from gui4 import PersonNameDelivery
from gui5 import ItemsDeliveredOrRecorded
from gui6 import AdminMenu
from gui7 import AddItem
from gui8 import MainMenu
from gui9 import ListItemsReachingExpiry
from gui10 import HeadChefNormalMenu
from gui11 import HeadChefAdvancedMenu
from gui12 import HeadChefMenuChoice
from gui13 import NewOrder
from gui14 import NewProducts
from gui15 import NewSupplier
from gui16 import DeliveryPersonMenu

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.previous_frame_name = "Frame"
        self.current_frame_name = "LoginFrame"
        self.logged_in_state = False
        self.user_id = ""
        self.account_type = ""
        self.username = ""

        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Future Fridges Application")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.app_frames = {}

        for frame_class in (DeliveryPersonMenu, NewProducts, NewSupplier, RemoveItem, RemoveItemSelectItem, ListItemsRunningOut, ListItemsReachingExpiry, PersonNameDelivery, ItemsDeliveredOrRecorded, AdminMenu, AddItem, LoginFrame, HeadChefNormalMenu, MainMenu, HeadChefMenuChoice, HeadChefAdvancedMenu, NewOrder):
            frame = frame_class(container, self)
            self.app_frames[frame_class] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_current_frame(LoginFrame)
    def show_current_frame(self, cont):
        frame = self.app_frames[cont]
        print(f"Current frame: {cont}")
        self.current_frame_name = cont

        if cont == MainMenu:
            self.app_frames[MainMenu].updateUsername()

        if cont == AdminMenu:
            self.app_frames[AdminMenu].updateUsername()

        if cont == HeadChefNormalMenu:
            self.app_frames[HeadChefNormalMenu].updateUsername()

        if cont == AddItem:
            self.app_frames[AddItem].update_fridge_items()

        if cont == NewProducts:
            self.app_frames[NewProducts].update_fridge_items()

        if cont == NewOrder:
            self.app_frames[NewOrder].update_fridge_items()

        if cont == DeliveryPersonMenu:
            self.app_frames[DeliveryPersonMenu].updateUsername()

        if cont == RemoveItem:
            self.app_frames[RemoveItem].update_fridge_items()


        frame.tkraise()
        frame.lift()

    def logout(self):
        self.user_id = ""
        self.account_type = ""
        self.username = ""


if __name__ == "__main__":
    application = Application()
    application.mainloop()