import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets


class Makefile():
    def __init__(self,self_fparser):
        self.ui=self_fparser.ui
        self.self_fparser=self_fparser
        self.os=''
        self.precission=''
        self.lib=''
        self.FC=''
        self.f2py='f2py'
        
    def selectOS(self):
        self.os=self.ui.comboBox_makeOS.currentText()
        print(self.os)

    def select_precission(self):
        if self.ui.radioButton_makeSP.isChecked() == True:
            self.precission=self.ui.radioButton_makeSP.text()
            print(self.precission)
        elif self.ui.radioButton_makeDP.isChecked() == True:
            self.precission=self.ui.radioButton_makeDP.text()
            print(self.precission)

    def writeLib(self):
        self.lib=self.ui.lineEdit_makeFlib.text()
        print(self.lib)

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
        self.select_precission()
        self.writeLib()
        self.fcompiler()
    
    def runmake(self):
        run=[]

        if self.os=='Windows':
            self.f2py='f2py'
        else:
            self.f2py='f2py3'
        run.append(self.f2py)

        for file in self.self_fparser.files:
            run.append(file)

        run.append('-m')
        run.append(self.lib+'f')
        run.append('-h')
        run.append('Interface.pyf')
        run.append('--overwrite-signature')

        pyf=subprocess.run(run,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.self_fparser.terminal_text.add_line(pyf.stdout.decode('utf-8'))
        #flags=['--fcompiler='+self.FC ,'--f90flags=-O3','--f90flags=-Wno-conversion','--f90flags=-std=f95','--f90flags=/real-size:64','-L'+self.lib]
        #subprocess.run(['f2py','-c','Interface.pyf','Hello_world.f90',flags])



if __name__ == "__main__":

    p=subprocess.run(['python','--version'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(p.stdout)