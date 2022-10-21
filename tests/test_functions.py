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


def test_make_new_file():
    assert functions.make_new_file("test", "test.tex") == "File test.tex created"

def test_space_after_comment():
    text = "%test"
    assert functions.space_after_comment(text) == "% test"

def test_tab_list():
    text = "\\begin{itemize}This is a test\nthis is a second line.\n\\end{itemize}"
    assert functions.tab_list(text) == "\\begin{itemize}\n\tThis is a test\n\tthis is a second line.\n\\end{itemize}"


def test_add_new_line():
    text = "This is a test, this is a second line."
    assert functions.add_new_line(text) == "This is a test,\n this is a second line."

def test_math_mode():
    text = "This is a test $(1+1=2)$"
    assert functions.math_mode(text) == "This is a test $this is a second line$"
