# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/Documentos/Matemáticas_MUSE/fparser/fparser_GUI/Options.ui'
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
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_fformat = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_fformat.sizePolicy().hasHeightForWidth())
        self.label_fformat.setSizePolicy(sizePolicy)
        self.label_fformat.setBaseSize(QtCore.QSize(0, 0))
        self.label_fformat.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_fformat.setObjectName("label_fformat")
        self.verticalLayout.addWidget(self.label_fformat)
        self.lineEdit_fformat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fformat.setObjectName("lineEdit_fformat")
        self.verticalLayout.addWidget(self.lineEdit_fformat)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_fcomments = QtWidgets.QLabel(self.centralwidget)
        self.label_fcomments.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_fcomments.setObjectName("label_fcomments")
        self.verticalLayout_2.addWidget(self.label_fcomments)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_fcommentsBefore = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_fcommentsBefore.setChecked(True)
        self.radioButton_fcommentsBefore.setObjectName("radioButton_fcommentsBefore")
        self.verticalLayout_3.addWidget(self.radioButton_fcommentsBefore)
        self.radioButton_fcommentsAfter = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_fcommentsAfter.setObjectName("radioButton_fcommentsAfter")
        self.verticalLayout_3.addWidget(self.radioButton_fcommentsAfter)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_terminal = QtWidgets.QLabel(self.centralwidget)
        self.label_terminal.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_terminal.setObjectName("label_terminal")
        self.verticalLayout_5.addWidget(self.label_terminal)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_terminalYes = QtWidgets.QRadioButton(self.widget)
        self.radioButton_terminalYes.setObjectName("radioButton_terminalYes")
        self.verticalLayout_4.addWidget(self.radioButton_terminalYes)
        self.radioButton_terminalNo = QtWidgets.QRadioButton(self.widget)
        self.radioButton_terminalNo.setChecked(True)
        self.radioButton_terminalNo.setObjectName("radioButton_terminalNo")
        self.verticalLayout_4.addWidget(self.radioButton_terminalNo)
        self.verticalLayout_5.addWidget(self.widget)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem2)
        self.buttonBox_accept = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox_accept.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_accept.setCenterButtons(True)
        self.buttonBox_accept.setObjectName("buttonBox_accept")
        self.verticalLayout_6.addWidget(self.buttonBox_accept)
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
        self.label_fformat.setText(_translate("MainWindow", "Available fortran files format"))
        self.lineEdit_fformat.setText(_translate("MainWindow", "*.f90, *.f"))
        self.label_fcomments.setText(_translate("MainWindow", "Position of fortran comments"))
        self.radioButton_fcommentsBefore.setText(_translate("MainWindow", "At the beginning of the file"))
        self.radioButton_fcommentsAfter.setText(_translate("MainWindow", "At the end of the file"))
        self.label_terminal.setText(_translate("MainWindow", "Show terminal"))
        self.radioButton_terminalYes.setText(_translate("MainWindow", "yes"))
        self.radioButton_terminalNo.setText(_translate("MainWindow", "no"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

