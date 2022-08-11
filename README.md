# MHR-Save-Backup
Script to backup monster hunter rise save files to a new folder for the current date.

Available in either Executable or .py form. If you have not installed Python on your PC then download the executable version.

# Executable version
Extract the folder and run the save_backup.exe shortcut.

# .py version
If you have Python installed onto your system simply run the script through the command line.

# Usage
Select the location of your "Steam/userdata" directory, this is commonly placed in C:/Program Files (x86)/Steam/userdata.

Click Backup Saves to proceed, the program will create a new folder in the same location as the shortcut.

The new folder will be named for the date you backed up the saves and should contain all of your save files for Monster Hunter Rise.

In the event you wish to restore your saves from a backup that you have made, you will need to navigate to:

Steam/userdata/__string of numbers tied to your steam profile__/1446780/remote

Take the win64_save folder located within the folder for the date of your choice and place it in the above folder.

# Changelog
v0.1: 
Initial Release
v0.2: 
Added GUI to allow the user to point the program to the steam/userdata folder
Check to ensure the folder selected is valid
Check to ask the user if they would like to overwrite an existing backup in the event of more than one backup within the same day.
Rewrote majority of code, hopefully to allow for easier changes later (fingers crossed!)

# To Do
Fix weird text formatting on overwrite confirmation prompt
Add label showing most recent save backup
Allow user to roll back saves to one of the stored backup files
Add GUI element to select date format for folders.