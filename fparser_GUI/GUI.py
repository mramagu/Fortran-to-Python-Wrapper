# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pablo\Documentos_1\MUSE\PRIMER_CURSO\AMPLIACION_DE_MATEMATICAS_I\VS_P2\fparser\fparser\fparser_GUI/GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\pablo\\Documentos_1\\MUSE\\PRIMER_CURSO\\AMPLIACION_DE_MATEMATICAS_I\\VS_P2\\fparser\\fparser\\fparser_GUI\\Arrow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\pablo\\Documentos_1\\MUSE\\PRIMER_CURSO\\AMPLIACION_DE_MATEMATICAS_I\\VS_P2\\fparser\\fparser\\fparser_GUI\\Arrow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\pablo\\Documentos_1\\MUSE\\PRIMER_CURSO\\AMPLIACION_DE_MATEMATICAS_I\\VS_P2\\fparser\\fparser\\fparser_GUI\\Arrow.jpg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\pablo\\Documentos_1\\MUSE\\PRIMER_CURSO\\AMPLIACION_DE_MATEMATICAS_I\\VS_P2\\fparser\\fparser\\fparser_GUI\\Arrow_selected.jpg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\pablo\\Documentos_1\\MUSE\\PRIMER_CURSO\\AMPLIACION_DE_MATEMATICAS_I\\VS_P2\\fparser\\fparser\\fparser_GUI\\Arrow.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\pablo\\Documentos_1\\MUSE\\PRIMER_CURSO\\AMPLIACION_DE_MATEMATICAS_I\\VS_P2\\fparser\\fparser\\fparser_GUI\\Arrow.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.toolButton_arrow.setIcon(icon)
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
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_fparserfiles = QtWidgets.QLabel(self.tab_fconfig)
        self.label_fparserfiles.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fparserfiles.setObjectName("label_fparserfiles")
        self.verticalLayout.addWidget(self.label_fparserfiles)
        self.treeWidget_fparserfiles = QtWidgets.QTreeWidget(self.tab_fconfig)
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
        self.treeWidget_fsummary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.treeWidget_fsummary.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeWidget_fsummary.setLineWidth(1)
        self.treeWidget_fsummary.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget_fsummary.setAnimated(True)
        self.treeWidget_fsummary.setWordWrap(False)
        self.treeWidget_fsummary.setObjectName("treeWidget_fsummary")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_fsummary)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_fsummary)
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
        self.horizontalLayout_4.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_make_OS = QtWidgets.QLabel(self.tab_makefile)
        self.label_make_OS.setAlignment(QtCore.Qt.AlignCenter)
        self.label_make_OS.setObjectName("label_make_OS")
        self.horizontalLayout_4.addWidget(self.label_make_OS)
        self.comboBox_make = QtWidgets.QComboBox(self.tab_makefile)
        self.comboBox_make.setEditable(False)
        self.comboBox_make.setObjectName("comboBox_make")
        self.comboBox_make.addItem("")
        self.comboBox_make.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_make)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_make_env = QtWidgets.QLabel(self.tab_makefile)
        self.label_make_env.setObjectName("label_make_env")
        self.horizontalLayout_5.addWidget(self.label_make_env)
        self.radioButton = QtWidgets.QRadioButton(self.tab_makefile)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_makefile)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_make_FC = QtWidgets.QLabel(self.tab_makefile)
        self.label_make_FC.setObjectName("label_make_FC")
        self.horizontalLayout_6.addWidget(self.label_make_FC)
        self.comboBox = QtWidgets.QComboBox(self.tab_makefile)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_6.addWidget(self.comboBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.pushButton_make1 = QtWidgets.QPushButton(self.tab_makefile)
        self.pushButton_make1.setDefault(False)
        self.pushButton_make1.setObjectName("pushButton_make1")
        self.verticalLayout_8.addWidget(self.pushButton_make1)
        self.tabWidget.addTab(self.tab_makefile, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Files = QtWidgets.QAction(MainWindow)
        self.actionOpen_Files.setObjectName("actionOpen_Files")
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.menuFile.addAction(self.actionOpen_Files)
        self.menuFile.addAction(self.actionOpen_Directory)
        self.menuFile.addAction(self.actionClear)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_ffiles.setText(_translate("MainWindow", "Fortran files"))
        self.treeWidget_ffiles.headerItem().setText(0, _translate("MainWindow", "Main directory"))
        self.label_select.setText(_translate("MainWindow", "Select Fortran files"))
        self.label_selffiles.setText(_translate("MainWindow", "Selected Fortran files"))
        self.pushButton_fparser.setText(_translate("MainWindow", "Run Fortran parser"))
        self.label_fparserfiles.setText(_translate("MainWindow", "Converted Fortran files"))
        self.treeWidget_fparserfiles.headerItem().setText(0, _translate("MainWindow", "Main directory"))
        self.label_fsummary.setText(_translate("MainWindow", "Fortran parser summary"))
        self.treeWidget_fsummary.headerItem().setText(0, _translate("MainWindow", "Fortran modules"))
        __sortingEnabled = self.treeWidget_fsummary.isSortingEnabled()
        self.treeWidget_fsummary.setSortingEnabled(False)
        self.treeWidget_fsummary.topLevelItem(0).setText(0, _translate("MainWindow", "Module 1"))
        self.treeWidget_fsummary.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Subroutines"))
        self.treeWidget_fsummary.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "Sub1"))
        self.treeWidget_fsummary.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Functions"))
        self.treeWidget_fsummary.topLevelItem(0).child(1).child(0).setText(0, _translate("MainWindow", "Fun1"))
        self.treeWidget_fsummary.topLevelItem(1).setText(0, _translate("MainWindow", "Module2"))
        self.treeWidget_fsummary.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fconfig), _translate("MainWindow", "Fortran files"))
        self.label_make_OS.setText(_translate("MainWindow", "Seleccione su sistema operativo."))
        self.comboBox_make.setItemText(0, _translate("MainWindow", "Windows"))
        self.comboBox_make.setItemText(1, _translate("MainWindow", "Linux"))
        self.label_make_env.setText(_translate("MainWindow", "Seleccione el entorno de Pyhton en el que desea trabajar."))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.label_make_FC.setText(_translate("MainWindow", "Seleccione su compilador de Fortran."))
        self.pushButton_make1.setText(_translate("MainWindow", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_makefile), _translate("MainWindow", "Makefile"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Files.setText(_translate("MainWindow", "Open Files"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Folder"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
