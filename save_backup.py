import os
import shutil
import tkinter as tk
from pathlib import Path
from datetime import datetime
from tkinter import Label, filedialog, Button, Entry, messagebox

steam = Path(r"C:/Program Files (x86)/Steam/userdata")
date = datetime.now()
if not os.path.isdir("Save Backups"):
    os.makedirs("Save Backups")

backup_folder = Path() / "Save Backups"
target = backup_folder / date.strftime("%m-%d-%Y")


class Gui:
    def __init__(self, master):
        self.master = master
        self.create_window()

    # Bits inside the window.
    def create_window(self, location=steam, saves_location=backup_folder):
        # Top Section of window, allows user to save files.
        global browse_bar_text
        browse_bar_text = tk.StringVar(value=location)

        browse_info = """\
        Find your Steam/userdata folder, this refers to Steam's install directory,
        not the install directory for Monster Hunter Rise."""

        Label(text=browse_info).grid(row=0, columnspan=5)

        browse_bar = Entry(font=('arial', 9), text=browse_bar_text,
                           width=52, border=3)
        browse_bar.grid(row=1, column=0, columnspan=4, padx=2)

        browse_button = Button(text="Browse Files", width=10, height=1,
                               command=self.Select_Directory)
        browse_button.grid(row=1, column=4, padx=1)

        backup_button = Button(text="Backup Saves", width=10,
                               command=lambda: self.Backup_Run(Path(browse_bar_text.get())))
        backup_button.grid(row=2, columnspan=5, pady=5)

        # Botom section of window, shows existing save files.
        Label(text="""\
            The below buttons will OVERWRITE your CURRENT steam saves for Rise,
            ensure you have backed up your current save before use.""").grid(
            row=3, columnspan=5)

        self.Button_Render(browse_bar_text, saves_location)

    def Button_Render(self, location, saves_location=backup_folder):
        saves = [f for f in os.listdir(saves_location)]
        saves.reverse()
        column = 0
        row = 4

        while True:
            if len(saves) < 10:
                saves.append("Not Found")
            else:
                break

        for x in range(0, 10):
            x = Button(text=saves[x], command=lambda x=x: self.Backup_Restore(saves[x], location)).grid(
                row=row, column=column, columnspan=2, pady=3)
            if column == 0:
                column += 3
            else:
                column -= 3
                row += 1

    def Select_Directory(self):
        # Lets the user select the directory that the code will search.
        global browse_bar_text
        steam = Path(filedialog.askdirectory(initialdir=browse_bar_text))
        browse_bar_text = steam
        self.create_window(steam)

    def Backup_Run(self, location):
        # This will place the backed up save files into new folder named for
        # the current date in MM-DD-YYYY format.
        # If you wish to change the date format you can change the order at the
        # end of the line below, for 2 digit date use %y instead of %Y.
        print(location)
        if "userdata" in location.__str__():
            saves = [p for p in location.rglob("1446780/remote")]
            for save in saves:
                source = save
            if os.path.exists(target):
                duplicate_backup = messagebox.askquestion(
                    "Backup Already Exists", """\
                    A backup has been created for todays date.
                    Would you like to overwrite the old backup
                    with the new one?""")
                if duplicate_backup == 'yes':
                    shutil.rmtree(target)
                    shutil.copytree(source, target)
                    messagebox.showinfo("Success!", "Backup Successful!")
                else:
                    pass
            else:
                shutil.copytree(source, target)
                messagebox.showinfo("Success!", "Backup Successful!")
        else:
            messagebox.showerror(
                "Error", "Ensure you selected the correct folder.")

        self.Button_Render(location)

    def Backup_Restore(self, folder, location):
        saves = [p for p in location.rglob("1446780/remote/win64_save")]
        for save in saves:
            place = save

        if folder == "Not Found":
            pass
        elif os.path.exists(Path(backup_folder / folder)):
            backup_target = Path(backup_folder / folder / 'win64_save')

            backup_confirm = messagebox.askquestion("Confirm Overwrite", """\
                This will overwrite your CURRENT save file
                with the backup you selected, ensure you
                have backed up your current save file as
                this CANNOT currently be undone.""")
            if backup_confirm == 'yes':
                shutil.copytree(backup_target, place, dirs_exist_ok=True)
                messagebox.showinfo(
                    "Success!", f"Save file Overwritten with selected Backup dated {folder}")
            else:
                pass


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("460x303")
    window.title("MH Rise Save Backup")
    window.wm_resizable(width=False, height=False)
    my_gui = Gui(window)
    window.mainloop()
