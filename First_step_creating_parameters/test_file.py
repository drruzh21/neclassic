import pyodbc

def print_column_names(db_path, table_name):
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=' + db_path + ';'
    )
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0")  # Запрос без данных
        columns = [column[0] for column in cursor.description]
        print(f"Столбцы в таблице '{table_name}':")
        for col in columns:
            print(f" - {col}")
    except pyodbc.Error as e:
        print(f"Ошибка при подключении или выполнении запроса для таблицы '{table_name}':", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    db_path = r"C:\Hackaton_October\neclassic\main_data.accdb"
    tables = ['GOST', 'MTR', 'OKPD_2']
    for table in tables:
        print_column_names(db_path, table)
        print()
