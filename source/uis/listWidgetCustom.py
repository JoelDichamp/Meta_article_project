from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from pathlib import Path

import utils


class ListWidget(QtWidgets.QListWidget):
  def __init__(self, parent=None):
    super().__init__()
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
        localFile = url.toLocalFile()
        p = Path(str(localFile))
        extFile = ''
        if self.whatsThis() == 'pdf':
          extFile = utils.EXT_PDF
        elif self.whatsThis() == 'notes':
          extFile = utils.EXT_NOTES
        if (p.suffix.lower() == extFile):
          self.clear()
          self.addItems([localFile])    
    else:
      event.ignore() 


  
  