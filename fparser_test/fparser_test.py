#%% Imports
import pytest
import os

import fobjects

#%% Helper Functions
def file_reader(file_dir):
    """
    Helper function to read Fortran files.

    Args:
        file_dir (string): Path of the file.

    Returns:
        list of strings with each line of the file.
    """
    file_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               '../FortranExamples/TestModules/' + file_dir)
    file = open(file_dir, 'r') 
    file_code = file.readlines() 

    for i, line in enumerate(file_code):
        file_code[i] = line.replace('\n', '')
    file.close()
    return file_code

#%% Tests 
@pytest.mark.parametrize('file,module_names', [
    ('TestModule1.f90', ['test_module_1', 'test_module_2'])
    ])
def test_module_reader(file, module_names):
    """
    Tests to determine if fparser is interpreting the modules names correctly.

    Args:
        file (string): Name of the Fortran File 
        module_names (list): Name of each module in the file
    """
    file_code = file_reader(file)
    fortran_file = fobjects.Ffile(file, file_code)
    for module in module_names:
        assert module in [x.name for x in fortran_file.modules], 'fparser could not find modoule {} within {}.'.format(module, file)
    assert len(module_names) == len(fortran_file.modules), 'modules read by fparser in {} do not match number of modules expected.'.format(file)

@pytest.mark.parametrize('file,functionals', [
    ('TestModule1.f90', ['test_function_1', 'test_function_2'])
    ])
def test_functional_reader(file, functionals):
    """
    Tests to determine if fparser is interpreting the functionals names correctly.

    Args:
        file (string): Name of the Fortran File 
        functionals (list): Name of each functional in the file
    """
    file_code = file_reader(file)
    fortran_file = fobjects.Ffile(file, file_code)
    file_functionals = list()
    for m in fortran_file.modules:
        file_functionals += [x for x in m.functionals]
    for f in functionals:
        assert f in [x.name for x in file_functionals], 'fparser could not find functional {} within {}.'.format(f, file)
    assert len(functionals) == len(file_functionals), 'functionals read by fparser in {} do not match number of functionals expected.'.format(file)