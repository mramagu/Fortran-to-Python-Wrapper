import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets


class Makefile():
    def __init__(self,self_fparser):
        self.ui=self_fparser.ui
        self.self_fparser=self_fparser
        self.os=''
        self.condaEnv=''
        self.env=''
        self.FC=''

    def selectOS(self):
        self.os=self.ui.comboBox_makeOS.currentText()
        print(self.os)

    def select_condaEnv(self):
        if self.ui.radioButton_makeYes.isChecked() == True:
            self.condaEnv=self.ui.radioButton_makeYes.text()
            print(self.condaEnv)
        elif self.ui.radioButton_makeNo.isChecked() == True:
            self.condaEnv=self.ui.radioButton_makeNo.text()
            print(self.condaEnv)

    def writeEnv(self):
        self.env=self.ui.lineEdit_makeEnv.text()
        print(self.env)

    def fcompiler(self):
        if self.ui.comboBox_makeFC.currentIndex() == 0:
            self.FC='intelvem'
            print(self.FC)
        elif self.ui.comboBox_makeFC.currentIndex() == 1:
            self.FC='gfortran'
            print(self.FC)

    def searchFC(self):
        p=subprocess.run(['f2py','-c','--help-fcompiler'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.self_fparser.terminal_text.add_line(p.stdout.decode('utf-8'),number=2)

    def properties(self):
        self.selectOS()
        self.select_condaEnv()
        self.writeEnv()
        self.fcompiler()
    
    def runmake(self):
        pass
        #subprocess.run(['f2py','Hello_world.f90','-m','','-h','Interface.pyf','--overwrite-signature'])
        #flags=['--fcompiler='+self.FC ,'--f90flags=-O3','--f90flags=-Wno-conversion','--f90flags=-std=f95','--f90flags=/real-size:64' -L%library%]
        #subprocess.run(['f2py','-c','Interface.pyf','Hello_world.f90',flags])
    
"""
    def f(ui,mf):
        mf.os=ui.combobox.currentText()
    class Makefile():
        def __init__(self):
            self.os=''
            self.compiler=''
"""


if __name__ == "__main__":

    p=subprocess.run(['python','--version'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(p.stdout)


