import subprocess
import os
File_ui=os.path.dirname(os.path.abspath(__file__))+'/Window_fmodules.ui'
File_py=os.path.dirname(os.path.abspath(__file__))+'/Window_fmodules.py'
subprocess.run(['pyuic5','-x',File_ui,'-o',File_py])