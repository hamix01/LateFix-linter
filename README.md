# LateFix linter

This is a simple latex linter that is going to take a file as an input and fix it


Use program:

    To start the program enter command [python3 main.py [filename.tex]]
    Terminal will print The standard size of line brakes after chapters.
    Terminal will print if better git support is active with "True" or if not active "False"
    
    The output should look like:
    "
    LateFix Linter...
    Line break size: 0
    Better git support: False
    "

    To active better git support enter command [python3 main.py [filename.tex] -git True/False]

    To add new lines after chapter [python3 main.py [filename.tex] -git True/False -line [number_of_lines]] or 
    [python3 main.py [filename.tex] -line [number_of_lines]]
    
    Please note that new line between chapter is not implemented and nothing will happen with the text if you use the command.


Lists:

    If \begin{document}
        No lines will be tapped until \begin{something else than document}

    If \begin is commented with %:
        all lines will be tapped after until it's new list \begin{...} in line or \end{...}
    
    If \end{document}
        All lines after will be tapped

    If \end is commented with %, the text will not change. 




Better git support:

    If user set better git support to True:
        After [":", ";", ",", ".", "!", "?"] it will be new line.
    ex. 
        "Hello, This is linter for laTex.Welcome!"
        will be:
            "Hello,
             This is linter for laTex.
            Welcome!

            "
    Space after marks will continue to remain.
    If "Hello...":
        The output will be:
            "Hello.
            .
            .
            "



Comments:

    When % exists it will be space after. 
    If spaces already exist:
        There will be extra space after and before "%" --> " % ".
    If it's more than one % after each other:
        "%%%" ---> " %  %  % ow"


 
 Math environment:

    Right now there is a bug that can cause problem in the text:
        if line contains "$":
            The system will think that all "$" is mathematical expression.
            If "$" will be in middle of line:
                ex input:
                    "This t-shirt cost 50$."
                output:
                    "This t-shirt cost 50 $ ."




Test of functions:

    To start the tests of the functions type the command [pytest].
    The tests will either be true(succeed) or false(fail).
    The tests shows the input that have been made and the output and what it expected. 
