# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 643)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 654, 374))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineSpecies = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineSpecies.sizePolicy().hasHeightForWidth())
        self.lineSpecies.setSizePolicy(sizePolicy)
        self.lineSpecies.setBaseSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setItalic(False)
        self.lineSpecies.setFont(font)
        self.lineSpecies.setAutoFillBackground(False)
        self.lineSpecies.setObjectName("lineSpecies")
        self.gridLayout_2.addWidget(self.lineSpecies, 1, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.treeWidget.setMouseTracking(False)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropOverwriteMode(False)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.treeWidget.setDefaultDropAction(QtCore.Qt.TargetMoveAction)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setIndentation(10)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setWordWrap(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(60)
        self.treeWidget.header().setHighlightSections(True)
        self.treeWidget.header().setMinimumSectionSize(5)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.gridLayout_2.addWidget(self.treeWidget, 3, 0, 1, 2)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setToolTipsVisible(True)
        self.menuHelp.setObjectName("menuHelp")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuDatabases = QtWidgets.QMenu(self.menubar)
        self.menuDatabases.setObjectName("menuDatabases")
        self.menuPlants = QtWidgets.QMenu(self.menuDatabases)
        self.menuPlants.setObjectName("menuPlants")
        MainWindow.setMenuBar(self.menubar)
        self.toolBarEdit = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.toolBarEdit.sizePolicy().hasHeightForWidth())
        self.toolBarEdit.setSizePolicy(sizePolicy)
        self.toolBarEdit.setMouseTracking(False)
        self.toolBarEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.toolBarEdit.setStyleSheet("QToolBar{spacing: 0px;}")
        self.toolBarEdit.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBarEdit.setIconSize(QtCore.QSize(40, 40))
        self.toolBarEdit.setFloatable(True)
        self.toolBarEdit.setObjectName("toolBarEdit")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarEdit)
        self.toolBarSearch = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBarSearch.sizePolicy().hasHeightForWidth())
        self.toolBarSearch.setSizePolicy(sizePolicy)
        self.toolBarSearch.setAutoFillBackground(True)
        self.toolBarSearch.setStyleSheet("QToolBar_2{spacing: 0px;}")
        self.toolBarSearch.setIconSize(QtCore.QSize(40, 40))
        self.toolBarSearch.setObjectName("toolBarSearch")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarSearch)
        self.dockWidgetTaxonInfo = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetTaxonInfo.setFloating(False)
        self.dockWidgetTaxonInfo.setObjectName("dockWidgetTaxonInfo")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.taxonInfoScrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taxonInfoScrollArea.sizePolicy().hasHeightForWidth())
        self.taxonInfoScrollArea.setSizePolicy(sizePolicy)
        self.taxonInfoScrollArea.setMinimumSize(QtCore.QSize(0, 100))
        self.taxonInfoScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.taxonInfoScrollArea.setWidgetResizable(True)
        self.taxonInfoScrollArea.setObjectName("taxonInfoScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 654, 103))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.textBrowserInfo = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowserInfo.sizePolicy().hasHeightForWidth())
        self.textBrowserInfo.setSizePolicy(sizePolicy)
        self.textBrowserInfo.setMinimumSize(QtCore.QSize(0, 50))
        self.textBrowserInfo.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowserInfo.setOpenExternalLinks(True)
        self.textBrowserInfo.setObjectName("textBrowserInfo")
        self.gridLayout_10.addWidget(self.textBrowserInfo, 0, 0, 1, 1)
        self.taxonInfoScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.addWidget(self.taxonInfoScrollArea, 0, 0, 1, 1)
        self.dockWidgetTaxonInfo.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetTaxonInfo)
        self.actionSelectExport = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectExport.setIcon(icon)
        self.actionSelectExport.setIconVisibleInMenu(False)
        self.actionSelectExport.setObjectName("actionSelectExport")
        self.actionBatch = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/batch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBatch.setIcon(icon1)
        self.actionBatch.setIconVisibleInMenu(False)
        self.actionBatch.setObjectName("actionBatch")
        self.actionDeleteSel = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteSel.setIcon(icon2)
        self.actionDeleteSel.setIconVisibleInMenu(False)
        self.actionDeleteSel.setObjectName("actionDeleteSel")
        self.actionDeleteAll = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/delete_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteAll.setIcon(icon3)
        self.actionDeleteAll.setIconVisibleInMenu(False)
        self.actionDeleteAll.setObjectName("actionDeleteAll")
        self.actionClearSp = QtWidgets.QAction(MainWindow)
        self.actionClearSp.setObjectName("actionClearSp")
        self.actionHomepage = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHomepage.setIcon(icon4)
        self.actionHomepage.setIconVisibleInMenu(False)
        self.actionHomepage.setObjectName("actionHomepage")
        self.actionReportIssues = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/bug_report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReportIssues.setIcon(icon5)
        self.actionReportIssues.setIconVisibleInMenu(False)
        self.actionReportIssues.setObjectName("actionReportIssues")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setIconVisibleInMenu(False)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setCheckable(False)
        self.actionMinimize.setChecked(False)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionZoom = QtWidgets.QAction(MainWindow)
        self.actionZoom.setObjectName("actionZoom")
        self.actionMaximize = QtWidgets.QAction(MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionTropicos = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/tropicos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTropicos.setIcon(icon6)
        self.actionTropicos.setIconVisibleInMenu(False)
        self.actionTropicos.setObjectName("actionTropicos")
        self.actionSaveTxt = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/save_txt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveTxt.setIcon(icon7)
        self.actionSaveTxt.setIconVisibleInMenu(False)
        self.actionSaveTxt.setObjectName("actionSaveTxt")
        self.actionExportChecklist = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/execute_export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportChecklist.setIcon(icon8)
        self.actionExportChecklist.setIconVisibleInMenu(False)
        self.actionExportChecklist.setObjectName("actionExportChecklist")
        self.actionNomenMatch = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/nomenmatch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNomenMatch.setIcon(icon9)
        self.actionNomenMatch.setObjectName("actionNomenMatch")
        self.actionAddSpecies = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/addspecies_32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddSpecies.setIcon(icon10)
        self.actionAddSpecies.setIconVisibleInMenu(False)
        self.actionAddSpecies.setObjectName("actionAddSpecies")
        self.actionShowToolbarText = QtWidgets.QAction(MainWindow)
        self.actionShowToolbarText.setCheckable(True)
        self.actionShowToolbarText.setObjectName("actionShowToolbarText")
        self.actionDeselectAll = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/deselect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeselectAll.setIcon(icon11)
        self.actionDeselectAll.setIconVisibleInMenu(False)
        self.actionDeselectAll.setObjectName("actionDeselectAll")
        self.actionSelectAll = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/select_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectAll.setIcon(icon12)
        self.actionSelectAll.setIconVisibleInMenu(False)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionSelect_export_file = QtWidgets.QAction(MainWindow)
        self.actionSelect_export_file.setObjectName("actionSelect_export_file")
        self.actionMerge = QtWidgets.QAction(MainWindow)
        self.actionMerge.setObjectName("actionMerge")
        self.actionCompare = QtWidgets.QAction(MainWindow)
        self.actionCompare.setObjectName("actionCompare")
        self.actionCombine = QtWidgets.QAction(MainWindow)
        self.actionCombine.setObjectName("actionCombine")
        self.actionFormat = QtWidgets.QAction(MainWindow)
        self.actionFormat.setObjectName("actionFormat")
        self.actionTaiwanVascularPlants = QtWidgets.QAction(MainWindow)
        self.actionTaiwanVascularPlants.setCheckable(True)
        self.actionTaiwanVascularPlants.setChecked(True)
        self.actionTaiwanVascularPlants.setObjectName("actionTaiwanVascularPlants")
        self.actionTaiwanFlora = QtWidgets.QAction(MainWindow)
        self.actionTaiwanFlora.setCheckable(True)
        self.actionTaiwanFlora.setObjectName("actionTaiwanFlora")
        self.actionJapanYlist = QtWidgets.QAction(MainWindow)
        self.actionJapanYlist.setCheckable(True)
        self.actionJapanYlist.setObjectName("actionJapanYlist")
        self.actionNewProject = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewProject.setIcon(icon13)
        self.actionNewProject.setIconVisibleInMenu(False)
        self.actionNewProject.setObjectName("actionNewProject")
        self.actionShowTaxonInfo = QtWidgets.QAction(MainWindow)
        self.actionShowTaxonInfo.setCheckable(True)
        self.actionShowTaxonInfo.setChecked(True)
        self.actionShowTaxonInfo.setObjectName("actionShowTaxonInfo")
        self.actionShowEdit = QtWidgets.QAction(MainWindow)
        self.actionShowEdit.setCheckable(True)
        self.actionShowEdit.setChecked(True)
        self.actionShowEdit.setObjectName("actionShowEdit")
        self.actionShowSearch = QtWidgets.QAction(MainWindow)
        self.actionShowSearch.setCheckable(True)
        self.actionShowSearch.setChecked(True)
        self.actionShowSearch.setObjectName("actionShowSearch")
        self.actionUpdateDB = QtWidgets.QAction(MainWindow)
        self.actionUpdateDB.setObjectName("actionUpdateDB")
        self.actionDatabaseInfo = QtWidgets.QAction(MainWindow)
        self.actionDatabaseInfo.setObjectName("actionDatabaseInfo")
        self.menuFile.addAction(self.actionNewProject)
        self.menuFile.addAction(self.actionSelectExport)
        self.menuFile.addAction(self.actionBatch)
        self.menuFile.addAction(self.actionSaveTxt)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExportChecklist)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionAddSpecies)
        self.menuEdit.addAction(self.actionClearSp)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDeleteSel)
        self.menuEdit.addAction(self.actionDeleteAll)
        self.menuEdit.addAction(self.actionDeselectAll)
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHomepage)
        self.menuHelp.addAction(self.actionReportIssues)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionMaximize)
        self.menuWindow.addAction(self.actionZoom)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionShowTaxonInfo)
        self.menuWindow.addAction(self.actionShowEdit)
        self.menuWindow.addAction(self.actionShowSearch)
        self.menuView.addAction(self.actionShowToolbarText)
        self.menuTool.addAction(self.actionMerge)
        self.menuTool.addAction(self.actionCompare)
        self.menuTool.addAction(self.actionCombine)
        self.menuTool.addSeparator()
        self.menuTool.addAction(self.actionFormat)
        self.menuPlants.addAction(self.actionTaiwanVascularPlants)
        self.menuPlants.addAction(self.actionTaiwanFlora)
        self.menuPlants.addAction(self.actionJapanYlist)
        self.menuDatabases.addAction(self.menuPlants.menuAction())
        self.menuDatabases.addSeparator()
        self.menuDatabases.addAction(self.actionDatabaseInfo)
        self.menuDatabases.addAction(self.actionUpdateDB)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuDatabases.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBarEdit.addAction(self.actionNewProject)
        self.toolBarEdit.addAction(self.actionSaveTxt)
        self.toolBarEdit.addAction(self.actionSelectExport)
        self.toolBarEdit.addAction(self.actionBatch)
        self.toolBarEdit.addAction(self.actionExportChecklist)
        self.toolBarEdit.addSeparator()
        self.toolBarEdit.addAction(self.actionAddSpecies)
        self.toolBarEdit.addAction(self.actionDeleteSel)
        self.toolBarEdit.addAction(self.actionDeleteAll)
        self.toolBarEdit.addAction(self.actionSelectAll)
        self.toolBarEdit.addAction(self.actionDeselectAll)
        self.toolBarSearch.addAction(self.actionTropicos)
        self.toolBarSearch.addAction(self.actionNomenMatch)
        self.toolBarSearch.addSeparator()
        self.toolBarSearch.addAction(self.actionHomepage)
        self.toolBarSearch.addAction(self.actionReportIssues)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "checklister: a species checklist generator"))
        self.lineSpecies.setToolTip(_translate("MainWindow", "<html><head/><body><p>Input species name. Type part of common names/epithets/family to list similar names. </p><p>You can press enter or return to add it to the checklist.</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Common name/scientific name/family"))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Family"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "FullNameWithAuthors"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Common name"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuWindow.setTitle(_translate("MainWindow", "&Window"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTool.setTitle(_translate("MainWindow", "Tool"))
        self.menuDatabases.setTitle(_translate("MainWindow", "Databases"))
        self.menuPlants.setTitle(_translate("MainWindow", "Plants"))
        self.toolBarEdit.setWindowTitle(_translate("MainWindow", "Edit Toolbar"))
        self.toolBarSearch.setWindowTitle(_translate("MainWindow", "Search Toolbar"))
        self.dockWidgetTaxonInfo.setWindowTitle(_translate("MainWindow", "Taxon Info"))
        self.actionSelectExport.setText(_translate("MainWindow", "Select export file"))
        self.actionSelectExport.setIconText(_translate("MainWindow", "Select export file"))
        self.actionSelectExport.setToolTip(_translate("MainWindow", "Select export File"))
        self.actionSelectExport.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionBatch.setText(_translate("MainWindow", "Select batch export file"))
        self.actionBatch.setIconText(_translate("MainWindow", "Batch export"))
        self.actionBatch.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionDeleteSel.setText(_translate("MainWindow", "Delete selected"))
        self.actionDeleteSel.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionDeleteAll.setText(_translate("MainWindow", "Delete all"))
        self.actionDeleteAll.setShortcut(_translate("MainWindow", "Ctrl+Shift+D"))
        self.actionClearSp.setText(_translate("MainWindow", "Clear taxa"))
        self.actionClearSp.setShortcut(_translate("MainWindow", "Esc"))
        self.actionHomepage.setText(_translate("MainWindow", "Homepage"))
        self.actionHomepage.setShortcut(_translate("MainWindow", "Ctrl+Shift+H"))
        self.actionReportIssues.setText(_translate("MainWindow", "Report issues"))
        self.actionReportIssues.setToolTip(_translate("MainWindow", "Bug report"))
        self.actionReportIssues.setShortcut(_translate("MainWindow", "Ctrl+Shift+R"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionMinimize.setIconText(_translate("MainWindow", "Minimize window"))
        self.actionMinimize.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionZoom.setText(_translate("MainWindow", "Zoom"))
        self.actionZoom.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionMaximize.setShortcut(_translate("MainWindow", "Ctrl+Shift+M"))
        self.actionTropicos.setText(_translate("MainWindow", "Search Tropicos"))
        self.actionTropicos.setToolTip(_translate("MainWindow", "Search Tropicos database"))
        self.actionTropicos.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionSaveTxt.setText(_translate("MainWindow", "&Save species txtfile"))
        self.actionSaveTxt.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExportChecklist.setText(_translate("MainWindow", "Export checklist!"))
        self.actionExportChecklist.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionNomenMatch.setText(_translate("MainWindow", "Search NomenMatch"))
        self.actionNomenMatch.setToolTip(_translate("MainWindow", "Search NomenMatch database"))
        self.actionNomenMatch.setShortcut(_translate("MainWindow", "Ctrl+J"))
        self.actionAddSpecies.setText(_translate("MainWindow", "Add taxa"))
        self.actionAddSpecies.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.actionShowToolbarText.setText(_translate("MainWindow", "Show toolbar text"))
        self.actionShowToolbarText.setShortcut(_translate("MainWindow", "Ctrl+Shift+T"))
        self.actionDeselectAll.setText(_translate("MainWindow", "Deselect all species"))
        self.actionDeselectAll.setToolTip(_translate("MainWindow", "Deselect all taxa"))
        self.actionDeselectAll.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionSelectAll.setText(_translate("MainWindow", "Select all taxa"))
        self.actionSelectAll.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionSelect_export_file.setText(_translate("MainWindow", "Select export file"))
        self.actionMerge.setText(_translate("MainWindow", "Merge checklists"))
        self.actionMerge.setShortcut(_translate("MainWindow", "Ctrl+Shift+G"))
        self.actionCompare.setText(_translate("MainWindow", "Compare checklists"))
        self.actionCompare.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionCombine.setText(_translate("MainWindow", "Combine checklists"))
        self.actionCombine.setShortcut(_translate("MainWindow", "Ctrl+Shift+B"))
        self.actionFormat.setText(_translate("MainWindow", "Format scientific names (beta version)"))
        self.actionFormat.setShortcut(_translate("MainWindow", "Ctrl+Shift+F"))
        self.actionTaiwanVascularPlants.setText(_translate("MainWindow", "Taiwan: Vascular plants"))
        self.actionTaiwanFlora.setText(_translate("MainWindow", "Taiwan: Vascular plants (Flora of Taiwan)"))
        self.actionJapanYlist.setText(_translate("MainWindow", "Japan: Ylist"))
        self.actionNewProject.setText(_translate("MainWindow", "New project"))
        self.actionNewProject.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionShowTaxonInfo.setText(_translate("MainWindow", "Taxon info widget"))
        self.actionShowEdit.setText(_translate("MainWindow", "Edit toolbar"))
        self.actionShowSearch.setText(_translate("MainWindow", "Search toolbar"))
        self.actionUpdateDB.setText(_translate("MainWindow", "Update database"))
        self.actionDatabaseInfo.setText(_translate("MainWindow", "Database info"))

import iconResources_rc
