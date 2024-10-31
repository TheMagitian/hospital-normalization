#!/home/oracle/Documents/Project/proj/bin/python3
import getpass
import oracledb

# Thick mode for Oracle - needed for connection with instantclient and locally running db.

oracledb.init_oracle_client(lib_dir='/opt/oracle/product/21c/dbhomeXE/lib')

# connecting as sysdba
connection = oracledb.connect(
# 	user="sys",
	mode=oracledb.AUTH_MODE_SYSDBA,
	dsn="localhost/XEPDB1"
)

# creating a cursor
cursor = connection.cursor()

# testing connection by executing a query
# cursor.execute("SELECT * FROM v$instance")
cursor.execute("SELECT * FROM placement_event")

for row in cursor:
	print(row)

# close cursor & terminate connection
cursor.close()
connection.close()
