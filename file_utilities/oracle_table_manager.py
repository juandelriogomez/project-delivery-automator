import cx_Oracle
import re

class OracleTableManager:
    def __init__(self, db_username, db_password, db_host, db_port, db_service):
        self.connection = cx_Oracle.connect(db_username, db_password, f"{db_host}:{db_port}/{db_service}")
        self.cursor = self.connection.cursor()

    def check_table_sga_exists(self, name_table):
        query = """
           SQL
        """
        result = self.cursor.execute(query, {'table_name': name_table}).fetchone()
        return bool(result[0])
    
    def check_file_exists(self, file_name):
        query = """
           SQL
        """
        result = self.cursor.execute(query, {'file_name': file_name}).fetchone()
        return bool(result[0])
    
    def insert_processed_values(self, file_name):
        version_pattern = re.compile(r"(?:Entrega|VERSION_)(\d{3}(?:-p\d{2})?)\.zip")
        insert_query = """
            SQL
        """
        self.cursor.execute(insert_query, {'file_name': file_name, 
                                           'version': version_pattern.search(file_name).group(1)})
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
