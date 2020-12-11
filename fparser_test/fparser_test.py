#%% Imports
import pytest
import os

import fobjects
import fparser

#%% Helper Functions
def path_joining(file_dir):
    """
    Helper function to get the path to test modules.

    Args:
        file_dir (string): Path of the file.

    Returns:
        String with the path to the files
    """
    file_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               '../FortranExamples/TestModules/' + file_dir)
    return file_dir

def file_reader(file_dir):
    """
    Helper function to read Fortran files.

    Args:
        file_dir (string): Path of the file.

    Returns:
        list of strings with each line of the file.
    """
    file_dir = path_joining(file_dir)
    file = open(file_dir, 'r') 
    file_code = file.readlines() 

    for i, line in enumerate(file_code):
        file_code[i] = line.replace('\n', '')
    file.close()
    return file_code

#%% Tests for fparser objects
@pytest.mark.parametrize('file,module_names', [
    ('TestModule1.f90', ['test_module_1', 'test_module_12']),
    ('TestModule2.f90', ['test_module_2']),
    ('TestModule3.f90', ['test_module_3'])
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

@pytest.mark.parametrize('file,contents', [
    ('TestModule1.f90', ['test_function_1', 'test_function_12']),
    ('TestModule2.f90', ['test_function_2', 'test_subroutine_1']),
    ('TestModule3.f90', ['test_function_3', 'test_function_4'])
    ])
def test_contains_reader(file, contents):
    """
    Tests to determine if fparser is interpreting the contents names correctly.

    Args:
        file (string): Name of the Fortran File 
        contents (list): Name of each functional in the file
    """
    file_code = file_reader(file)
    fortran_file = fobjects.Ffile(file, file_code)
    file_contents = list()
    for m in fortran_file.modules:
        file_contents += [x for x in m.contents]
    for f in contents:
        assert f in [x.name for x in file_contents], 'fparser could not find functional {} within {}.'.format(f, file)
    assert len(contents) == len(file_contents), 'contents read by fparser in {} do not match number of contents expected.'.format(file)

@pytest.mark.parametrize('files,expected_order', [
    (['TestModule1.f90', 'TestModule2.f90'], ['test_module_1', 'test_module_12', 'test_module_2']),
    (['TestModule1.f90', 'TestModule2.f90', 'TestModule3.f90'], ['test_module_1', 'test_module_12', 'test_module_2', 'test_module_3'])
    ])
def test_dependecies_ordering(files, expected_order):
    """
    Tests to determine if fparser is ordering modules correctly by number of dependencies and generating libraries correctly.

    Args:
        files (list): Test files from which to read modules
        expected_order (list): Expected module order
    """
    fortran_files = list()
    for file in files:
        file_code = file_reader(file)
        fortran_files.append(fobjects.Ffile(file, file_code))
    lib = fobjects.Flibrary(fortran_files)
    assert len(expected_order) == len(lib.modules), 'Modules read by fparser in {} do not match number of Modules expected.'.format(files)
    for m, ex_m in zip(lib.modules, expected_order):
        assert m.name == ex_m, 'Modules from files {} did not appear in the expected order'.format(files)

@pytest.mark.parametrize('files', [
    (['TestModule1.f90', 'TestModule2.f90']),
    (['TestModule1.f90', 'TestModule2.f90', 'TestModule3.f90'])
    ])
def test_fake_naming(files):
    """
    Tests to determine if fparser is renaming contents and modules correctly.

    Args:
        files (list): Test files from which to read modules
    """
    fortran_files = list()
    for file in files:
        file_code = file_reader(file)
        fortran_files.append(fobjects.Ffile(file, file_code))
    lib = fobjects.Flibrary(fortran_files)
    for m in lib.modules:
        assert m.fake_name != m.name, 'Module {} was renamed incorrectly to {}'.format(m.name, m.fake_name)
        for c in m.contents:
            assert c.fake_name != c.name, '{} in {} was renamed incorrectly to {}'.format(c.name, m.name, c.fake_name)
    all_names = [m.name for m in lib.modules] + [m.fake_name for m in lib.modules] + \
        [c.name for m in lib.modules for c in m.contents] + [c.fake_name for m in lib.modules for c in m.contents]
    for a in all_names:
        assert all_names.count(a) == 1, '{} hasn\'t been renamed correctly, it should appear only once in library but appears {}.'.format(a, all_names.count(a))

#%% Tests for fparser control
@pytest.mark.parametrize('files', [
    (['TestModule1.f90', 'TestModule2.f90']),
    (['TestModule1.f90', 'TestModule2.f90', 'TestModule3.f90'])
    ])
def test_library_maker(files):
    """
    Tests to determine if fparser is making libraries correctly.

    Args:
        files (list): Test files from which to read modules
    """
    new_files = list()
    for file_dir in files:
        new_files.append(path_joining(file_dir))
    lib = fparser.library_maker(new_files)
    assert isinstance(lib, fobjects.Flibrary)

@pytest.mark.parametrize('files,module_names', [
    (['TestModule1.f90', 'TestModule2.f90'], ['test_module_1', 'test_module_2']),
    (['TestModule1.f90', 'TestModule2.f90', 'TestModule3.f90'], ['test_module_1', 'test_module_2', 'test_module_3'])
    ])
def test_interface_writer(files, module_names):
    """
    Tests to determine if fparser is making interfaces from libraries correctly.

    Args:
        files (list): Test files from which to read modules.
        module_names (list): Name of modules that ought to be in that interface.
    """
    new_files = list()
    for file_dir in files:
        new_files.append(path_joining(file_dir))
    lib = fparser.library_maker(new_files)
    interface = fparser.interface_writer(lib, module_names)
    interface_lines = interface.split('\n')
    interface_file = fobjects.Ffile('interface', interface_lines)
    assert len(interface_file.modules) == len(module_names), 'Number of Modules made in interface does not match number of modules expected.'
    for m in interface_file.modules:
        assert m.name in [x.fake_name for x in lib.modules], 'Modules made in interface {} is not within original library'.format(m.name)

@pytest.mark.parametrize('file_code,var_type,new_precision,output', [
    (['function test(x,y,z)', 'real,dimension(2)::x', 'real(8),dimension(2)::y', 'real*16 ,dimension(2)::x'],
    'real', 8,
    ['function test(x,y,z)', 'real(8),dimension(2)::x', 'real(8),dimension(2)::y', 'real*16 ,dimension(2)::x']),
    (['function test(x,y,z)', 'real,dimension(2)::x', 'real(8),dimension(2)::y', 'real*16,dimension(2)::x'],
    'real', 16,
    ['function test(x,y,z)', 'real(16),dimension(2)::x', 'real(16),dimension(2)::y', 'real*16,dimension(2)::x']),
    (['function test(x,y,z)', 'real,dimension(2)::x', 'real(8),dimension(2)::y', 'real*16::x'],
    'real', 32,
    ['function test(x,y,z)', 'real(32),dimension(2)::x', 'real(32),dimension(2)::y', 'real(32)::x'])
    ])
def test_increase_precision(file_code, var_type, new_precision, output):
    """
    Tests to determine if fparser is increasing the precision of variable types as commanded.

    Args:
        file_code (list): List of strings containing the code.
        var_type (string): Type of variable to change the precision.  
        new_precision (int): New Variable precision
        output(list): expected output of the function
    """
    for i, j in zip(fparser.increase_precision(file_code, var_type, new_precision), output):
        assert i == j, 'Increase precision function isn\'t working as expected'
