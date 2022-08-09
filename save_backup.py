from pathlib import Path
from datetime import datetime
import shutil

date = datetime.now()
steam = Path(r"C:/Program Files (x86)/Steam/userdata")

# This will place the backed up save files into new folder named for the current date in MM-DD-YYYY format.
# If you wish to change the date format you can change the order at the end of the line below, for 2 digit date use %y instead of %Y.
target = Path() / date.strftime("%m-%d-%Y")

saves = [p for p in steam.rglob("1446780/remote")]
for save in saves:
    source = save

shutil.copytree(source, target)
