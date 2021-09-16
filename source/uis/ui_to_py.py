""" compile :
  ressource.qrc -> ressource_rc.pycd s
  .ui -> .py
"""

from subprocess import run
from pathlib import Path
import sys

current_dir = Path(__file__).resolve().parent
pathPySide2 = current_dir.parent.parent / "source" / "env" / "Lib" / "site-packages" / "PySide2"
pgme_uic = pathPySide2 / "uic"
pgme_rcc = pathPySide2 / "rcc"

ressource_qrc = current_dir / "icons" / "ressource.qrc"
ressource_rc_py = current_dir.parent / "ressource_rc.py"
ret = run([pgme_rcc, "-g", "python", ressource_qrc, "-o", ressource_rc_py])
if ret.returncode == 0:
    print(f"{ressource_rc_py} : ok")
else:
  print(f"{ressource_rc_py} : error !")
  sys.exit()

for f in current_dir.iterdir():
  if f.suffix == ".ui":
    file_py = current_dir / (f.stem + ".py")
    ret = run([pgme_uic, "-g", "python", f, "-o", file_py])
    if ret.returncode == 0:
      print(f"{f} : ok")
    else:
      print(f"{f} : error !")
      break
