from pathlib import Path
from datetime import datetime
import shutil

date = datetime.now()

# This will place the backed up save files into new folder named for the current date in MM-DD-YYYY format.
# If you wish to change the date format you can change the order at the end of the line below, for 2 digit date use %y instead of %Y.
target = Path() / date.strftime("%m-%d-%Y")

# Edit this line to where your saves are located, the 1446780 folder is the folder for the game, the folder that contains it is dependant on your steam profile.
source = Path(r"C:/Program Files (x86)/Steam/userdata/32342647/1446780/remote")


shutil.copytree(source, target)
