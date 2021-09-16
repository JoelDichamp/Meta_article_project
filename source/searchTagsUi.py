from re import I
from PySide2 import QtWidgets
from PySide2.QtCore import Slot
from PySide2.QtCore import Qt

from uis.diag_search_tags import Ui_Dialog
import utils
import utilsFrm as uf

E_PAR_OPEN = '('
E_PAR_CLOSE = ')'
E_TAG = "TAG"
E_OR = 'OR'
E_AND = 'AND'


class SearchTags(QtWidgets.QDialog, Ui_Dialog):
  def __init__(self, listAllTags: list[str], searchTagsReq: str, ignoreCase: bool):
      super().__init__()
      self.listAllTags = listAllTags
      self.setupUi(self)
      self.modifSetupUi(searchTagsReq, ignoreCase)
      self.setupConnections()
  
  
  def modifSetupUi(self, searchTagsReq: str, ignoreCase: bool):
    btn_ok = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
    btn_cancel = self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel)
    uf.btnSetIcon(btn_ok, uf.BTN_VALIDATE)
    uf.btnSetIcon(btn_cancel, uf.BTN_CANCEL)

    self.cb_tag.addItems(self.listAllTags)
    self.cb_tag.setEditable(True)
    self.initUi(searchTagsReq, ignoreCase)


  def initUi(self, searchTagsReq: str = '', ignoreCase: bool = False):
    self.frameTagCleaned()
    self.nbParOpen = 0
    if searchTagsReq:
      self.cbx_ignore_case.setChecked(ignoreCase)
      self.le_req.setText(searchTagsReq)
      listItemsReq = searchTagsReq.split()
      lastItem = listItemsReq[-1]
      if lastItem == E_PAR_CLOSE:
        txtItem = E_PAR_CLOSE
      else:
        txtItem = E_TAG
      self.automatReq(txtItem)
    else:
      self.cbItemFilled([E_PAR_OPEN, E_TAG])
    

  def setupConnections(self):
    self.btn_req.clicked.connect(self.btnReqPressed)
    self.cb_item.currentTextChanged.connect(self.cbItemChanged)
    self.btn_erase_req.clicked.connect(self.btnEraseReqPressed)
    self.btn_erase_last_item.clicked.connect(self.btnEraseLastItemPressed)


  def frameTagCleaned(self):
    self.cb_tag.setCurrentIndex(0)
    self.cbx_word_boundary.setChecked(False)
    self.frame_tag.setVisible(False)


  def cbItemChanged(self):
    text = self.cb_item.currentText()
    if text == E_TAG:
      self.frame_tag.setVisible(True)
      self.cb_tag.setFocus(Qt.OtherFocusReason)
    else:
      self.frameTagCleaned()


  def cbItemFilled(self, listItems: list[str]):
    self.cb_item.clear()
    self.cb_item.addItems(listItems)


  def automatReq(self, txtItem: str, deleteLastItem: bool = False):
    # print(txtItem, self.nbParOpen)
    if txtItem == E_TAG:
      """ suit une ) ou un ope : 
        ) : que si on a une ( en cours et un ope avant le tag
        ope : c'est le même que celui (s'il existe) qui est avant le tag saisi
      """
      listItems = []
      listItemsReq = self.le_req.text().split()
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

      self.cbItemFilled(listItems)
      self.frameTagCleaned()

    elif txtItem == E_PAR_OPEN:
      """ suit une ( ou un tag 
        maj du nb de parenthèses ouvrantes
      """
      if not deleteLastItem:
        self.nbParOpen += 1
      self.cbItemFilled([E_PAR_OPEN, E_TAG])

    elif txtItem == E_PAR_CLOSE:
      """ suit une ) ou un ope :
        ) : que si on a une ( en cours, 
        ope : OR ou AND
        maj du nb de parenthèses ouvrantes
      """
      if not deleteLastItem:
        if self.nbParOpen > 0: 
          self.nbParOpen -= 1
      listItems = []
      if self.nbParOpen > 0:
        listItems.append(E_PAR_CLOSE)
      listItems.extend([E_OR, E_AND])
      self.cbItemFilled(listItems)

    elif txtItem == E_OR or txtItem == E_AND:
      """ suit une ( ou un tag 
      """
      self.cbItemFilled([E_PAR_OPEN, E_TAG])


  def btnReqPressed(self):
    txtItem = self.cb_item.currentText()
    if txtItem == E_TAG:
      text = self.cb_tag.currentText().strip()
      if not text:
        QtWidgets.QMessageBox.warning(self, "Warning", "No tag has been selected!")
      if self.cbx_word_boundary.isChecked():
        text = utils.WORD_BOUNDARY + text + utils.WORD_BOUNDARY
    else:
      text = txtItem
    
    le_text = self.le_req.text()
    if le_text:
      le_text += ' ' + text
    else:
      le_text = text
    self.le_req.setText(le_text)
    
    self.automatReq(txtItem)
    

  def btnEraseReqPressed(self):
    self.le_req.setText('')
    self.initUi()


  def btnEraseLastItemPressed(self):
    listItemsReq = self.le_req.text().split()
    if not listItemsReq:
      return

    lastItem = listItemsReq[-1]
    if lastItem == E_PAR_OPEN:
      self.nbParOpen -= 1
    elif lastItem == E_PAR_CLOSE:
      self.nbParOpen += 1

    # print("lastitem à virer", lastItem, "nbParOpen", self.nbParOpen)

    listItemsReq = listItemsReq[0:-1]
    self.le_req.setText(' '.join(listItemsReq))

    if not listItemsReq:
      self.cbItemFilled([E_PAR_OPEN, E_TAG])
      return

    lastItem = listItemsReq[-1]
    if lastItem != E_PAR_CLOSE and lastItem != E_PAR_OPEN and lastItem != E_OR and lastItem != E_AND:
      lastItem = E_TAG

    # print("lastitem pour automat", lastItem)
    self.automatReq(lastItem, True)


  def isReqValid(self) -> bool:
    ok = False

    listItemsReq = self.le_req.text().split()
    if not listItemsReq:
      QtWidgets.QMessageBox.warning(self, "Warning", "Invalid query: the query was not entered!")

    elif self.nbParOpen != 0:
      QtWidgets.QMessageBox.warning(self, "Warning", "Invalid query: the number of brackets is incorrect!")
    
    elif listItemsReq[-1] == E_AND or listItemsReq[-1] == E_OR:
      QtWidgets.QMessageBox.warning(self, "Warning", "Invalid query: the query is incomplete!")

    else:
      ok = True

    return ok


  @Slot()
  def accept(self) -> None:
    if self.isReqValid():
      return super().accept()