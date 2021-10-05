# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form_meta_article.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from uis.btnCustom import BtnCustom

import ressource_rc

class Ui_FormMetaArticle(object):
    def setupUi(self, FormMetaArticle):
        if not FormMetaArticle.objectName():
            FormMetaArticle.setObjectName(u"FormMetaArticle")
        FormMetaArticle.resize(1078, 573)
        font = QFont()
        font.setPointSize(8)
        FormMetaArticle.setFont(font)
        icon = QIcon()
        icon.addFile(u":/_rc/article.ico", QSize(), QIcon.Normal, QIcon.Off)
        FormMetaArticle.setWindowIcon(icon)
        self.gridLayout = QGridLayout(FormMetaArticle)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_btns = QFrame(FormMetaArticle)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.w_search = QWidget(self.frame_btns)
        self.w_search.setObjectName(u"w_search")
        self.horizontalLayout_3 = QHBoxLayout(self.w_search)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_erase_search = QPushButton(self.w_search)
        self.btn_erase_search.setObjectName(u"btn_erase_search")
        self.btn_erase_search.setMinimumSize(QSize(32, 32))
        self.btn_erase_search.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/_rc/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_erase_search.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btn_erase_search)

        self.le_search = QLineEdit(self.w_search)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMinimumSize(QSize(200, 32))
        self.le_search.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_3.addWidget(self.le_search)

        self.btn_quick_search = QPushButton(self.w_search)
        self.btn_quick_search.setObjectName(u"btn_quick_search")
        self.btn_quick_search.setMinimumSize(QSize(32, 32))
        self.btn_quick_search.setMaximumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/_rc/quick_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_quick_search.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btn_quick_search)


        self.horizontalLayout_5.addWidget(self.w_search)

        self.w_search_tags = QWidget(self.frame_btns)
        self.w_search_tags.setObjectName(u"w_search_tags")
        self.horizontalLayout = QHBoxLayout(self.w_search_tags)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_search_tags = QPushButton(self.w_search_tags)
        self.btn_search_tags.setObjectName(u"btn_search_tags")
        self.btn_search_tags.setMinimumSize(QSize(160, 32))
        self.btn_search_tags.setMaximumSize(QSize(160, 32))
        icon3 = QIcon()
        icon3.addFile(u":/_rc/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search_tags.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btn_search_tags)

        self.btn_cancel_search_tags = QPushButton(self.w_search_tags)
        self.btn_cancel_search_tags.setObjectName(u"btn_cancel_search_tags")
        self.btn_cancel_search_tags.setMinimumSize(QSize(160, 32))
        self.btn_cancel_search_tags.setMaximumSize(QSize(160, 32))
        icon4 = QIcon()
        icon4.addFile(u":/_rc/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel_search_tags.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btn_cancel_search_tags)


        self.horizontalLayout_5.addWidget(self.w_search_tags)

        self.w_article = QWidget(self.frame_btns)
        self.w_article.setObjectName(u"w_article")
        self.horizontalLayout_4 = QHBoxLayout(self.w_article)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_remove_article = QPushButton(self.w_article)
        self.btn_remove_article.setObjectName(u"btn_remove_article")
        self.btn_remove_article.setMinimumSize(QSize(180, 32))
        self.btn_remove_article.setMaximumSize(QSize(180, 32))
        icon5 = QIcon()
        icon5.addFile(u":/_rc/remove_minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove_article.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.btn_remove_article)

        self.btn_add_article = BtnCustom(self.w_article)
        self.btn_add_article.setObjectName(u"btn_add_article")
        self.btn_add_article.setMinimumSize(QSize(160, 32))
        self.btn_add_article.setMaximumSize(QSize(160, 32))
        icon6 = QIcon()
        icon6.addFile(u":/_rc/add_plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_article.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.btn_add_article)


        self.horizontalLayout_5.addWidget(self.w_article)


        self.gridLayout.addWidget(self.frame_btns, 0, 0, 1, 1)

        self.tableArticles = QTableWidget(FormMetaArticle)
        if (self.tableArticles.columnCount() < 4):
            self.tableArticles.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableArticles.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableArticles.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableArticles.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableArticles.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableArticles.rowCount() < 2):
            self.tableArticles.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.tableArticles.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.tableArticles.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.tableArticles.setItem(0, 2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.tableArticles.setItem(0, 3, __qtablewidgetitem7)
        self.tableArticles.setObjectName(u"tableArticles")
        self.tableArticles.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableArticles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableArticles.setRowCount(2)
        self.tableArticles.setColumnCount(4)
        self.tableArticles.horizontalHeader().setVisible(True)
        self.tableArticles.horizontalHeader().setCascadingSectionResizes(False)

        self.gridLayout.addWidget(self.tableArticles, 1, 0, 1, 1)

        self.frame_label = QFrame(FormMetaArticle)
        self.frame_label.setObjectName(u"frame_label")
        self.frame_label.setMaximumSize(QSize(16777215, 40))
        self.frame_label.setFrameShape(QFrame.StyledPanel)
        self.frame_label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_label)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_label)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.gridLayout.addWidget(self.frame_label, 2, 0, 1, 1)


        self.retranslateUi(FormMetaArticle)

        QMetaObject.connectSlotsByName(FormMetaArticle)
    # setupUi

    def retranslateUi(self, FormMetaArticle):
        FormMetaArticle.setWindowTitle(QCoreApplication.translate("FormMetaArticle", u"Meta_article_project", None))
#if QT_CONFIG(tooltip)
        self.btn_erase_search.setToolTip(QCoreApplication.translate("FormMetaArticle", u"Delete the text to search", None))
#endif // QT_CONFIG(tooltip)
        self.btn_erase_search.setText("")
        self.le_search.setText("")
        self.le_search.setPlaceholderText(QCoreApplication.translate("FormMetaArticle", u"Enter the text to search", None))
#if QT_CONFIG(tooltip)
        self.btn_quick_search.setToolTip(QCoreApplication.translate("FormMetaArticle", u"Quick search ignoring the case", None))
#endif // QT_CONFIG(tooltip)
        self.btn_quick_search.setText("")
        self.btn_search_tags.setText(QCoreApplication.translate("FormMetaArticle", u"Search tags", None))
        self.btn_cancel_search_tags.setText(QCoreApplication.translate("FormMetaArticle", u"Cancel search tags", None))
        self.btn_remove_article.setText(QCoreApplication.translate("FormMetaArticle", u"Remove meta-articles", None))
#if QT_CONFIG(whatsthis)
        self.btn_add_article.setWhatsThis(QCoreApplication.translate("FormMetaArticle", u"nothing", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_add_article.setText(QCoreApplication.translate("FormMetaArticle", u"Add a meta-article", None))
        ___qtablewidgetitem = self.tableArticles.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormMetaArticle", u"Meta-article", None));
        ___qtablewidgetitem1 = self.tableArticles.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormMetaArticle", u"Tags", None));
        ___qtablewidgetitem2 = self.tableArticles.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormMetaArticle", u"Pdf file", None));
        ___qtablewidgetitem3 = self.tableArticles.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormMetaArticle", u"Notes file", None));

        __sortingEnabled = self.tableArticles.isSortingEnabled()
        self.tableArticles.setSortingEnabled(False)
        self.tableArticles.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(whatsthis)
        self.tableArticles.setWhatsThis(QCoreApplication.translate("FormMetaArticle", u"nothing", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText("")
    # retranslateUi

