# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/Documentos/Matemáticas_MUSE/fparser/fparser_GUI/Window_fmodules.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_fmod = QtWidgets.QLabel(self.centralwidget)
        self.label_fmod.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fmod.setObjectName("label_fmod")
        self.verticalLayout.addWidget(self.label_fmod)
        self.listWidget_fmod = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_fmod.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_fmod.setObjectName("listWidget_fmod")
        self.verticalLayout.addWidget(self.listWidget_fmod)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(30, 0, 30, 225)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_select = QtWidgets.QLabel(self.centralwidget)
        self.label_select.setAlignment(QtCore.Qt.AlignCenter)
        self.label_select.setObjectName("label_select")
        self.verticalLayout_6.addWidget(self.label_select)
        self.toolButton_arrow = QtWidgets.QToolButton(self.centralwidget)
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
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_selfmod = QtWidgets.QLabel(self.centralwidget)
        self.label_selfmod.setAlignment(QtCore.Qt.AlignCenter)
        self.label_selfmod.setObjectName("label_selfmod")
        self.verticalLayout_7.addWidget(self.label_selfmod)
        self.listWidget_selfmod = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_selfmod.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_selfmod.setObjectName("listWidget_selfmod")
        self.verticalLayout_7.addWidget(self.listWidget_selfmod)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.buttonBox_accept = QtWidgets.QDialogButtonBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox_accept.sizePolicy().hasHeightForWidth())
        self.buttonBox_accept.setSizePolicy(sizePolicy)
        self.buttonBox_accept.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_accept.setCenterButtons(True)
        self.buttonBox_accept.setObjectName("buttonBox_accept")
        self.horizontalLayout.addWidget(self.buttonBox_accept)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_fmod.setText(_translate("MainWindow", "Fortran modules"))
        self.label_select.setText(_translate("MainWindow", "Select Fortran modules"))
        self.label_selfmod.setText(_translate("MainWindow", "Selected Fortran modules"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
