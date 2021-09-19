from PySide2.QtGui import QIcon, QRegExpValidator
from PySide2.QtCore import Qt, QSize, QRegExp
from PySide2.QtWidgets import QPushButton, QComboBox

BTN_ADD = "Add"
BTN_UPDATE = "Update"
BTN_VALIDATE = "Validate"
BTN_CANCEL = "Cancel"

DICT_ICONS = { "Add": u":/_rc/add_plus.png",
               "Update": u":/_rc/update.png",
               "Validate": u":/_rc/validate.png",
               "Cancel": u":/_rc/cancel.png" }

RE_TAG = "[a-zA-Z0-9_-]+"
RE_REQ = "[a-zA-Z0-9_-\s\(\)]+" # \s = whitespace
COLOR_FOUND_TXT = Qt.green


def btnSetIcon(btn : QPushButton, btnName: str):
  btn.setText(btnName)
  icon = QIcon()
  icon.addFile(DICT_ICONS[btnName], QSize(), QIcon.Normal, QIcon.Off)
  btn.setIcon(icon)


def cbEditable(cb : QComboBox, re: str = ''):
  cb.setEditable(True)
  if re == RE_TAG:
    regex = QRegExp(RE_TAG) 
    validator = QRegExpValidator(regex)
    cb.setValidator(validator)
