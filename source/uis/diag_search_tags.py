# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diag_search_tags.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ressource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1119, 301)
        Dialog.setMinimumSize(QSize(952, 160))
        icon = QIcon()
        icon.addFile(u":/_rc/article.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(900, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.w_tag = QWidget(self.frame)
        self.w_tag.setObjectName(u"w_tag")
        self.w_tag.setMinimumSize(QSize(0, 0))
        self.w_tag.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.w_tag)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_tag = QFrame(self.w_tag)
        self.frame_tag.setObjectName(u"frame_tag")
        self.frame_tag.setFrameShape(QFrame.StyledPanel)
        self.frame_tag.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_tag)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_tag = QLabel(self.frame_tag)
        self.label_tag.setObjectName(u"label_tag")

        self.horizontalLayout_2.addWidget(self.label_tag)

        self.cb_tag = QComboBox(self.frame_tag)
        self.cb_tag.setObjectName(u"cb_tag")
        self.cb_tag.setMinimumSize(QSize(170, 0))
        self.cb_tag.setMaxVisibleItems(20)

        self.horizontalLayout_2.addWidget(self.cb_tag)

        self.cbx_word_boundary = QCheckBox(self.frame_tag)
        self.cbx_word_boundary.setObjectName(u"cbx_word_boundary")

        self.horizontalLayout_2.addWidget(self.cbx_word_boundary)


        self.horizontalLayout_3.addWidget(self.frame_tag)


        self.horizontalLayout_4.addWidget(self.w_tag)

        self.w_req = QWidget(self.frame)
        self.w_req.setObjectName(u"w_req")
        self.gridLayout_2 = QGridLayout(self.w_req)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.le_req = QLineEdit(self.w_req)
        self.le_req.setObjectName(u"le_req")
        self.le_req.setMinimumSize(QSize(0, 0))
        self.le_req.setReadOnly(False)

        self.gridLayout_2.addWidget(self.le_req, 0, 1, 1, 1)

        self.btn_req = QPushButton(self.w_req)
        self.btn_req.setObjectName(u"btn_req")
        self.btn_req.setMinimumSize(QSize(32, 32))
        self.btn_req.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/_rc/right_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_req.setIcon(icon1)

        self.gridLayout_2.addWidget(self.btn_req, 0, 0, 1, 1)

        self.btn_erase_req = QPushButton(self.w_req)
        self.btn_erase_req.setObjectName(u"btn_erase_req")
        self.btn_erase_req.setMinimumSize(QSize(32, 32))
        self.btn_erase_req.setMaximumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/_rc/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_erase_req.setIcon(icon2)

        self.gridLayout_2.addWidget(self.btn_erase_req, 0, 2, 1, 1)

        self.cbx_ignore_case = QCheckBox(self.w_req)
        self.cbx_ignore_case.setObjectName(u"cbx_ignore_case")

        self.gridLayout_2.addWidget(self.cbx_ignore_case, 0, 3, 1, 1)


        self.horizontalLayout_4.addWidget(self.w_req)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Search tags", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The search is based on a simple Boolean query composed of opening and closing parentheses, tags and the boolean operators &quot;AND&quot; and &quot;OR&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Examples:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-ind"
                        "ent:0; text-indent:0px;\"><span style=\" font-family:'Symbol';\">	\u00b7</span><span style=\" font-family:'Times New Roman'; font-size:7pt;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span>embryonic </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	<span style=\" font-family:'Symbol';\">\u00b7</span><span style=\" font-family:'Times New Roman'; font-size:7pt;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span>ECM or metabolism </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	<span style=\" font-family:'Symbol';\">\u00b7</span><span style=\" font-family:'Times New Roman'; font-size:7pt;\">\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0 </span>(ECM or metabolism) and hESC </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" ma"
                        "rgin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tags can be entered directly into the query field or selected from the drop-down list containing all tags and then added (button &quot;-&gt;&quot;) to the query; note that the list field is editable.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The default search is &quot;case sensitive&quot;; if you want to ignore the case, check the &quot;Ignore case&quot; box.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_tag.setText(QCoreApplication.translate("Dialog", u"Tag", None))
#if QT_CONFIG(tooltip)
        self.cb_tag.setToolTip(QCoreApplication.translate("Dialog", u"List of all tags", None))
#endif // QT_CONFIG(tooltip)
        self.cbx_word_boundary.setText(QCoreApplication.translate("Dialog", u"Word boundary", None))
#if QT_CONFIG(tooltip)
        self.le_req.setToolTip(QCoreApplication.translate("Dialog", u"Boolean query", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_req.setToolTip(QCoreApplication.translate("Dialog", u"Add the selected tag to the query", None))
#endif // QT_CONFIG(tooltip)
        self.btn_req.setText("")
#if QT_CONFIG(tooltip)
        self.btn_erase_req.setToolTip(QCoreApplication.translate("Dialog", u"Delete query", None))
#endif // QT_CONFIG(tooltip)
        self.btn_erase_req.setText("")
        self.cbx_ignore_case.setText(QCoreApplication.translate("Dialog", u"Ignore case", None))
    # retranslateUi

