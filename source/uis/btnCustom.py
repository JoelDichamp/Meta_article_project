from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QEvent
from PySide2.QtGui import QKeyEvent
import pathlib 
from typing import Tuple

import utils
import articlesManager as am


class BtnCustom(QtWidgets.QPushButton):
  def __init__(self, txt, parent=None):
    super().__init__(txt)
    self.setAcceptDrops(True)


  def dragEnterEvent(self, event):
    if event.mimeData().hasUrls():
      event.accept()
    else:
      event.ignore()


  def dragMoveEvent(self, event):
    if event.mimeData().hasUrls():
      event.accept()
    else:
      event.ignore()


  def dropEvent(self, event):
    if event.mimeData().hasUrls():
      event.setDropAction(Qt.CopyAction)
      event.accept()
      url = event.mimeData().urls()[0]
      if url.isLocalFile():
        pDir = pathlib.Path(str(url.toLocalFile()))
        if not pDir.is_dir():
          QtWidgets.QMessageBox.warning(self, "Warning", "A directory is expected not a file!")
        elif am.articleAlreadyUsed(utils.FCT_CREATE, pDir.name, ''):
          QtWidgets.QMessageBox.warning(self, "Warning", f"The article '{pDir.name}' already exists!")
        else:
          ok, error_msg, tags, pdfFile, notesFile = self.getInfosArticle(pDir) 
          if not ok:
            QtWidgets.QMessageBox.critical(self, "Error", error_msg)
          ok, error_msg = am.majArticle(utils.FCT_CREATE, pDir.name, '', tags, pdfFile, notesFile)
          if not ok:
            QtWidgets.QMessageBox.critical(self, "Error", error_msg)
          self.setWhatsThis(pDir.name)
          self.animateClick()


  def getInfosArticle(self, pDir: pathlib.Path) -> Tuple[bool, str, str, str, str]:
    ok = True
    error_msg = ''

    notesFile = ''
    pdfFile = ''
    tags = ''
    word_ok = False
    pdf_ok = False
    json_ok = False
    for f in pDir.iterdir():
      if (not word_ok) and (f.suffix.lower() == utils.EXT_NOTES):
        notesFile = str(f)
        word_ok = True
      elif (not pdf_ok) and (f.suffix.lower() == utils.EXT_PDF):
        pdfFile = str(f)
        pdf_ok = True
      elif (not json_ok) and (f.suffix.lower() == utils.EXT_TAGS):
        ok, error_msg, listTags = am.checkTagsFile(f)
        tags = ' '.join(listTags)

      if word_ok and pdf_ok and json_ok: break

    return ok, error_msg, tags, pdfFile, notesFile
