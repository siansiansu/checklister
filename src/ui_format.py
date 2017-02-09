# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_format.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormatDialog(object):
    def setupUi(self, FormatDialog):
        FormatDialog.setObjectName("FormatDialog")
        FormatDialog.resize(566, 246)
        self.gridLayout = QtWidgets.QGridLayout(FormatDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(FormatDialog)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 542, 222))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(325, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 6)
        self.butClose = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.butClose.setObjectName("butClose")
        self.gridLayout_2.addWidget(self.butClose, 6, 2, 1, 3)
        self.butSelectExcel = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.butSelectExcel.setObjectName("butSelectExcel")
        self.gridLayout_2.addWidget(self.butSelectExcel, 1, 3, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.butFormatName = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butFormatName.sizePolicy().hasHeightForWidth())
        self.butFormatName.setSizePolicy(sizePolicy)
        self.butFormatName.setDefault(True)
        self.butFormatName.setObjectName("butFormatName")
        self.gridLayout_2.addWidget(self.butFormatName, 6, 5, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineExcelFilePath = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineExcelFilePath.setText("")
        self.lineExcelFilePath.setObjectName("lineExcelFilePath")
        self.gridLayout_2.addWidget(self.lineExcelFilePath, 1, 1, 1, 1)
        self.labelColNumber = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelColNumber.sizePolicy().hasHeightForWidth())
        self.labelColNumber.setSizePolicy(sizePolicy)
        self.labelColNumber.setObjectName("labelColNumber")
        self.gridLayout_2.addWidget(self.labelColNumber, 4, 0, 1, 2)
        self.lineExcelColnum = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineExcelColnum.sizePolicy().hasHeightForWidth())
        self.lineExcelColnum.setSizePolicy(sizePolicy)
        self.lineExcelColnum.setObjectName("lineExcelColnum")
        self.gridLayout_2.addWidget(self.lineExcelColnum, 4, 4, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(FormatDialog)
        QtCore.QMetaObject.connectSlotsByName(FormatDialog)

    def retranslateUi(self, FormatDialog):
        _translate = QtCore.QCoreApplication.translate
        FormatDialog.setWindowTitle(_translate("FormatDialog", "Formating scientific names"))
        self.butClose.setToolTip(_translate("FormatDialog", "<html><head/><body><p>Select export checklist file. Supported file formats: Microsoft Word 2007 (.docx), Open document format (.odt), markdown (.md). Default is docx and markdown.</p></body></html>"))
        self.butClose.setText(_translate("FormatDialog", "Close"))
        self.butSelectExcel.setToolTip(_translate("FormatDialog", "<html><head/><body><p>Select export checklist file. Supported file formats: Microsoft Word 2007 (.docx), Open document format (.odt), markdown (.md). Default is docx and markdown.</p></body></html>"))
        self.butSelectExcel.setText(_translate("FormatDialog", "Select file ..."))
        self.label_2.setText(_translate("FormatDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Options</span></p></body></html>"))
        self.butFormatName.setText(_translate("FormatDialog", "Format"))
        self.checkBox.setText(_translate("FormatDialog", "with header"))
        self.label.setText(_translate("FormatDialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Formating scientific names in Excel</span></p></body></html>"))
        self.label_3.setText(_translate("FormatDialog", "Excel file"))
        self.labelColNumber.setText(_translate("FormatDialog", "Column number of scientific names"))
        self.lineExcelColnum.setText(_translate("FormatDialog", "1"))
