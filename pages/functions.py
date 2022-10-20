"""functions collection"""


def print_flags():
    """ print the flags that are set"""

    print("""
    Usages: python3 main.py [source file] [flags]
    
    The following flags are set:
    
    --better_git_support      Gives a better git support
    --line_break_size         Sets the line break size
    """)

def is_tex(file):
    """ check if the file is a tex file """
    tex = False
    if ".tex" in file:
        tex = True
    return tex

def get_text(file_path):
    """ get the text from the file """
    text = ""
    file = open(file_path, "r", encoding="utf-8")
    for line in file:
        text += line
    file.close()
    return text

def add_taps(line):
    """ add taps to the line """
    return "\t" + line

def add_lines(text, number):
    """ add lines to the text """
    # final_text = ""
    # for line in text.split("\n"):
    #     line = (number * "\n") + line
    #     final_text += line
    #     # print(final_text)
    # for line in text.strip():
    #     print(line + ">12312>s123213hell")

    return number

def remove_lines(text, line_break_size):
    """ remove lines from the text """
    final_text = ""
    # text = text.replace('\n','')
    lines = text.split("\n")
    # final_text = addLines(text, line_break_size)
    for line in lines:
        # strip blank lines
        if line != "":
            final_text += line + "\n"

    return final_text


def make_new_file(text, name):
    """ make a new file """
    new_file = open(name, "w", encoding="utf-8")
    new_file.write(text)
    new_file.close()
    file_done = "File " + name + " created"
    return file_done


def space_after_comment(text):
    """ add a space after a comment """
    final_text = ""
    for line in text.split("\n"):
        if contain_word("%", line):
            line = line.replace("%", " % ")
        final_text += line + "\n"
    return final_text

def contain_word(word, string):
    """check if a word is in a string"""
    contains = False
    if word in string:
        contains =  True
    return contains

def choose_file_name():
    """ choose a file name """
    file_name = input("Enter the file name: ") + ".tex"
    return file_name

def tab_list(text):
    """
    This function will add tabs to the list
    """
    final_text = ""
    is_list = False

    for line in text.split("\n"):
        if contain_word("begin{", line) and not contain_word("document", line) and not contain_word("%\begin", line):
            final_text += line + "\n"
            is_list = True
            continue
        elif is_list:
            if contain_word("end{", line) and not contain_word("document", line) and not contain_word("%\end", line):
                final_text += line + "\n"
                is_list = False
                continue
            else:
                final_text += add_taps(line) + "\n"
        else:
            final_text += line + "\n"
    return final_text

def add_new_line(text):
    """
    This function will add a new line after a sentence
    """
    final_text = ""
    marks = [":", ";", ",", ".", "!", "?"]
    for line in text.split("\n"):
        for mark in marks:
            if mark in line:
                line = line.replace(mark, mark + "\n")
        final_text += line + "\n"
    return final_text


def math_mode(text):
    """space after math mode"""

    signs = ["+", "-", "*", "/", "=", "(", ")", "[", "]", "{", "}", ">", "<", "!", "|", "&", "^", "~", ":", ";", ",", ".", "!", "?", "$"]
    final_text = ""
    for line in text.split("\n"):
        if contain_word("$", line):
            for sign in signs:
                if sign in line:
                    line = line.replace(sign, " " + sign + " ")
        final_text += line + "\n"
    return final_text

def logic(file_path, better_git_support, line_break_size):
    """
    This function will do the logic
    """
    text = get_text(file_path)
    # final_text = ""

    if better_git_support:
        text = add_new_line(text)

    if "begin{" in text:
        text = tab_list(text)    
    text = space_after_comment(text)
    text = math_mode(text)    
    if line_break_size >= 0:
        text = remove_lines(text, line_break_size)
        # text = add_lines(text, line_break_size)

    # file_name = choose_file_name()
    # file_done = make_new_file(final_text, file_name)
    print(text)
    return text
