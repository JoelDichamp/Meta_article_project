from logging import info
from typing import Tuple
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QFont, QTextCharFormat
from functools import partial
from typing import Tuple

import os
import pathlib
import re

import qdarkstyle

import utils
from uis.main_form_meta_article import Ui_FormMetaArticle
from majArticleUi import MajArticle
from searchTagsUi import SearchTags, E_PAR_OPEN, E_PAR_CLOSE, E_OR, E_AND
from highlightDelegate import HighlightDelegate
import articlesManager as am


class ArticlesManager(QtWidgets.QWidget, Ui_FormMetaArticle):
  def __init__(self):
    super().__init__()

    self.setupUi(self)
    self.btn_cancel_search_tags.setVisible(False)
    self.setupConnections()
    self.searchTagsReq = ''
    self.ignoreCase = False
    self.getArticles()


  def setupConnections(self):
    self.btn_add_article.clicked.connect(partial(self.btnMajArticlePressed, utils.FCT_CREATE))
    self.btn_remove_article.clicked.connect(partial(self.btnRemoveArticlePressed))
    self.tableArticles.doubleClicked.connect(self.on_doubleClick)
    self.btn_quick_search.clicked.connect(partial(self.btnQuickSearchPressed))
    self.btn_erase_search.clicked.connect(partial(self.btnEraseSearchPressed))
    self.btn_search_tags.clicked.connect(self.btnSearchTagsPressed)
    self.btn_cancel_search_tags.clicked.connect(self.btnCancelSearchTagsPressed)


  @Slot() 
  def on_doubleClick(self, index):
    twi = self.tableArticles.item(index.row(), utils.COL_ARTICLE)
    dictArticle = self.dictArticles[twi.text()]
    column = index.column()
    if (column == utils.COL_ARTICLE or column == utils.COL_TAGS) and (not self.btn_cancel_search_tags.isVisible()):
      self.btnMajArticlePressed(utils.FCT_UPDATE, column, twi.text(), dictArticle)
    elif column == utils.COL_PDF or column == utils.COL_NOTES:
      k = utils.D_PATH_NOTES
      if column == utils.COL_PDF:
        k = utils.D_PATH_PDF
      pathFile = dictArticle[k]
      if pathFile:
        os.startfile(pathFile)


  def btnMajArticlePressed(self, fct: str, columnItem: int = utils.COL_ARTICLE, articleName: str = '', dictArticle: dict = {}):
    dlg = MajArticle(fct, columnItem, articleName, dictArticle)
    dlg.exec_()
    if dlg.result() == QtWidgets.QDialog.Accepted:
      self.getArticles()
      items = self.tableArticles.findItems(dlg.articleName, Qt.MatchExactly)
      for item in items:
        # item.setSelected(True)
        modelIndex = self.tableArticles.indexFromItem(item)
        rng = QtWidgets.QTableWidgetSelectionRange(modelIndex.row(), utils.COL_ARTICLE, modelIndex.row(), utils.COL_NOTES)
        self.tableArticles.setRangeSelected(rng, True)
        self.tableArticles.scrollTo(modelIndex)
        
      self.putLabel(f"'{dlg.articleName}' {fct} OK!")


  def btnRemoveArticlePressed(self):
    listModelIndex = self.tableArticles.selectedIndexes()
    listArticles = []
    for index in listModelIndex:
      if index.column() == utils.COL_ARTICLE:
        listArticles.append(self.tableArticles.item(index.row(), utils.COL_ARTICLE).text())
    if len(listArticles) == 0:
      QtWidgets.QMessageBox.warning(self, "Warning", "No meta-article has been selected!")
    else:
      names = "'" + "' '".join(listArticles) + "'"
      q = f"Do you confirm the removal of the following meta-articles:\n\t{names}" 
      reply = QtWidgets.QMessageBox.question(self, "Question", q)
      if reply == QtWidgets.QMessageBox.Yes:
        ok = True
        for article in listArticles:
          ok, error_msg = am.removeArticle(article)
          if not ok:
            QtWidgets.QMessageBox.critical(self, "Error", error_msg)
            break
        self.getArticles()
        if ok:
          self.putLabel(f"{names} removal OK!")


  def btnQuickSearchPressed(self):
    txtSearch = self.le_search.text().strip()
    if not txtSearch:
      QtWidgets.QMessageBox.warning(self, "Warning", "The text to search has not been filled in!")
      self.le_search.setFocus(Qt.OtherFocusReason)
      return

    listPathArticles = []
    items = self.tableArticles.findItems(txtSearch, Qt.MatchContains)
    for item in items:
      rowItem = self.tableArticles.row(item)
      articleName = self.tableArticles.item(rowItem, utils.COL_ARTICLE).text()
      pathArticle = self.dictArticles[articleName][utils.D_PATH_ARTICLE]
      if pathArticle not in listPathArticles:
        listPathArticles.append(pathArticle) 
      
    self.getArticles(True, txtSearch, True, listPathArticles)


  def btnEraseSearchPressed(self):
    if self.le_search.text().strip:
      self.le_search.setText('')
      self.getArticles()


  def manageWidgets(self, visible: bool):
    self.w_search.setVisible(visible)
    self.w_article.setVisible(visible)
    self.btn_cancel_search_tags.setVisible(not visible)


  def buildRegEx(self, req: str) -> Tuple[str, str]:
    listItems = req.split()
    regEx = ''
    regExHighlight = ''
    for item in listItems:
      if item == E_PAR_OPEN or item == E_PAR_CLOSE:
        regEx += item
      elif item == E_OR:
        regEx += "|"
      elif item != E_AND:
        regEx += f"(?=.*{item})"
        item = item.replace(utils.WORD_BOUNDARY, '')
        if regExHighlight:
          regExHighlight += '|' + item
        else:
          regExHighlight = item

    print(f"'{req}' -> '{regEx}'") 
    return regEx, regExHighlight


  def searchTags(self, regEx: str, ignoreCase: bool) -> list[pathlib.Path]:
    listPathArticles = []
    if ignoreCase:
      r = re.compile(regEx, re.I)
    else:
      r = re.compile(regEx)
    for k in self.dictArticles:
      res = r.search(self.dictArticles[k][utils.D_TAGS])
      if res != None:
        listPathArticles.append(self.dictArticles[k][utils.D_PATH_ARTICLE])

    return listPathArticles


  def btnSearchTagsPressed(self):
    self.getArticles()
    dlg = SearchTags(self.listAllTags, self.searchTagsReq, self.ignoreCase)
    dlg.exec_()
    if dlg.result() == QtWidgets.QDialog.Accepted:
      self.manageWidgets(False)
      self.searchTagsReq = dlg.le_req.text()
      regEx, regExHighlight = self.buildRegEx(self.searchTagsReq)
      self.ignoreCase = dlg.cbx_ignore_case.isChecked()
      listPathArticles = self.searchTags(regEx, self.ignoreCase)
      self.getArticles(True, regExHighlight, self.ignoreCase, listPathArticles, f"'{self.searchTagsReq}'")


  def btnCancelSearchTagsPressed(self):
    self.manageWidgets(True)
    self.getArticles()


  def putLabel(self, info: str = ''):
    text_label = f"{str(self.nbArticle)} meta-article{'s' if self.nbArticle > 1 else ''}" 
    if info:
      text_label += " - " + info
    self.label.setText(text_label)


  def putinfo(self, search: bool = False, ignoreCase: bool = False, listPathArticles: list[pathlib.Path] = [], infoLabel: str = ''):
    if infoLabel:
      infoCase = 'IgnoreCase' if ignoreCase else 'CaseSensitive'
      infoLabel += '   ' + infoCase

    self.putLabel(infoLabel)
    if search and (not listPathArticles):
      QtWidgets.QMessageBox.warning(self, "Warning", "No meta-article was found!")


  def getArticles(self, search: bool = False, regEx: str = '', ignoreCase: bool = False, listPathArticles: list[pathlib.Path] = [], infoLabel: str = ''):
    self.tableArticles.clearContents()
    self.listAllTags = []

    if search:
      self.initHighlightDelegate(regEx, ignoreCase)
    else:
      # delegate by default
      self.tableArticles.setItemDelegate(QtWidgets.QStyledItemDelegate()) 

    self.dictArticles = am.getArticles(search, listPathArticles)
    self.nbArticle = len(self.dictArticles.keys())
    self.tableArticles.setRowCount(self.nbArticle)
    header = self.tableArticles.horizontalHeader()
    header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
    iLine = 0
    for k in self.dictArticles:
      article = QtWidgets.QTableWidgetItem(k)
      tags = QtWidgets.QTableWidgetItem(self.dictArticles[k][utils.D_TAGS])
      pdf = QtWidgets.QTableWidgetItem(self.dictArticles[k][utils.D_PDF])
      notes = QtWidgets.QTableWidgetItem(self.dictArticles[k][utils.D_NOTES])
      self.tableArticles.setItem(iLine, utils.COL_ARTICLE, article)
      self.tableArticles.setItem(iLine, utils.COL_TAGS, tags)     
      self.tableArticles.setItem(iLine, utils.COL_PDF, pdf)     
      self.tableArticles.setItem(iLine, utils.COL_NOTES, notes)

      listTags = self.dictArticles[k][utils.D_TAGS].split()
      [self.listAllTags.append(tag) for tag in listTags if not tag in self.listAllTags]
           
      iLine += 1

    self.listAllTags.sort()
    self.putinfo(search, ignoreCase, listPathArticles, infoLabel)


  def initHighlightDelegate(self, regEx, ignoreCase: bool = False):
    self._delegate = HighlightDelegate(self.tableArticles)
    
    self._delegate.regex = QtCore.QRegExp(regEx)
    if not ignoreCase:
      self._delegate.regex.setCaseSensitivity(Qt.CaseSensitive)
    else:
      self._delegate.regex.setCaseSensitivity(Qt.CaseInsensitive)

    fmt = QTextCharFormat()
    fmt.setForeground(QtCore.Qt.green)
    fmt.setFontWeight(QFont.Bold)
    self._delegate.highlightFormat = fmt
    self.tableArticles.setItemDelegate(self._delegate)


appli = QtWidgets.QApplication([])
appli.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
win = ArticlesManager()
win.show()
appli.exec_()