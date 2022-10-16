# Latex linter

This is a simple latex linter that is going to take a file as an input and fix it



Lists:
    If \begin{document}
        No lines will be tapped until \begin{something else than document}

    If \begin is commented with %, the text will not change. 
    
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
        There will be extra space after %.
        

    If it's more than one % after each other:
        "%%%" ---> "% % % "


 

 Mathenivorment:

    Right now there is a bug that can cause problem in the text:
        if line contains "$":
            The system will think that all "$" is mathematical expression.
            If "$" will be in middle of line:
                ex input:
                    "This t-shirt cost 50$."
                output:
                    "This t-shirt cost 50 $ ."