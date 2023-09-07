import cx_Oracle
import re

class OracleTableManager:
    def __init__(self, db_username, db_password, db_host, db_port, db_service):
        self.connection = cx_Oracle.connect(db_username, db_password, f"{db_host}:{db_port}/{db_service}")
        self.cursor = self.connection.cursor()

    def check_table_sga_exists(self, name_table):
        query = """
            SELECT CASE WHEN COUNT(*) > 0 THEN 1 ELSE 0 END AS EXISTE_REGISTRO
            FROM CGA_META_TABLAS_SGA
            WHERE TX_NOMBRE = :table_name
        """
        result = self.cursor.execute(query, {'table_name': name_table}).fetchone()
        return bool(result[0])
    
    def check_file_exists(self, file_name):
        query = """
            SELECT CASE WHEN COUNT(*) > 0 THEN 1 ELSE 0 END AS EXISTE_REGISTRO
            FROM CGA_META_ENTREGAS
            WHERE TX_FICHERO = :file_name
        """
        result = self.cursor.execute(query, {'file_name': file_name}).fetchone()
        return bool(result[0])
    
    def insert_processed_values(self, file_name):
        version_pattern = re.compile(r"(?:Entrega|VERSION_)(\d{3}(?:-p\d{2})?)\.zip")
        insert_query = """
            INSERT INTO CGA_META_ENTREGAS (TX_FICHERO, TX_FECHA, LG_TRATADO, NU_VERSION)
            VALUES (:file_name, SYSTIMESTAMP, 'S', :version)
        """
        self.cursor.execute(insert_query, {'file_name': file_name, 
                                           'version': version_pattern.search(file_name).group(1)})
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()