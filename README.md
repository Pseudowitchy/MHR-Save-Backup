# MHR-Save-Backup
Script to backup monster hunter rise save files to a new folder for the current date.

Available in either Executable or .py form. If you have not installed Python on your PC then download the executable version.

# Executable version
Extract the folder and run the save_backup.exe file.

# .py version
If you have Python installed onto your system simply run the script through the command line.

# Usage
Select the location of your "Steam/userdata" directory, this is commonly placed in C:/Program Files (x86)/Steam/userdata.

Click Backup Saves to proceed, the program will create a new folder in the Save Backups folder, the new folder will be named for the date of it's creation and will contain all of the save files for Monster Hunter Rise.

The 10 backup buttons can be clicked to roll back your saves to one of the backups you have stored within the Save Backups folder. Doing so will overwrite your currently existing steam saves for Monster Hunter Rise, ensure they are backed up before you overwrite them. There is a prompt upon clicking the buttons to ensure the user intends to overwrite their saves.

In the event you wish to restore your saves from a backup that is older than those displayed within the program, you will need to navigate to:

Steam/userdata/__string of numbers tied to your steam profile__/1446780/remote

Take the win64_save folder located within the folder for the date of your choice and place it in the above folder.

# Changelog
v0.3:

Previous 10 save backups should display in the GUI as buttons, clicking a button will ask for confirmation before moving that backup into the steam folder, overwriting the existing save file. Ensure you've backed up your save before doing so to avoid losing it.

Fixed some formatting issues for text in the GUI.

v0.2:
 
Added GUI to allow the user to point the program to the steam/userdata folder

Check to ensure the folder selected is valid

Check to ask the user if they would like to overwrite an existing backup in the event of more than one backup within the same day.

Rewrote majority of code, hopefully to allow for easier changes later (fingers crossed!)

v0.1: 
Initial Release

# To Do
Improve appearance of GUI

Have the buttons showing past backup dates update when a new backup file is created.

Add GUI element to select date format for folders.

Sort out code to allow the program to work on Mac or Linux, as I don't believe they would work currently, though I cannot test it myself as of now.
