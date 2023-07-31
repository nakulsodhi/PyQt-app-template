import sqlite3

class ParamsDB():
    """docstring for ParamsDB."""

    def __init__(self, db_file_name):
        super(ParamsDB, self).__init__()
        self.con = sqlite3.connect(db_file_name)
        self.cur = self.con.cursor()

        self.cur.execute("""
                         CREATE TABLE IF NOT EXISTS Params(file, path, date_modified)
                         """)
        self.con.commit()

    def add_record(self,record):
        """
           Description: Add a record to the table
           Parameters: record (tuple) to be added
           Return: None 
           """   
        self.cur.execute("""
                         INSERT INTO Params VALUES(?, ?, ?)
                         """, record )
        self.con.commit()
        

    def get_record(self):
        """
           Description: Return Table from database 
           Parameters: self 
           Return: A list of tuples (records from table) 
           """   
        result = self.cur.execute("""
                                  SELECT * FROM Params
                                  """)
        result = result.fetchall()
        return result
    

    def delete_record(self, filepath):
        self.cur.execute(f"""
                         DELETE FROM Params WHERE path = "{filepath}" 
                         """)
        self.con.commit()
    
    def clear_table(self):
        """
           Description: Delete all items from the table. 
           Parameters: self
           Return: None
        """   
        self.cur.execute("""
                         DELETE FROM Params
                         """ )
        self.con.commit()
