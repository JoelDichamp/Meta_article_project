from PySide2 import QtWidgets
from functools import partial 
from PySide2.QtCore import Slot, Qt, QRegExp
from PySide2.QtGui import QKeySequence, QRegExpValidator
from typing import List, Dict
import pathlib

from uis.diag_maj_article import Ui_Dialog
from updateTagUi import UpdateTag
import utils
import articlesManager as am
import utilsFrm as uf


class MajArticle(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, fct: str, listAllTags: List[str], columnItem: int = utils.COL_ARTICLE, articleName: str = '', dictArticle: Dict = {}):
      super().__init__()
      self.fct = fct
      self.listAllTags = listAllTags
      self.articleNameOri = articleName
      self.setupUi(self)
      self.modifSetupUi()
      if fct == utils.FCT_UPDATE:
        self.fillWidgets(columnItem, dictArticle)
      self.setupConnections()
      self.setupShortCuts()
      

    def setupShortCuts(self):
      QtWidgets.QShortcut(QKeySequence('Esc'), self, self.close)


    def modifSetupUi(self):
      title = "Add a meta-article"
      if self.fct == utils.FCT_UPDATE:
        title = "Update meta-article"
      self.setWindowTitle(title)

      btn_ok = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
      btn_cancel = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
      if self.fct == utils.FCT_CREATE:
        uf.btnSetIcon(btn_ok, uf.BTN_ADD)
      elif utils.FCT_CREATE:
        uf.btnSetIcon(btn_ok, uf.BTN_UPDATE)

      uf.btnSetIcon(btn_cancel, uf.BTN_CANCEL)

      regex = QRegExp("[^<>:|?*\"/\\\]+") #chars invalid for a file name : <, >, :, |, ?, *, ", /, \
      validator = QRegExpValidator(regex)
      self.le_articleName.setValidator(validator)
      
      self.cb_tag.addItems(self.listAllTags)
      uf.cbEditable(self.cb_tag, uf.RE_TAG)
      self.cb_tag.setCurrentIndex(-1)

      self.list_tags.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)

      
    def fillWidgets(self, columnItem: int, dictArticle: Dict):
      self.le_articleName.setText(self.articleNameOri)
      if dictArticle[utils.D_PATH_TAGS] != pathlib.Path():
        self.list_tags.addItems(dictArticle[utils.D_TAGS].split())
      self.pdfFile.addItem(str(dictArticle[utils.D_PATH_PDF]))
      self.notesFile.addItem(str(dictArticle[utils.D_PATH_NOTES]))

      self.list_tags.sortItems()
      self.putLabel()
      if columnItem == utils.COL_TAGS:
        self.cb_tag.setFocus(Qt.OtherFocusReason)


    def setupConnections(self):
      self.btn_pdfFile.clicked.connect(partial(self.selectFile, utils.D_PDF, utils.EXT_PDF))
      self.btn_notesFile.clicked.connect(partial(self.selectFile, utils.D_NOTES, utils.EXT_NOTES))
      self.btn_add_tag.clicked.connect(self.addTag)
      self.btn_remove_tag.clicked.connect(self.removeTags)
      self.list_tags.doubleClicked.connect(self.on_doubleClick)


    def putLabel(self, info: str = ''):
      nbTags = self.list_tags.count()
      text_label = f"{str(nbTags)} tag{'s' if nbTags > 1 else ''}" 
      if info:
        text_label += " - " + info
      self.label_info_tag.setText(text_label)


    def addTagOk(self, newTag: str) -> bool:
      ok = True
      tags = self.list_tags.findItems(newTag, Qt.MatchExactly)
      if tags:
        QtWidgets.QMessageBox.warning(self, "Warning", f"The '{newTag}' tag already exists!")
        self.cb_tag.setFocus(Qt.OtherFocusReason)
        ok = False

      return ok


    def addTag(self):
      tag = self.cb_tag.currentText().strip()
      if not tag:
        self.cb_tag.setFocus(Qt.OtherFocusReason)
      else:
        if self.addTagOk(tag):
          self.list_tags.addItem(tag)
          self.list_tags.sortItems()
          self.cb_tag.setCurrentIndex(-1)
          self.putLabel(f"'{tag}' add OK!")
          self.cb_tag.setFocus(Qt.OtherFocusReason)
          

    @Slot() 
    def on_doubleClick(self, index):
      tag = self.list_tags.item(index.row()).text()
      dlg = UpdateTag(tag, self.list_tags)
      dlg.exec_()
      if dlg.result() == QtWidgets.QDialog.Accepted:
        self.list_tags.item(index.row()).setText(dlg.tag)
        self.list_tags.sortItems()
        self.putLabel(f"'{tag}' update OK!")


    def removeTags(self):
      listTagsSelected = self.list_tags.selectedItems()
      lst = []
      [lst.append(t.text()) for t in listTagsSelected]
      if not lst:
        QtWidgets.QMessageBox.warning(self, "Warning", "No tag has been selected!")
      else:
        lstNames = "'" + "' '".join(lst) + "'"
        reply = QtWidgets.QMessageBox.question(self, "Question", f"Do you confirm the removal of the following tag{'s' if len(lst) > 1 else ''}:\n\t{lstNames}")
        if reply == QtWidgets.QMessageBox.Yes:
          for tagSelected in listTagsSelected:
            self.list_tags.takeItem(self.list_tags.row(tagSelected))


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
      items = []
      for i in range(self.list_tags.count()):
        items.append(self.list_tags.item(i).text())

      return ' '.join(items)

    
      
    
