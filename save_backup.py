from pathlib import Path
from datetime import datetime
import shutil

date = datetime.now()

source = Path(r"C:/Program Files (x86)/Steam/userdata/53828396/1446780/remote")
# source = Path(r"C:/Program Files (x86)/Steam/userdata/32342647/1446780/remote")
target = Path() / date.strftime("%m-%d-%Y")

shutil.copytree(source, target)
