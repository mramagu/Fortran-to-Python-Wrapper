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
        if command in line and 'end' not in line.lower():
            present = True
        elif command in line and 'end' in line.lower():
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
        
        print(counter + len(name), len(code_line))
        print(code_line[counter:counter+len(name)], name)
        if name == code_line[counter:counter+len(name)]: # If selection matches it studies the code
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