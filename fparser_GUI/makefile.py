print('HelloWord!')
def f(ui,mf):
    mf.os=ui.combobox.currentText()

class Makefile():
    def __init__(self):
        self.os=''
        self.compiler=''
