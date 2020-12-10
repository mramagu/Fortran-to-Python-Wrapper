import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets


def selectOS(ui):
    OperatingSystem=ui.comboBox_makeOS.currentText()
    print(OperatingSystem)

def select_condaEnv(ui):
    if ui.radioButton_makeYes.isChecked() == True:
        condaEnv=ui.radioButton_makeYes.text()
        print(condaEnv)
    elif ui.radioButton_makeNo.isChecked() == True:
        condaEnv=ui.radioButton_makeNo.text()
        print(condaEnv)

def writeEnv(ui):
    Env=ui.lineEdit_makeEnv.text()
    print(Env)

def fcompiler(ui):
    FC=ui.comboBox_makeFC.currentText()
    print(FC)

def properties(ui):
    selectOS(ui)
    select_condaEnv(ui)
    writeEnv(ui)
    fcompiler(ui)
    
def runmake(ui):
    pass
    #subprocess.run(['f2py','Hello_world.f90','-m','','-h','Interface.pyf','--overwrite-signature'])
    #flags=['--fcompiler=' %fcompiler% ,'--f90flags=-O3','--f90flags=-Wno-conversion','--f90flags=-std=f95','--f90flags=/real-size:64' -L%library%]
    #subprocess.run(['f2py','-c','Interface.pyf','Hello_world.f90',flags,'&&','ECHO','SUCCESS'])
    
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

