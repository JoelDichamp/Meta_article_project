# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diag_maj_article.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from uis.listWidgetCustom import ListWidget

import ressource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 388)
        font = QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/_rc/article.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lab_articleName = QLabel(Dialog)
        self.lab_articleName.setObjectName(u"lab_articleName")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.lab_articleName.setFont(font1)

        self.gridLayout.addWidget(self.lab_articleName, 0, 0, 1, 1)

        self.le_articleName = QLineEdit(Dialog)
        self.le_articleName.setObjectName(u"le_articleName")

        self.gridLayout.addWidget(self.le_articleName, 0, 1, 1, 1)

        self.lab_tags = QLabel(Dialog)
        self.lab_tags.setObjectName(u"lab_tags")
        self.lab_tags.setFont(font1)

        self.gridLayout.addWidget(self.lab_tags, 1, 0, 1, 1)

        self.frame_tag = QFrame(Dialog)
        self.frame_tag.setObjectName(u"frame_tag")
        self.frame_tag.setFrameShape(QFrame.StyledPanel)
        self.frame_tag.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_tag)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.w_tag = QWidget(self.frame_tag)
        self.w_tag.setObjectName(u"w_tag")
        self.w_tag.setMinimumSize(QSize(0, 0))
        self.w_tag.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.w_tag)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_tag = QLabel(self.w_tag)
        self.label_tag.setObjectName(u"label_tag")

        self.horizontalLayout_2.addWidget(self.label_tag)

        self.cb_tag = QComboBox(self.w_tag)
        self.cb_tag.setObjectName(u"cb_tag")
        self.cb_tag.setMinimumSize(QSize(170, 0))
        self.cb_tag.setMaxVisibleItems(20)

        self.horizontalLayout_2.addWidget(self.cb_tag)


        self.horizontalLayout.addWidget(self.w_tag)

        self.btn_add_tag = QPushButton(self.frame_tag)
        self.btn_add_tag.setObjectName(u"btn_add_tag")
        self.btn_add_tag.setMinimumSize(QSize(32, 32))
        self.btn_add_tag.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/_rc/right_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_tag.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_add_tag)

        self.w_list_tags = QWidget(self.frame_tag)
        self.w_list_tags.setObjectName(u"w_list_tags")
        self.verticalLayout = QVBoxLayout(self.w_list_tags)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_remove_tag = QPushButton(self.w_list_tags)
        self.btn_remove_tag.setObjectName(u"btn_remove_tag")
        self.btn_remove_tag.setMinimumSize(QSize(110, 32))
        self.btn_remove_tag.setMaximumSize(QSize(110, 32))
        icon2 = QIcon()
        icon2.addFile(u":/_rc/remove_minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_tag.setIcon(icon2)

        self.verticalLayout.addWidget(self.btn_remove_tag)

        self.list_tags = QListWidget(self.w_list_tags)
        self.list_tags.setObjectName(u"list_tags")

        self.verticalLayout.addWidget(self.list_tags)


        self.horizontalLayout.addWidget(self.w_list_tags)


        self.gridLayout.addWidget(self.frame_tag, 1, 1, 1, 1)

        self.lab_pdfFile = QLabel(Dialog)
        self.lab_pdfFile.setObjectName(u"lab_pdfFile")
        self.lab_pdfFile.setFont(font1)

        self.gridLayout.addWidget(self.lab_pdfFile, 2, 0, 1, 1)

        self.pdfFile = ListWidget(Dialog)
        self.pdfFile.setObjectName(u"pdfFile")
        self.pdfFile.setMaximumSize(QSize(16777215, 40))
        self.pdfFile.setToolTipDuration(-1)

        self.gridLayout.addWidget(self.pdfFile, 2, 1, 1, 1)

        self.btn_pdfFile = QPushButton(Dialog)
        self.btn_pdfFile.setObjectName(u"btn_pdfFile")
        self.btn_pdfFile.setMinimumSize(QSize(32, 32))
        self.btn_pdfFile.setMaximumSize(QSize(32, 32))
        icon3 = QIcon()
        icon3.addFile(u":/_rc/pdf_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pdfFile.setIcon(icon3)

        self.gridLayout.addWidget(self.btn_pdfFile, 2, 2, 1, 1)

        self.lab_notesFile = QLabel(Dialog)
        self.lab_notesFile.setObjectName(u"lab_notesFile")
        self.lab_notesFile.setFont(font1)

        self.gridLayout.addWidget(self.lab_notesFile, 3, 0, 1, 1)

        self.notesFile = ListWidget(Dialog)
        self.notesFile.setObjectName(u"notesFile")
        self.notesFile.setMaximumSize(QSize(16777215, 40))
        self.notesFile.setToolTipDuration(-1)

        self.gridLayout.addWidget(self.notesFile, 3, 1, 1, 1)

        self.btn_notesFile = QPushButton(Dialog)
        self.btn_notesFile.setObjectName(u"btn_notesFile")
        self.btn_notesFile.setMinimumSize(QSize(32, 32))
        self.btn_notesFile.setMaximumSize(QSize(32, 32))
        icon4 = QIcon()
        icon4.addFile(u":/_rc/word_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_notesFile.setIcon(icon4)

        self.gridLayout.addWidget(self.btn_notesFile, 3, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lab_articleName.setText(QCoreApplication.translate("Dialog", u"Article name", None))
        self.le_articleName.setText("")
        self.lab_tags.setText(QCoreApplication.translate("Dialog", u"Tags", None))
        self.label_tag.setText(QCoreApplication.translate("Dialog", u"Tag", None))
#if QT_CONFIG(tooltip)
        self.cb_tag.setToolTip(QCoreApplication.translate("Dialog", u"List of all tags", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_add_tag.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:8pt;\">Add the selected tag to the list</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_tag.setText("")
        self.btn_remove_tag.setText(QCoreApplication.translate("Dialog", u"Remove tags", None))
        self.lab_pdfFile.setText(QCoreApplication.translate("Dialog", u"PDF File", None))
#if QT_CONFIG(tooltip)
        self.pdfFile.setToolTip(QCoreApplication.translate("Dialog", u"Drag and drop the pdf file here!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pdfFile.setWhatsThis(QCoreApplication.translate("Dialog", u"pdf", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.pdfFile.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.btn_pdfFile.setToolTip(QCoreApplication.translate("Dialog", u"To select a pdf File", None))
#endif // QT_CONFIG(tooltip)
        self.btn_pdfFile.setText("")
        self.lab_notesFile.setText(QCoreApplication.translate("Dialog", u"Notes file", None))
#if QT_CONFIG(tooltip)
        self.notesFile.setToolTip(QCoreApplication.translate("Dialog", u"Drag and drop the notes file (.docx) here!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.notesFile.setWhatsThis(QCoreApplication.translate("Dialog", u"notes", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.btn_notesFile.setToolTip(QCoreApplication.translate("Dialog", u"To select a notes file (.docx)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_notesFile.setText("")
    # retranslateUi

