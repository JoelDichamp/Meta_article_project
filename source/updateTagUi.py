from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QRegExp, Slot
from PySide2.QtGui import QRegExpValidator


import utilsFrm as uf
from uis.diag_update_tag import Ui_Dialog


class UpdateTag(QtWidgets.QDialog, Ui_Dialog):
  def __init__(self, tag: str, list_tags: QtWidgets.QListWidget):
    super().__init__()
    self.tag = tag
    self.tagOri = tag
    self.list_tags = list_tags
    self.setupUi(self)
    self.modifSetupUi()


  def modifSetupUi(self):
    btn_ok = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
    btn_cancel = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
    uf.btnSetIcon(btn_ok, uf.BTN_UPDATE)
    uf.btnSetIcon(btn_cancel, uf.BTN_CANCEL)

    self.le_tag.setText(self.tag)
    regex_le = QRegExp(uf.RE_TAG) 
    validator_le = QRegExpValidator(regex_le)
    self.le_tag.setValidator(validator_le)


  def majTagOk(self, newTag: str) -> bool:
    ok = True
    tags = self.list_tags.findItems(newTag, Qt.MatchFixedString)
    if tags:
      if newTag.lower() != self.tagOri.lower():
        QtWidgets.QMessageBox.warning(self, "Warning", f"The '{newTag}' tag already exists!")
        ok = False

    return ok
  

  @Slot()
  def accept(self) -> None:
    self.tag = self.le_tag.text().strip()
    if self.majTagOk(self.tag):
      return super().accept()