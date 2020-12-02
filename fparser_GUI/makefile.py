from PyQt5 import QtCore, QtGui, QtWidgets

def selectOS(ui):
    OperatingSystem=ui.comboBox_make.currentText()
    print(OperatingSystem)

def fcompiler(ui):
    pass
"""
    def f(ui,mf):
        mf.os=ui.combobox.currentText()
    class Makefile():
        def __init__(self):
            self.os=''
            self.compiler=''
"""