import subprocess
File_ui='/home/david/Documentos/Matemáticas_MUSE/fparser/fparser_GUI/Ejemplos_GUI/Window.ui'
File_py='/home/david/Documentos/Matemáticas_MUSE/fparser/fparser_GUI/Ejemplos_GUI/Window_ui.py'
subprocess.run(['pyuic5','-x',File_ui,'-o',File_py])