from PySide2 import QtCore, QtGui, QtWidgets

class HighlightDelegate(QtWidgets.QStyledItemDelegate):
  def __init__(self, parent=None):
    super(HighlightDelegate, self).__init__(parent)
    self.doc = QtGui.QTextDocument(self)
    self._regex = QtCore.QRegExp()
    self._highlight_format = QtGui.QTextCharFormat()

  def paint(self, painter, option, index):
    painter.save()
    options = QtWidgets.QStyleOptionViewItem(option)
    self.initStyleOption(options, index)
    self.doc.setPlainText(options.text)
    self.apply_highlight()
    options.text = ""
    style = QtWidgets.QApplication.style() if options.widget is None else options.widget.style()
    style.drawControl(QtWidgets.QStyle.CE_ItemViewItem, options, painter)

    ctx = QtGui.QAbstractTextDocumentLayout.PaintContext()
    if option.state & QtWidgets.QStyle.State_Selected:
        ctx.palette.setColor(QtGui.QPalette.Text, option.palette.color(
            QtGui.QPalette.Active, QtGui.QPalette.HighlightedText))
    else:
        ctx.palette.setColor(QtGui.QPalette.Text, option.palette.color(
            QtGui.QPalette.Active, QtGui.QPalette.Text))

    textRect = style.subElementRect(
        QtWidgets.QStyle.SE_ItemViewItemText, options)

    if index.column() != 0:
        textRect.adjust(5, 0, 0, 0)

    the_constant = 4
    margin = (option.rect.height() - options.fontMetrics.height()) // 2
    margin = margin - the_constant
    textRect.setTop(textRect.top() + margin)

    painter.translate(textRect.topLeft())
    painter.setClipRect(textRect.translated(-textRect.topLeft()))
    self.doc.documentLayout().draw(painter, ctx)

    painter.restore()

  def apply_highlight(self):
      cursor = QtGui.QTextCursor(self.doc)
      cursor.beginEditBlock()
      highlightCursor = QtGui.QTextCursor(self.doc)
      while not highlightCursor.isNull() and not highlightCursor.atEnd():
          highlightCursor = self.doc.find(self.regex, highlightCursor)
          if not highlightCursor.isNull():
              highlightCursor.mergeCharFormat(self.highlightFormat)
      cursor.endEditBlock()

  @property
  def regex(self):
      return self._regex

  @regex.setter
  def regex(self, regex: QtCore.QRegExp):
      if self._regex == regex: return
      self._regex = regex

  @property
  def highlightFormat(self):
      return self._highlight_format

  @highlightFormat.setter
  def highlightFormat(self, fmt):
      self._highlight_format = fmt
