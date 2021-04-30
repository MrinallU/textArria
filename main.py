import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'root',
    'password': 'Thekey2275!',
    'host': '35.223.103.123',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}




config['database'] = 'testdb' 
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()

cnxn.commit() 


# first we setup our query
# query = ("INSERT INTO space_missions (company_name) VALUES (5)")
# cursor.execute(query)
# cnxn.commit()  

cursor.execute("SELECT * FROM space_missions")
my_result = cursor.fetchone()
while my_result is not None:
    print(my_result)
    my_result = cursor.fetchone()