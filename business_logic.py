from pathlib import Path
import database
import datetime

"""
Style Guide:
    Function Names = snake_case
    Variable Names = camelCase
    Class Name = CapitalizeEachWord
    Tabs = 4 spaces
    Wrap Code blocks in ####
    Function Docstring with Description, Parameters, Return
"""

###################### Initialize the database
fileHistoryDatabase = database.ParamsDB("file-edit-history.db")
####################################



####################### Function definitions
def testing_func():
    """
    Description: Function for testing
    Parameters: None
    Returns: String "Look at the Window Title"
    """
    return "Look at the Window Title"


def sample_md_text():
    """
       Description: Sample MarkDown Text
       Parameters: None
       Return: MarkDown sample as a string  
       """       
    file = open("markdown.md", "r")
    string = file.read()
    return string

def return_filename(path):
    """
    Description: Returns filename given the absolute path
    Parameters: path to the file
    Return: file name
   """  
    file_obj = Path(path)
    return file_obj.stem

def sample_html_text():
    """
    Description: Sample HTML Text
    Parameters: None
    Return: HTML sample as a string 
    """
    file = open("sample.html", "r")
    string = file.read()
    return string

def append_file_history(path):
    """
    Description: Append the file history database
    Parameters: path to the opened file
    Return: None 
    """
    filename = return_filename(path)
    #delete existing record
    fileHistoryDatabase.delete_record(path)
    time = str(datetime.datetime.now())
    fileHistoryDatabase.add_record( (filename,path,time) )

def get_last_file():
    """
    Description: Get the last modified file from the database
    Parameters: None
    Return: The db record tuple (filename, path, date modified) 
    """
    rec = fileHistoryDatabase.get_record()
    recordReturn = rec[-1]
    # [Not Required Anymore] fileHistoryDatabase.delete_record(recordReturn[1])
    return recordReturn

def eval_expression(expression):
    """
    Description: Given a math expression in string form, evaluate it 
    Parameters: String expression 
    Return: either int/float solution or the ERROR string 
    """
    try:
        answer = eval(expression)
    except:
        answer = "ERROR"
    return answer


####################################


