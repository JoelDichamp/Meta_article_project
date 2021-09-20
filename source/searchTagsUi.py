from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtCore import Slot
from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence
from typing import List

from uis.diag_search_tags import Ui_Dialog
import utils
import utilsFrm as uf

E_PAR_OPEN = '('
E_PAR_CLOSE = ')'
E_TAG = "TAG"
E_OR = 'OR'
E_AND = 'AND'


class SearchTags(QtWidgets.QDialog, Ui_Dialog):
  def __init__(self, listAllTags: List[str], searchTagsReq: str, ignoreCase: bool):
      super().__init__()
      self.listAllTags = listAllTags
      self.setupUi(self)
      self.modifSetupUi(searchTagsReq, ignoreCase)
      self.setupConnections()
      self.setupShortCuts()


  def setupShortCuts(self):
    QtWidgets.QShortcut(QKeySequence('Esc'), self, self.close)
  
  
  def modifSetupUi(self, searchTagsReq: str, ignoreCase: bool):
    btn_ok = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
    btn_cancel = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
    uf.btnSetIcon(btn_ok, uf.BTN_VALIDATE)
    uf.btnSetIcon(btn_cancel, uf.BTN_CANCEL)

    self.cb_tag.addItems(self.listAllTags)
    uf.cbEditable(self.cb_tag, uf.RE_TAG)

    regex_le = QtCore.QRegExp(uf.RE_REQ) 
    validator_le = QtGui.QRegExpValidator(regex_le)
    self.le_req.setValidator(validator_le)

    self.initUi(searchTagsReq, ignoreCase)


  def initUi(self, searchTagsReq: str = '', ignoreCase: bool = False):
    self.frameTagCleaned()
    self.nbParOpen = 0
    if searchTagsReq:
      self.cbx_ignore_case.setChecked(ignoreCase)
      self.le_req.setText(searchTagsReq)
    self.le_req.setFocus(Qt.OtherFocusReason)
    

  def setupConnections(self):
    self.btn_req.clicked.connect(self.btnReqPressed)
    self.btn_erase_req.clicked.connect(self.btnEraseReqPressed)


  def frameTagCleaned(self):
    self.cb_tag.setCurrentIndex(-1)
    self.cbx_word_boundary.setChecked(False)


  def automatReq(self, txtItem: str, listItemsReq: List[str]) -> List[str]:
    listItems = []
    # print(txtItem, self.nbParOpen)
    if txtItem == E_TAG:
      """ suit une ) ou un ope : 
        ) : que si on a une ( en cours et un ope avant le tag
        ope : c'est le même que celui (s'il existe) qui est avant le tag saisi
      """
      penultimateItem = ''
      if len(listItemsReq) >= 2:
        penultimateItem = listItemsReq[-2]
      if penultimateItem == E_AND or penultimateItem == E_OR:
        listItems.append(penultimateItem)
        if self.nbParOpen > 0:
          listItems.append(E_PAR_CLOSE)
      else:
        # c'est une ( ou rien
        listItems.extend([E_OR, E_AND])

    elif txtItem == E_PAR_OPEN:
      """ suit une ( ou un tag 
        maj du nb de parenthèses ouvrantes
      """
      self.nbParOpen += 1
      listItems = [E_PAR_OPEN, E_TAG]

    elif txtItem == E_PAR_CLOSE:
      """ suit une ) ou un ope :
        ) : que si on a une ( en cours, 
        ope : OR ou AND
        maj du nb de parenthèses ouvrantes
      """
      if self.nbParOpen > 0: 
        self.nbParOpen -= 1
        listItems.append(E_PAR_CLOSE)
      listItems.extend([E_OR, E_AND])

    elif txtItem == E_OR or txtItem == E_AND:
      """ suit une ( ou un tag 
      """
      listItems = [E_PAR_OPEN, E_TAG]

    return listItems


  def btnReqPressed(self):
    text = self.cb_tag.currentText().strip()
    if not text:
        QtWidgets.QMessageBox.warning(self, "Warning", "No tag has been selected!")
        self.cb_tag.setFocus(Qt.OtherFocusReason)
        return
    if self.cbx_word_boundary.isChecked():
      text = utils.WORD_BOUNDARY + text + utils.WORD_BOUNDARY
    
    le_text = self.le_req.text()
    if le_text:
      le_text += ' ' + text
    else:
      le_text = text
    self.le_req.setText(le_text)
    self.le_req.setFocus(Qt.OtherFocusReason)
    self.frameTagCleaned()
    

  def btnEraseReqPressed(self):
    self.le_req.setText('')
    self.initUi()


  def whichItem(self, iItem : int, listItemsReq: List[str]) -> str:
    item = listItemsReq[iItem]
    if item.upper() == E_OR or item.upper() == E_AND:
      item = item.upper()
      listItemsReq[iItem] = item

    if item != E_PAR_CLOSE and item != E_PAR_OPEN and item != E_OR and item != E_AND:
      item = E_TAG

    return item


  def putMessage(self, msg: str):
    QtWidgets.QMessageBox.warning(self, "Warning", msg)
    self.le_req.setFocus(Qt.OtherFocusReason)


  def isReqValid(self) -> bool:
    ok = False

    txtReq = self.le_req.text().strip()
    if not txtReq:
      self.putMessage("Invalid query: the query was not entered!")
      return ok

    nbParOpen = txtReq.count(E_PAR_OPEN)
    nbParClose = txtReq.count(E_PAR_CLOSE)
    if nbParOpen != nbParClose:
      self.putMessage(f"Invalid query: the number of brackets is incorrect, {nbParOpen} ( and {nbParClose} )!")
      return ok
    
    txtReq = txtReq.replace(E_PAR_OPEN, f' {E_PAR_OPEN} ').replace(E_PAR_CLOSE, f' {E_PAR_CLOSE} ')
    listItemsReq = txtReq.split()
    for i in range(len(listItemsReq)):
      # print("i", i, listItemsReq[i])
      txtItem = self.whichItem(i, listItemsReq)
      # print("txtItem", txtItem, listItemsReq)
      listValidItems = self.automatReq(txtItem, listItemsReq[0:i+1])
      # print("listValidItems", listValidItems)

      if i < len(listItemsReq) - 1:
        itemNext = self.whichItem((i+1), listItemsReq)
        # print("itemNext", itemNext)
        ok = False
        for item in listValidItems:
          if item == itemNext:
            ok = True
            break
        if not ok:
          self.putMessage(f"Invalid query: Unexpected rank {i+1} '{itemNext}' element,\n\texpected {' or '.join(listValidItems)}!")
          break
      else: # last item
        ok = (txtItem != E_AND and txtItem != E_OR)
        if not ok:
          self.putMessage("Invalid query: the query is incomplete!")

    return ok


  @Slot()
  def accept(self) -> None:
    if self.isReqValid():
      return super().accept()