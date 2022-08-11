import os
import shutil
import tkinter as tk
from pathlib import Path
from datetime import datetime
from tkinter import Label, filedialog, Button, Entry, messagebox

steam = Path(r"C:/Program Files (x86)/Steam/userdata")


class Gui:
    def __init__(self, master):
        self.master = master
        self.create_window()

    def create_window(self, location=steam):  # Bits inside the window

        global browse_bar_text
        browse_bar_text = tk.StringVar(value=location)

        browse_info = Label(text="""Find your Steam/userdata folder, this is Steam's install
              directory, not for Monster Hunter Rise""")
        browse_info.grid(row=0, columnspan=5)

        browse_bar = Entry(font=('arial', 9), text=browse_bar_text,
                           width=52, border=3)
        browse_bar.grid(row=1, column=0, columnspan=4, padx=2)

        browse_button = Button(text="Browse Files", width=10, height=1,
                               command=self.Select_Directory)
        browse_button.grid(row=1, column=4, padx=1)

        backup_button = Button(text="Backup Saves", width=10,
                               command=lambda: self.Backup_Run(location))
        backup_button.grid(row=2, columnspan=5, pady=5)

    def Select_Directory(self):
        # Lets the user select the directory that the code will search
        global browse_bar_text
        steam = Path(filedialog.askdirectory(initialdir=browse_bar_text))
        browse_bar_text = steam
        self.create_window(steam)

    def Backup_Run(self, location):
        # This will place the backed up save files into new folder named for
        # the current date in MM-DD-YYYY format.
        # If you wish to change the date format you can change the order at the
        # end of the line below, for 2 digit date use %y instead of %Y.
        date = datetime.now()
        target = Path() / date.strftime("%m-%d-%Y")

        if "userdata" in location.__str__():
            saves = [p for p in location.rglob("1446780/remote")]
            for save in saves:
                source = save
            if os.path.exists(target):
                duplicate_backup = messagebox.askquestion(
                    "Backup Already Exists",
                    """A backup has been created for todays date.
                    Would you like to overwrite the old backup
                    with the new one?""")
                if duplicate_backup == 'yes':
                    shutil.rmtree(target)
                    shutil.copytree(source, target)
                else:
                    pass
            else:
                shutil.copytree(source, target)
        else:
            messagebox.showerror(
                "Erorr", "Ensure you selected the correct folder.")


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("460x300")
    window.title("MH Rise Save Backup")
    window.wm_resizable(width=False, height=False)
    my_gui = Gui(window)
    window.mainloop()
