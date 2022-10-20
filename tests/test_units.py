"""
    Test the functions in the functions.py file
"""
from pages import functions

def test_is_tex():
    """
        Test if the file is a tex file
    """
    assert functions.is_tex("test.tex") == True

def test_is_not_tex():
    """
        Test if the file is not a tex file
    """
    assert functions.is_tex("test.py") == False

def test_add_taps():
    assert functions.add_taps("test") == "\ttest"

def test_new_sentence():
    assert functions.new_sentence("test;") == "test;\n"

def test_addNewLines():
    assert functions.addNewLines("test", 2) == "\n\ntest"

def test_addSpace():
    assert functions.addSpace("test") == " test"

def test_listBlock():
    text = "\\begin{itemize}This is a test\nthis is a secound line.\n\\end{itemize}"
    assert functions.listBlock(text) == "\\begin{itemize}\n\tThis is a test\n\tthis is a secound line.\n\\end{itemize}"
