# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diag_update_tag.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 111)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_tag = QFrame(Dialog)
        self.frame_tag.setObjectName(u"frame_tag")
        self.frame_tag.setFrameShape(QFrame.StyledPanel)
        self.frame_tag.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_tag)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_tag = QLabel(self.frame_tag)
        self.label_tag.setObjectName(u"label_tag")

        self.horizontalLayout.addWidget(self.label_tag)

        self.le_tag = QLineEdit(self.frame_tag)
        self.le_tag.setObjectName(u"le_tag")
        self.le_tag.setMinimumSize(QSize(260, 0))

        self.horizontalLayout.addWidget(self.le_tag)


        self.gridLayout.addWidget(self.frame_tag, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Update tag", None))
        self.label_tag.setText(QCoreApplication.translate("Dialog", u"Tag", None))
    # retranslateUi

