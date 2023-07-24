"""
Style Guide:
    Function Names = snake_case
    Variable Names = camelCase
    Class Name = CapitalizeEachWord
    Tabs = 4 spaces
    Wrap Code blocks in ####
    Function Docstring with Description, Parameters, Return
"""




def testing_func():
    """
    Description: Function for testing
    Parameters: None
    Returns: String "Hello"
    """
    return "Look at the Window Title"


def sample_md_text():
    file = open("markdown.md","r")
    string = file.read()
    return string



def sample_html_text():
    file = open("sample.html","r")
    string = file.read()
    return string
