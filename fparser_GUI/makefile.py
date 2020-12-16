import subprocess
import os
import sys
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
try:
    sys.path.insert(1, '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-1])+'/fparser')
    import fparser
except:
    sys.path.insert(1, '/'.join(os.path.dirname(os.path.abspath(__file__)).split('\\')[0:-1])+'/fparser')
    import fparser


class Makefile():
    def __init__(self,self_fparser):
        self.ui=self_fparser.ui
        self.self_fparser=self_fparser
        self.os=''
        self.precission=''
        self.lib=''
        self.FC=''
        self.complib=''
        self.f2py='f2py'
        
    def selectOS(self):
        self.os=self.ui.comboBox_makeOS.currentText()
        # print(self.os)

    def select_precission(self):
        if self.ui.radioButton_makeSP.isChecked() == True:
            self.precission=self.ui.radioButton_makeSP.text()
            # print(self.precission)
        elif self.ui.radioButton_makeDP.isChecked() == True:
            self.precission=self.ui.radioButton_makeDP.text()
            # print(self.precission)

    def writeLib(self):
        self.lib=self.ui.lineEdit_makeFlib.text()
        # print(self.lib)

    def fcompiler(self):
        if self.ui.comboBox_makeFC.currentIndex() == 0:
            self.FC='intelvem'
            self.ui.lineEdit_lib.setReadOnly(False)
            self.ui.lineEdit_lib.setStyleSheet('background-color:rgb(255,255,255)')
            # print(self.FC)
        elif self.ui.comboBox_makeFC.currentIndex() == 1:
            self.FC='gfortran'
            self.ui.lineEdit_lib.setReadOnly(True)
            self.ui.lineEdit_lib.setStyleSheet('background-color:rgb(150,150,150)')
            # print(self.FC)

    def searchFC(self):
        p=subprocess.run(['f2py','-c','--help-fcompiler'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.self_fparser.terminal_text.add_line(p.stdout.decode('utf-8'),number=2)

    def searchLib(self):
        file_dialog=QtWidgets.QFileDialog()
        folder=file_dialog.getExistingDirectory()
        self.ui.lineEdit_lib.setText(folder)
        self.complib=folder

    def properties(self):
        self.selectOS()
        self.select_precission()
        self.writeLib()
        self.fcompiler()
        self.searchLib()
    
    def runmake(self):
        self.selectOS()
        self.select_precission()
        self.writeLib()
        self.fcompiler()
        #Create python interface
        self.self_fparser.py_interface=fparser.py_interface_writer(self.self_fparser.lib,self.self_fparser.module_list,self.lib+'f',terminal=self.self_fparser.terminal_text)
        f=open(self.self_fparser.folder_path+'/'+self.lib+'.py','w+')
        f.write(self.self_fparser.py_interface)
        f.close() 

        #Generate Interface.pyf 
        run=[]

        if self.os=='Windows':
            self.f2py='f2py'
            end='.pyd'
        else:
            self.f2py='f2py3'
            end='.so'
        run.append(self.f2py)

        run.append(self.self_fparser.folder_path+'/Interface.f90')
        run.append('-m')
        run.append(self.lib+'f')
        run.append('-h')
        run.append(self.self_fparser.folder_path+'/Interface.pyf')
        run.append('--overwrite-signature')

        try:
            pyf=subprocess.run(run,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            self.self_fparser.terminal_text.add_line(pyf.stdout.decode('utf-8'),number=2)
            self.self_fparser.terminal_text.add_line('Success: Interface.pyf Generated',number=2)
        except:
            self.self_fparser.terminal_text.add_line(pyf.stderr.decode('utf-8'),number=2)

        #Apply precission
        if self.precission=='Simple precission.':
            new_precision=4
        else:
            new_precision=8

        f=open(self.self_fparser.folder_path+'/Interface.pyf','r')
        code=f.readlines()
        f.close()

        f=open(self.self_fparser.folder_path+'/Interface.pyf','w+')
        interface_pyf=fparser.increase_precision(code, 'real', new_precision, terminal=self.self_fparser.terminal_text)
        f.writelines(interface_pyf)
        f.close()

        run_comp=[]
        # make_bat='CALL f2py -c '

        if self.FC=='intelvem':
            flags=['--fcompiler='+self.FC,'--f90flags=-O3','--f90flags=-Wno-conversion','--f90flags=-std=f95','--f90flags=/real-size:64','-L'+''+self.complib+'']
        else:
            flags=['--fcompiler='+self.FC,'--f90flags=-O3','--f90flags=-Wno-conversion','--f90flags=-std=f95','--f90flags=-fdefault-real-8']

        # if self.precission=='Simple precission.':
        #     flags.pop(4)
        # print(flags)

        run_comp.append(self.f2py)
        run_comp.append('-c')
        # run_comp.append(self.self_fparser.folder_path+'/Interface.pyf')
        run_comp.append('Interface.pyf')
        # make_bat=make_bat+'Interface.pyf '

        #*.f Files 
        for f in self.self_fparser.files_f:
            f2='/'.join(f.split('\\')).split('/')[-1] 
            shutil.copy(f,self.self_fparser.folder_path+'/'+f2)
            run_comp.append(f2)
            # make_bat=make_bat+f2+' '
        #*.f90 Files 
        for f in self.self_fparser.files_order:
            f2='/'.join(f.split('\\')).split('/')[-1] 
            shutil.copy(f,self.self_fparser.folder_path+'/'+f2)
            run_comp.append(f2)
            # make_bat=make_bat+f2+' '
        # run_comp.append(self.self_fparser.folder_path+'/Interface.f90')
        run_comp.append('Interface.f90')
        # make_bat=make_bat+'Interface.f90 '
        #Flags 
        for flag in flags:
            run_comp.append(flag)
            # make_bat=make_bat+flag+' '


        #Run f2py 
        # if self.os=='Windows':
        #     #Create Makefile.bat
        #     f=open(self.self_fparser.folder_path+'/Makefile.bat','w+')
        #     f.write(make_bat)
        #     f.close()
        #     comp=subprocess.run(['Makefile.bat'],cwd=self.self_fparser.folder_path)
        # else:
        #     comp=subprocess.run(run_comp,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=self.self_fparser.folder_path)
        #     self.self_fparser.terminal_text.add_line(comp.stdout.decode('utf-8'),number=2)
        comp=subprocess.run(run_comp,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=self.self_fparser.folder_path)

        #Check if the library has been successfully generated
        ct=0
        with os.scandir(self.self_fparser.folder_path) as files:
            for f in files:
                if f.is_file():
                    file_name=f.name
                    if file_name.startswith(self.lib+'f') and file_name.endswith(end):
                        self.self_fparser.terminal_text.add_line('Success: Python library Generated',number=2)
                        ct=1
                        break
        if ct==0:
            self.self_fparser.terminal_text.add_line(comp.stderr.decode('utf-8'),number=2)
            self.self_fparser.terminal_text.add_line('Error: Python library generation Failed',number=2)

        #Move library to the new folder 
        # if self.os=='Linux':
        #     pwd=subprocess.run(['pwd'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #     lib_dir=pwd.stdout.decode('utf-8')
        #     end='.so'
        #     lib_dir=lib_dir.strip('\n')
        # else:
        #     chdir=subprocess.run(['chdir'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        #     lib_dir=chdir.stdout.decode('utf-8')
        #     end='.pyd'
        #     lib_dir=lib_dir.strip('\n').strip('\r')

        # try:
        #     with os.scandir(lib_dir) as files:
        #         for f in files:
        #             if f.is_file():
        #                 file_name=f.name
        #                 if file_name.startswith(self.lib+'f') and file_name.endswith(end):
        #                     lib_name=file_name
        #                     break
        #     os.rename(lib_dir+'/'+lib_name,self.self_fparser.folder_path+'/'+lib_name)
        #     self.self_fparser.terminal_text.add_line('Success: Python library Generated',number=2)
        # except:
        #     #self.self_fparser.terminal_text.add_line(comp.stderr.decode('utf-8'))
        #     self.self_fparser.terminal_text.add_line('Error: Python library generation Failed',number=2)




if __name__ == "__main__":

    p=subprocess.run(['pwd'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(p.stdout.decode('utf-8'))
    #dir1=os.path.dirname(os.path.abspath(__file__))
    #print(dir1)
    #pwd=subprocess.run(['pwd'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #lib_dir=pwd.stdout.decode('utf-8')
    #print(lib_dir)
    #lib_dir=lib_dir.strip('\n')
    #print(lib_dir)
    #with os.scandir(lib_dir) as files:
    #    for f in files:
    #        if f.is_file():
    #            if f.name.startswith('test_interface'+'f') and f.name.endswith('.so'):
    #                lib_name=f.name
    #                break
    #print(lib_name)