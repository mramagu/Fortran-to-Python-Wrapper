# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/Documentos/Matemáticas_MUSE/fparser/fparser_GUI/GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 836)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_fconfig = QtWidgets.QWidget()
        self.tab_fconfig.setObjectName("tab_fconfig")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_fconfig)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ffiles = QtWidgets.QLabel(self.tab_fconfig)
        self.label_ffiles.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ffiles.setObjectName("label_ffiles")
        self.verticalLayout_3.addWidget(self.label_ffiles)
        self.treeWidget_ffiles = QtWidgets.QTreeWidget(self.tab_fconfig)
        self.treeWidget_ffiles.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget_ffiles.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.treeWidget_ffiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget_ffiles.setAnimated(True)
        self.treeWidget_ffiles.setObjectName("treeWidget_ffiles")
        self.verticalLayout_3.addWidget(self.treeWidget_ffiles)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(30, 70, 30, 70)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_select = QtWidgets.QLabel(self.tab_fconfig)
        self.label_select.setAlignment(QtCore.Qt.AlignCenter)
        self.label_select.setObjectName("label_select")
        self.verticalLayout_6.addWidget(self.label_select)
        self.toolButton_arrow = QtWidgets.QToolButton(self.tab_fconfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_arrow.sizePolicy().hasHeightForWidth())
        self.toolButton_arrow.setSizePolicy(sizePolicy)
        self.toolButton_arrow.setText("")
        self.toolButton_arrow.setIconSize(QtCore.QSize(71, 51))
        self.toolButton_arrow.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_arrow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton_arrow.setAutoRaise(True)
        self.toolButton_arrow.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_arrow.setObjectName("toolButton_arrow")
        self.verticalLayout_6.addWidget(self.toolButton_arrow)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_selffiles = QtWidgets.QLabel(self.tab_fconfig)
        self.label_selffiles.setAlignment(QtCore.Qt.AlignCenter)
        self.label_selffiles.setObjectName("label_selffiles")
        self.verticalLayout_4.addWidget(self.label_selffiles)
        self.listWidget_selffiles = QtWidgets.QListWidget(self.tab_fconfig)
        self.listWidget_selffiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_selffiles.setObjectName("listWidget_selffiles")
        self.verticalLayout_4.addWidget(self.listWidget_selffiles)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(self.tab_fconfig)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_fparser = QtWidgets.QPushButton(self.frame)
        self.pushButton_fparser.setObjectName("pushButton_fparser")
        self.horizontalLayout.addWidget(self.pushButton_fparser)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_7.addWidget(self.frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_fparserfiles = QtWidgets.QLabel(self.tab_fconfig)
        self.label_fparserfiles.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fparserfiles.setObjectName("label_fparserfiles")
        self.verticalLayout.addWidget(self.label_fparserfiles)
        self.treeWidget_fparserfiles = QtWidgets.QTreeWidget(self.tab_fconfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_fparserfiles.sizePolicy().hasHeightForWidth())
        self.treeWidget_fparserfiles.setSizePolicy(sizePolicy)
        self.treeWidget_fparserfiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget_fparserfiles.setAnimated(True)
        self.treeWidget_fparserfiles.setObjectName("treeWidget_fparserfiles")
        self.verticalLayout.addWidget(self.treeWidget_fparserfiles)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_fsummary = QtWidgets.QLabel(self.tab_fconfig)
        self.label_fsummary.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fsummary.setObjectName("label_fsummary")
        self.verticalLayout_5.addWidget(self.label_fsummary)
        self.treeWidget_fsummary = QtWidgets.QTreeWidget(self.tab_fconfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_fsummary.sizePolicy().hasHeightForWidth())
        self.treeWidget_fsummary.setSizePolicy(sizePolicy)
        self.treeWidget_fsummary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.treeWidget_fsummary.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeWidget_fsummary.setLineWidth(1)
        self.treeWidget_fsummary.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget_fsummary.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget_fsummary.setAnimated(True)
        self.treeWidget_fsummary.setWordWrap(False)
        self.treeWidget_fsummary.setObjectName("treeWidget_fsummary")
        self.verticalLayout_5.addWidget(self.treeWidget_fsummary)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_fconfig, "")
        self.tab_makefile = QtWidgets.QWidget()
        self.tab_makefile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_makefile.setObjectName("tab_makefile")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_makefile)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_make_OS = QtWidgets.QLabel(self.tab_makefile)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_make_OS.setFont(font)
        self.label_make_OS.setObjectName("label_make_OS")
        self.verticalLayout_11.addWidget(self.label_make_OS)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.comboBox_makeOS = QtWidgets.QComboBox(self.tab_makefile)
        self.comboBox_makeOS.setEditable(False)
        self.comboBox_makeOS.setObjectName("comboBox_makeOS")
        self.comboBox_makeOS.addItem("")
        self.comboBox_makeOS.addItem("")
        self.verticalLayout_10.addWidget(self.comboBox_makeOS)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_make_precission = QtWidgets.QLabel(self.tab_makefile)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_make_precission.setFont(font)
        self.label_make_precission.setObjectName("label_make_precission")
        self.verticalLayout_16.addWidget(self.label_make_precission)
        self.horizontalLayout_9.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.radioButton_makeSP = QtWidgets.QRadioButton(self.tab_makefile)
        self.radioButton_makeSP.setChecked(True)
        self.radioButton_makeSP.setObjectName("radioButton_makeSP")
        self.verticalLayout_17.addWidget(self.radioButton_makeSP)
        self.radioButton_makeDP = QtWidgets.QRadioButton(self.tab_makefile)
        self.radioButton_makeDP.setObjectName("radioButton_makeDP")
        self.verticalLayout_17.addWidget(self.radioButton_makeDP)
        self.horizontalLayout_9.addLayout(self.verticalLayout_17)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_make_lib = QtWidgets.QLabel(self.tab_makefile)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.label_make_lib.setFont(font)
        self.label_make_lib.setObjectName("label_make_lib")
        self.verticalLayout_14.addWidget(self.label_make_lib)
        self.horizontalLayout_5.addLayout(self.verticalLayout_14)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lineEdit_makeFlib = QtWidgets.QLineEdit(self.tab_makefile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_makeFlib.sizePolicy().hasHeightForWidth())
        self.lineEdit_makeFlib.setSizePolicy(sizePolicy)
        self.lineEdit_makeFlib.setText("")
        self.lineEdit_makeFlib.setReadOnly(False)
        self.lineEdit_makeFlib.setObjectName("lineEdit_makeFlib")
        self.verticalLayout_13.addWidget(self.lineEdit_makeFlib)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_make_FC = QtWidgets.QLabel(self.tab_makefile)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_make_FC.setFont(font)
        self.label_make_FC.setObjectName("label_make_FC")
        self.verticalLayout_19.addWidget(self.label_make_FC)
        self.horizontalLayout_6.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.comboBox_makeFC = QtWidgets.QComboBox(self.tab_makefile)
        self.comboBox_makeFC.setObjectName("comboBox_makeFC")
        self.comboBox_makeFC.addItem("")
        self.comboBox_makeFC.addItem("")
        self.verticalLayout_20.addWidget(self.comboBox_makeFC)
        self.horizontalLayout_6.addLayout(self.verticalLayout_20)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_f2py = QtWidgets.QLabel(self.tab_makefile)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_f2py.setFont(font)
        self.label_f2py.setAutoFillBackground(False)
        self.label_f2py.setTextFormat(QtCore.Qt.AutoText)
        self.label_f2py.setScaledContents(False)
        self.label_f2py.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_f2py.setWordWrap(False)
        self.label_f2py.setObjectName("label_f2py")
        self.verticalLayout_12.addWidget(self.label_f2py)
        self.horizontalLayout_8.addLayout(self.verticalLayout_12)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_searchFC = QtWidgets.QPushButton(self.tab_makefile)
        self.pushButton_searchFC.setObjectName("pushButton_searchFC")
        self.verticalLayout_18.addWidget(self.pushButton_searchFC)
        self.horizontalLayout_8.addLayout(self.verticalLayout_18)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        spacerItem5 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_complib = QtWidgets.QLabel(self.tab_makefile)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_complib.setFont(font)
        self.label_complib.setObjectName("label_complib")
        self.verticalLayout_22.addWidget(self.label_complib)
        self.horizontalLayout_10.addLayout(self.verticalLayout_22)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_11.setContentsMargins(20, -1, 0, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_lib = QtWidgets.QLineEdit(self.tab_makefile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_lib.sizePolicy().hasHeightForWidth())
        self.lineEdit_lib.setSizePolicy(sizePolicy)
        self.lineEdit_lib.setObjectName("lineEdit_lib")
        self.horizontalLayout_11.addWidget(self.lineEdit_lib)
        self.toolButton_lib = QtWidgets.QToolButton(self.tab_makefile)
        self.toolButton_lib.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton_lib.setObjectName("toolButton_lib")
        self.horizontalLayout_11.addWidget(self.toolButton_lib)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_3 = QtWidgets.QFrame(self.tab_makefile)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_7.addWidget(self.line_3)
        self.pushButton_makeOK = QtWidgets.QPushButton(self.tab_makefile)
        self.pushButton_makeOK.setDefault(False)
        self.pushButton_makeOK.setObjectName("pushButton_makeOK")
        self.horizontalLayout_7.addWidget(self.pushButton_makeOK)
        self.line_4 = QtWidgets.QFrame(self.tab_makefile)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_7.addWidget(self.line_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab_makefile, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1076, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_terminal = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_terminal.setEnabled(True)
        self.dockWidget_terminal.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_terminal.setObjectName("dockWidget_terminal")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.plainTextEdit_terminal = QtWidgets.QPlainTextEdit(self.dockWidgetContents)
        self.plainTextEdit_terminal.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.plainTextEdit_terminal.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_terminal.setSizePolicy(sizePolicy)
        self.plainTextEdit_terminal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plainTextEdit_terminal.setSizeIncrement(QtCore.QSize(0, 0))
        self.plainTextEdit_terminal.setBaseSize(QtCore.QSize(0, 0))
        self.plainTextEdit_terminal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit_terminal.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit_terminal.setReadOnly(True)
        self.plainTextEdit_terminal.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit_terminal.setCenterOnScroll(False)
        self.plainTextEdit_terminal.setObjectName("plainTextEdit_terminal")
        self.verticalLayout_9.addWidget(self.plainTextEdit_terminal)
        self.dockWidget_terminal.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_terminal)
        self.actionOpen_Files = QtWidgets.QAction(MainWindow)
        self.actionOpen_Files.setObjectName("actionOpen_Files")
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.menuFile.addAction(self.actionOpen_Files)
        self.menuFile.addAction(self.actionOpen_Directory)
        self.menuFile.addAction(self.actionOptions)
        self.menuFile.addAction(self.actionClear)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fortran wrapper to Python library"))
        self.label_ffiles.setText(_translate("MainWindow", "Fortran files"))
        self.treeWidget_ffiles.headerItem().setText(0, _translate("MainWindow", "Main directory"))
        self.label_select.setText(_translate("MainWindow", "Select Fortran files"))
        self.label_selffiles.setText(_translate("MainWindow", "Selected Fortran files"))
        self.pushButton_fparser.setText(_translate("MainWindow", "Run Fortran parser"))
        self.label_fparserfiles.setText(_translate("MainWindow", "Converted Fortran files"))
        self.treeWidget_fparserfiles.headerItem().setText(0, _translate("MainWindow", "Main directory"))
        self.label_fsummary.setText(_translate("MainWindow", "Fortran parser summary"))
        self.treeWidget_fsummary.headerItem().setText(0, _translate("MainWindow", "Fortran modules"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fconfig), _translate("MainWindow", "Fortran files"))
        self.label_make_OS.setText(_translate("MainWindow", "Choose your operating system."))
        self.comboBox_makeOS.setItemText(0, _translate("MainWindow", "Windows"))
        self.comboBox_makeOS.setItemText(1, _translate("MainWindow", "Linux"))
        self.label_make_precission.setText(_translate("MainWindow", "Choose the precision you want to work with."))
        self.radioButton_makeSP.setText(_translate("MainWindow", "Simple precision."))
        self.radioButton_makeDP.setText(_translate("MainWindow", "Double precision."))
        self.label_make_lib.setText(_translate("MainWindow", "Write the name of the fortran library."))
        self.label_make_FC.setText(_translate("MainWindow", "Select your fortran compiler."))
        self.comboBox_makeFC.setItemText(0, _translate("MainWindow", "Intel Visual Fortran Compiler for 64-bit apps (intelvem)"))
        self.comboBox_makeFC.setItemText(1, _translate("MainWindow", "GNU Fortran 95 compiler (gfortran)"))
        self.label_f2py.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">NOTE:</span></p><p>You can execute &quot;f2py -c --help-fcompiler&quot; in your command window to see </p><p>which fortran compilers are available in your computer.</p></body></html>"))
        self.pushButton_searchFC.setText(_translate("MainWindow", "Search for fortran compilers"))
        self.label_complib.setText(_translate("MainWindow", "Select the compiler library (necessary if intel compiler is selected)."))
        self.toolButton_lib.setText(_translate("MainWindow", "..."))
        self.pushButton_makeOK.setText(_translate("MainWindow", "Run f2py"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_makefile), _translate("MainWindow", "Makefile"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.dockWidget_terminal.setWindowTitle(_translate("MainWindow", "Terminal"))
        self.actionOpen_Files.setText(_translate("MainWindow", "Open Files"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Folder"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

