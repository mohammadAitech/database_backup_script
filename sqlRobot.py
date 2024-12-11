import pyodbc as pdb

server = "MOHAMMAD"
database="master"

connection = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
conn = pdb.connect(connection)
cursor = conn.cursor()

try:
    backuped_db_name = input("please enter your database name for backuped: ")
    backuped_db_path = input("backuped path for example (F:/specifies_folder_name/backup_file_name.back) ")

    print(backuped_db_path)
    conn.autocommit = True

    select_db_query = "SELECT name FROM sys.databases"
    cursor.execute(select_db_query)

    databases= cursor.fetchall()

    for db in databases:
        if db.name == backuped_db_name:
            backup_query=f"BACKUP DATABASE [{db.name}] TO DISK='{backuped_db_path}'"
            cursor.execute(backup_query)
            print("backuped database")
except Exception:
    print(Exception)