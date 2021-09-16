from PySide2 import QtWidgets
from PySide2.QtCore import Slot, QSize
from functools import partial 
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon

from uis.diag_maj_article import Ui_Dialog
import utils
import articlesManager as am
import utilsFrm as uf


class MajArticle(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, fct: str, columnItem: int = utils.COL_ARTICLE, articleName: str = '', dictArticle: dict = {}):
      super().__init__()
      self.fct = fct
      self.articleNameOri = articleName
      self.setupUi(self)
      self.modifSetupUi()
      if fct == utils.FCT_UPDATE:
        self.fillWidgets(columnItem, dictArticle)
      self.setupConnections()
      

    def modifSetupUi(self):
      title = "Add a meta-article"
      if self.fct == utils.FCT_UPDATE:
        title = "Update the meta-article"
      self.setWindowTitle(title)

      btn_ok = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
      btn_cancel = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
      if self.fct == utils.FCT_CREATE:
        uf.btnSetIcon(btn_ok, uf.BTN_ADD)
      elif utils.FCT_CREATE:
        uf.btnSetIcon(btn_ok, uf.BTN_UPDATE)

      uf.btnSetIcon(btn_cancel, uf.BTN_CANCEL)


    def fillWidgets(self, columnItem: int, dictArticle: dict):
      self.le_articleName.setText(self.articleNameOri)
      self.te_tags.setText(dictArticle[utils.D_TAGS])
      self.pdfFile.addItem(str(dictArticle[utils.D_PATH_PDF]))
      self.notesFile.addItem(str(dictArticle[utils.D_PATH_NOTES]))

      if columnItem == utils.COL_TAGS:
        self.te_tags.setFocus(Qt.OtherFocusReason)


    def setupConnections(self):
      self.btn_pdfFile.clicked.connect(partial(self.selectFile, utils.D_PDF, utils.EXT_PDF))
      self.btn_notesFile.clicked.connect(partial(self.selectFile, utils.D_NOTES, utils.EXT_NOTES))


    def selectFile(self, typeFile: str, ext: str):
      lw = self.pdfFile
      if typeFile == utils.D_NOTES:
        lw = self.notesFile

      caption = f"Select {typeFile} file"
      filter = f"{typeFile} files *{ext}"
      dir = str(utils.dataFolder)
      fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption=caption, dir=dir, filter=filter)
      if fileName:
        lw.clear()
        lw.addItems([fileName])


    @Slot()
    def accept(self) -> None:
      self.articleName = self.le_articleName.text().strip()
      if not self.le_articleName.text():
        QtWidgets.QMessageBox.warning(self, "Warning", "The name of the article has not been filled in!")
      elif am.articleAlreadyUsed(self.fct, self.articleName, self.articleNameOri):
        QtWidgets.QMessageBox.warning(self, "Warning", f"The article '{self.articleName}' already exists!")
      else:
        tags = self.manageTags()

        pdfFile = ''
        if self.pdfFile.count() > 0:
          pdfFile = self.pdfFile.item(0).text()

        notesFile = ''
        if self.notesFile.count() > 0:
          notesFile = self.notesFile.item(0).text()

        ok, error_msg = am.majArticle(self.fct, self.articleName, self.articleNameOri, tags, pdfFile, notesFile)
        if not ok:
          QtWidgets.QMessageBox.critical(self, "Error", error_msg)
        else:
          return super().accept()

      
    def manageTags(self):
      tags = self.te_tags.toPlainText()
      tags = tags.replace("\n", " ")
      list_tags = tags.split()
      list_tags_clean = []
      for tag in list_tags:
        if tag not in list_tags_clean:
          list_tags_clean.append(tag)

      return ' '.join(list_tags_clean)

    
      
    
