from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QPushButton

BTN_ADD = "Add"
BTN_UPDATE = "Update"
BTN_VALIDATE = "Validate"
BTN_CANCEL = "Cancel"

DICT_ICONS = { "Add": u":/_rc/add_plus.png",
               "Update": u":/_rc/update.png",
               "Validate": u":/_rc/validate.png",
               "Cancel": u":/_rc/cancel.png" }


def btnSetIcon(btn : QPushButton, btnName: str):
  btn.setText(btnName)
  icon = QIcon()
  icon.addFile(DICT_ICONS[btnName], QSize(), QIcon.Normal, QIcon.Off)
  btn.setIcon(icon)
