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
    times = []
    count_times=0
    times_end=[]
    count_times_end=0
    for i, line in enumerate(code):
        if find_command(line.lower(), command) != None and find_command(line.lower(), 'end') == None:
            present = True
            count_times=count_times+1
            times.append(count_times)
        elif find_command(line.lower(), command) != None and find_command(line.lower(), 'end') != None:
            present = True
            count_times_end=count_times_end+1
            times_end.append(count_times_end)         
            if times == times_end:
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

def find_closing_parenthesis(code_line, start):
    """
        Finds the position of the closing parenthesis in a line of code given the position of the starting one.

        Args:
            code_line (string): Initial suggestion with which to generate the new name.

        Returns:
            Position of closing parenthesis in the code line
    """
    counter = start + 1
    while counter + 1 <= len(code_line):
        if code_line[counter] == '(':
            counter = find_closing_parenthesis(code_line, counter)
        elif code_line[counter] == ')':
            return counter
            break
        counter += 1
    else:
        raise Exception('Parenthesis is not closed in line: \n{}'.format(code_line))


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

def tabing_tool(code):
    """
        Adds a 4 space tab to every string on the list

        Args:
            code (list): List of strings

        Returns:
            Tabulated list
    """
    for i, line in enumerate(code):
        code[i] = ' '*4 + line
    return code
    
def remove_and_lists(code_line):
    """
        Function that finds the position of & in all the elements of a list and removes it

        Args:
            code_line (string): line of code       

        Returns:
            List with lines of code without the & , the lines that where separated by the & are merged
    """
    list_ands_element =[]
    list_ands_position =[]
    counter = 0
    z=0
    while counter + 1 <= len(code_line):
     and_finder = fparsertools.find_and(code_line[counter])
     counter += 1
     list_ands_position.append(and_finder)
     if and_finder != None : 
      list_ands_element.append(counter-1)
     and_position = [] 
     for val in list_ands_position: 
      if val != None : 
        and_position.append(val) 
     counter2 = 0
     clean_code=[]
     while counter2+1 <= len(code_line):  
      if counter2 not in list_ands_element:
       clean_code.append(code_line[counter2])  
     if counter2 in list_ands_element: 
      x = 0+z     
      clean_code.append(code_line[counter2][:and_position[x]] + code_line[counter2+1]) 
      z=1
      counter2+=1
     counter2+=1
    return clean_code



  