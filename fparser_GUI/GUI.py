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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_fconfig = QtWidgets.QWidget()
        self.tab_fconfig.setObjectName("tab_fconfig")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_fconfig)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_dir = QtWidgets.QLabel(self.tab_fconfig)
        self.label_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dir.setObjectName("label_dir")
        self.verticalLayout_2.addWidget(self.label_dir)
        self.plainTextEdit_dir = QtWidgets.QPlainTextEdit(self.tab_fconfig)
        self.plainTextEdit_dir.setObjectName("plainTextEdit_dir")
        self.verticalLayout_2.addWidget(self.plainTextEdit_dir)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.listWidget_ffiles = QtWidgets.QListWidget(self.tab_fconfig)
        self.listWidget_ffiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_ffiles.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_ffiles.setObjectName("listWidget_ffiles")
        self.gridLayout_2.addWidget(self.listWidget_ffiles, 0, 1, 2, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ffiles = QtWidgets.QLabel(self.tab_fconfig)
        self.label_ffiles.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ffiles.setObjectName("label_ffiles")
        self.verticalLayout_3.addWidget(self.label_ffiles)
        self.plainTextEdit_ffiles = QtWidgets.QPlainTextEdit(self.tab_fconfig)
        self.plainTextEdit_ffiles.setObjectName("plainTextEdit_ffiles")
        self.verticalLayout_3.addWidget(self.plainTextEdit_ffiles)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_fconfig, "")
        self.tab_makefile = QtWidgets.QWidget()
        self.tab_makefile.setObjectName("tab_makefile")
        self.tabWidget.addTab(self.tab_makefile, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
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
        self.menuFile.addAction(self.actionOpen_Files)
        self.menuFile.addAction(self.actionOpen_Directory)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_dir.setText(_translate("MainWindow", "Directory"))
        self.label_ffiles.setText(_translate("MainWindow", "Fortran files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fconfig), _translate("MainWindow", "Fortran files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_makefile), _translate("MainWindow", "Makefile"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_Files.setText(_translate("MainWindow", "Open Files"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

