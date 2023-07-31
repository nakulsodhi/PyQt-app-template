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
    file = open("sample.html", "r")
    string = file.read()
    return string


#def open_file_in_editor(filePath):
#    pass

def append_file_history(path):
    filename = return_filename(path)
    #delete existing record
    fileHistoryDatabase.delete_record(path)
    time = str(datetime.datetime.now())
    fileHistoryDatabase.add_record( (filename,path,time) )

def get_last_file():
    rec = fileHistoryDatabase.get_record()
    recordReturn = rec[-1]
    # [Not Required Anymore] fileHistoryDatabase.delete_record(recordReturn[1])
    return recordReturn

def eval_expression(expression):
    try:
        answer = eval(expression)
    except:
        answer = "ERROR"
    return answer


####################################


