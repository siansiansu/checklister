# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/namegen.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(705, 585)
        self.tabWidget = QtWidgets.QTabWidget(Window)
        self.tabWidget.setGeometry(QtCore.QRect(10, 130, 681, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tabSelect = QtWidgets.QWidget()
        self.tabSelect.setObjectName("tabSelect")
        self.treeWidget = QtWidgets.QTreeWidget(self.tabSelect)
        self.treeWidget.setGeometry(QtCore.QRect(10, 80, 651, 271))
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.treeWidget.setIndentation(10)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setDefaultSectionSize(60)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setMinimumSectionSize(2)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tabSelect)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(490, 360, 171, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.butGenerateSp = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.butGenerateSp.setObjectName("butGenerateSp")
        self.horizontalLayout_4.addWidget(self.butGenerateSp)
        self.butClose1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.butClose1.setObjectName("butClose1")
        self.horizontalLayout_4.addWidget(self.butClose1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tabSelect)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 551, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineSpecies = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineSpecies.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.lineSpecies.setFont(font)
        self.lineSpecies.setAutoFillBackground(False)
        self.lineSpecies.setObjectName("lineSpecies")
        self.gridLayout_3.addWidget(self.lineSpecies, 0, 1, 1, 1)
        self.butAddToTree = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.butAddToTree.setObjectName("butAddToTree")
        self.gridLayout_3.addWidget(self.butAddToTree, 0, 2, 1, 1)
        self.butDeleteSelection = QtWidgets.QPushButton(self.tabSelect)
        self.butDeleteSelection.setGeometry(QtCore.QRect(10, 360, 127, 32))
        self.butDeleteSelection.setObjectName("butDeleteSelection")
        self.butDeleteAll = QtWidgets.QPushButton(self.tabSelect)
        self.butDeleteAll.setGeometry(QtCore.QRect(140, 360, 131, 32))
        self.butDeleteAll.setObjectName("butDeleteAll")
        self.label_7 = QtWidgets.QLabel(self.tabSelect)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tabSelect, "")
        self.tabBatch = QtWidgets.QWidget()
        self.tabBatch.setObjectName("tabBatch")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tabBatch)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 411, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineBlist = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineBlist.setText("")
        self.lineBlist.setObjectName("lineBlist")
        self.horizontalLayout_2.addWidget(self.lineBlist)
        self.butBlist = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.butBlist.setObjectName("butBlist")
        self.horizontalLayout_2.addWidget(self.butBlist)
        self.tabWidget.addTab(self.tabBatch, "")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Window)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 681, 102))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.butSelectTempFile = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.butSelectTempFile.setObjectName("butSelectTempFile")
        self.gridLayout_2.addWidget(self.butSelectTempFile, 2, 2, 1, 1)
        self.comboDBselect = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboDBselect.setObjectName("comboDBselect")
        self.comboDBselect.addItem("")
        self.comboDBselect.addItem("")
        self.comboDBselect.addItem("")
        self.gridLayout_2.addWidget(self.comboDBselect, 0, 1, 1, 1)
        self.lineOutputFilename = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineOutputFilename.setText("")
        self.lineOutputFilename.setObjectName("lineOutputFilename")
        self.gridLayout_2.addWidget(self.lineOutputFilename, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.butSelectOutput = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.butSelectOutput.setObjectName("butSelectOutput")
        self.gridLayout_2.addWidget(self.butSelectOutput, 1, 2, 1, 1)
        self.lineSlist = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineSlist.setObjectName("lineSlist")
        self.gridLayout_2.addWidget(self.lineSlist, 2, 3, 1, 1)
        self.butUpdateDB = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.butUpdateDB.setObjectName("butUpdateDB")
        self.gridLayout_2.addWidget(self.butUpdateDB, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineTempFile = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineTempFile.setObjectName("lineTempFile")
        self.gridLayout_2.addWidget(self.lineTempFile, 2, 1, 1, 1)
        self.butSlist = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.butSlist.setObjectName("butSlist")
        self.gridLayout_2.addWidget(self.butSlist, 2, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 1)

        self.retranslateUi(Window)
        self.tabWidget.setCurrentIndex(0)
        self.butClose1.clicked.connect(Window.close)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "物種名錄產生器 namelist generator"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("Window", "科名"))
        self.treeWidget.headerItem().setText(1, _translate("Window", "學名"))
        self.treeWidget.headerItem().setText(2, _translate("Window", "中文名"))
        self.butGenerateSp.setText(_translate("Window", "產生名錄"))
        self.butClose1.setText(_translate("Window", "關閉"))
        self.label_5.setText(_translate("Window", "中文名"))
        self.lineSpecies.setToolTip(_translate("Window", "<html><head/><body><p>輸入物種開頭前幾字則會列出近似物種，</p><p>可按 enter 或 return 選擇該物種加入下方物種名錄清單</p></body></html>"))
        self.butAddToTree.setText(_translate("Window", "加入清單"))
        self.butDeleteSelection.setText(_translate("Window", "刪除所選物種"))
        self.butDeleteAll.setText(_translate("Window", "刪除所有物種"))
        self.label_7.setText(_translate("Window", "物種名錄清單"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSelect), _translate("Window", "選擇物種"))
        self.label.setText(_translate("Window", "物種清單資料表"))
        self.butBlist.setToolTip(_translate("Window", "<html><head/><body><p>選擇物種清單的資料表，這個資料表為 csv 檔案，以 UTF-8 編碼。</p></body></html>"))
        self.butBlist.setText(_translate("Window", "選擇檔案"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBatch), _translate("Window", "資料庫管理"))
        self.butSelectTempFile.setToolTip(_translate("Window", "<html><head/><body><p>選擇暫存的物種中名暫存檔，未來可重複載入此檔案批次產生名錄</p></body></html>"))
        self.butSelectTempFile.setText(_translate("Window", "選擇檔案"))
        self.comboDBselect.setItemText(0, _translate("Window", "臺灣維管束植物名錄(APG III)"))
        self.comboDBselect.setItemText(1, _translate("Window", "臺灣維管束植物名錄(Flora of Taiwan 2nd Edition)"))
        self.comboDBselect.setItemText(2, _translate("Window", "臺灣鳥類名錄(2014)"))
        self.label_2.setText(_translate("Window", "輸出名錄檔案"))
        self.butSelectOutput.setToolTip(_translate("Window", "<html><head/><body><p>選擇輸出的名錄檔案，會依照附檔名輸出相對應的格式。</p><p>目前支援的格式有：Microsoft Word 2007 (.docx), Open document format (.odt), markdown (.md) 等</p></body></html>"))
        self.butSelectOutput.setText(_translate("Window", "選擇檔案"))
        self.butUpdateDB.setToolTip(_translate("Window", "<html><head/><body><p>更新名錄資料庫(需連上網路)</p></body></html>"))
        self.butUpdateDB.setText(_translate("Window", "更新資料庫"))
        self.label_3.setText(_translate("Window", "載入資料庫"))
        self.label_6.setText(_translate("Window", "物種中名暫存檔"))
        self.butSlist.setText(_translate("Window", "選擇檔案"))
        self.label_4.setText(_translate("Window", "載入物種中名批次處理"))
