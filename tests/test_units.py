import pages.functions as functions

def test_isTex():
    assert functions.isTex("test.tex") == True

def test_isNotTex():
    assert functions.isTex("test.py") == False

def test_addTaps():
    assert functions.addTaps("test") == "\ttest"

def test_newSentence():
    assert functions.newSentence("test;") == "test;\n"

def test_addNewLines():
    assert functions.addNewLines("test", 2) == "\n\ntest"

def test_addSpace():
    assert functions.addSpace("test") == " test"

def test_listBlock():
    text = "\\begin{itemize}This is a test\nthis is a secound line.\n\\end{itemize}"
    assert functions.listBlock(text) == "\\begin{itemize}\n\tThis is a test\n\tthis is a secound line.\n\\end{itemize}"
