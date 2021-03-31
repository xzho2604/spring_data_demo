import pandas as pd
import pyodbc
import psycopg2



table_csv_file = '/Users/erikzhou/Desktop/spring_lab/spring_data/springboot-postgresql-hibernate-crud-example/employees.csv'
host="localhost"
db="employees"
user_name="erikzhou"
password="admin"

# Import CSV
df = pd.read_csv (table_csv_file)   

# df = pd.DataFrame(data, columns= ['first_name','last_name','email_address'])

conn = psycopg2.connect(
    host=host,
    database=db,
    user=user_name,
    password=password)

cursor = conn.cursor()

# Create Table
# cursor.execute('CREATE TABLE people_info (Name nvarchar(50), Country nvarchar(50), Age int)')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO employees (first_name, last_name, email_address)
                VALUES (%s,%s,%s)
                ''',
                (row.first_name,row.last_name,row.email_address))
conn.commit()
