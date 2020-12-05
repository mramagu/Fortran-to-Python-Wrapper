import random
import string

def section(code, command):
    """
    Function that sections a code according to a command

    Args:
        code (list): 
        command (string): 

    Returns:
        list: A list with all module objects
    """
    sections = list()
    section_str = list()
    present = False
    for i, line in enumerate(code):
        if find_command(line.lower(), command) != None and find_command(line.lower(), 'end') == None:
            present = True
        elif find_command(line.lower(), command) != None and find_command(line.lower(), 'end') != None:
            present = False
            section_str.append(line)
            sections.append(section_str)
            section_str = list()

        if present:
            section_str.append(line)
    return sections

def find_command(code_line, name):
    """
        Function that finds the position of a command in a fortran line.

        Args:
            code_line (string): line of code
            name (string): name of the command

        Returns:
            None if it is not present or its position in the code line string
    """
    before_chars = [',', ')', ':', ' '] # Characters allowed rigth before name
    after_chars = [',', '(', '=', '!', ' '] # Characters allowed rigth after name
    discard_between = ['\'', '\"']
    counter = 0
    while counter + len(name) <= len(code_line): # Studies each position in the line
        if code_line[counter] in discard_between: # If fortran character is being written jumps to end of char
            jump = code_line[counter+1].find(code_line[counter])
            if jump == -1:
                raise Exception('Fortran character did not finish being declared from position {}: \n {}'.format(counter, code_line))
            counter += jump + 1
        if name.lower() == code_line[counter:counter+len(name)].lower(): # If selection matches it studies the code
            if counter == 0: # Finds if selection before command is valid
                    before = True
            else:
                if code_line[counter - 1] in before_chars:
                    before = True
                else:
                    before = False
            if counter + len(name) == len(code_line): # Finds if selection after command is valid
                after = True
            else:
                if code_line[counter+len(name)] in after_chars:
                    after = True
                else:
                    after = False

            if before and after: # If both are valid it returns the position
                return counter
                break

        if code_line[counter] == '!': # If writting fortran comment invalidate rest of the line and returns None
            return None
            break

        counter += 1 # Adds 1 to the counter
    else: # If it reaches the end of the code without finding command it returns None
        return None

def identify_comment(code_line):
    """
        Finds the comment in a fortran line of code.

        Args:
            code_line (string): Line in which the variable is defined.

        Returns:
            string of the comment incluiding the initial ! or None.
    """
    discard_between = ['\'', '\"']
    counter = 0
    while counter + 1 <= len(code_line): # Studies each position in the line
        if code_line[counter] in discard_between: # If fortran character is being written jumps to end of char
            jump = code_line[counter+1].find(code_line[counter])
            if jump == -1:
                raise Exception('Fortran character did not finish being declared from position {}: \n {}'.format(counter, code_line))
            counter += jump + 1
        if code_line[counter] == '!': # If it finds comment declaration it stores it 
            return code_line[counter:]
            break

        counter += 1 # Advances counter
    else: # If it reaches the end of the code without finding comment it returns none
        return None

def block_comments(code):
    """
        Finds the comment block between two points in the code.

        Args:
            code (list): List of strings of the fortran code.

        Returns:
            List of str of the code that are pure comments.
    """
    block = list()
    for line in code:
        if bool(line.strip()): # If line is not empty
            if line.strip()[0] == '!': # If the first character of the string is the start of a comment it adds it
                block.append(identify_comment(line))
            elif bool(line.strip()): # If the first character of the string is not the start of a comment or its not empty it exits
                break
    return block

def name_generator(suggested, forbidden_names):
    """
        Generates a name for an object that is not included in the forbidden names list (no spaces).
        Names are generated from the suggested name.

        Args:
            suggested (string): Initial suggestion with which to generate the new name.
            forbidden_names (list): List of names the new name cannot take (lowercase).

        Returns:
            String with the new name.
    """
    new_name = suggested.strip()
    while new_name.lower() in [x.lower() for x in forbidden_names]:
        new_name += str(random.choice(string.ascii_lowercase))
    return new_name.strip()


def find_and(code_line):
    """
        Function that finds the position of & command in a fortran line.

        Args:
            code_line (string): line of code       

        Returns:
            None if it is not present or its position in the code line string
    """
    discard_between = ['\'', '\"']
    counter = 0
    while counter + 1 <= len(code_line): # Studies each position in the line
        if code_line[counter] in discard_between: # If fortran character is being written jumps to end of char
            jump = code_line[counter+1].find(code_line[counter])
            if jump == -1:
                raise Exception('Fortran character did not finish being declared from position {}: \n {}'.format(counter, code_line))
            counter += jump + 1
        if '&' == code_line[counter]: # If selection matches it studies the code       
            return counter
            break
        if code_line[counter] == '!': # If writting fortran comment invalidate rest of the line and returns None
            return None
            break
        counter += 1 # Adds 1 to the counter
    else: # If it reaches the end of the code without finding command it returns None
        return None

    
def find_and_lists(code_line):
    """
        Function that finds the position of & in all the elements of a list

        Args:
            code_line (string): line of code       

        Returns:
            List with & positions in the code
    """
    list_ands =[]
    counter = 0
    while counter + 1 <= len(code_line):
     and_finder = find_and(code_line[counter])
     counter += 1
     list_ands.append(and_finder)
     and_position = [] 
    for val in list_ands: 
     if val != None : 
      and_position.append(val) 
    print (and_position) 