import mysql.connector

class DatabaseConnection():

    def __init__(self):
        self.host = "ba4wmpjwd2fynuzr9vvq-mysql.services.clever-cloud.com"
        self.port = 3306
        self.user = "u8xcfo4ko24ym54s"
        self.password = "QP4QNTpnWNYLP0uJMahz"
        self.database = "ba4wmpjwd2fynuzr9vvq"
        self.cnx = None
        self.cursor = None
        self.order_id = ""

    def connect(self):
        self.cnx = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )

        if self.cnx.is_connected():
            print("Connection established to the MySQL database")
            self.cursor = self.cnx.cursor()

    def close(self):
        if self.cnx.is_connected():
            self.cnx.close()
            print("Connection closed to the MySQL database")

    def query(self, sql, data):
        self.cursor.execute(sql, data)
        result = self.cursor.fetchall()
        return result

    def query_no_data(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute(self, sql, data):
        self.cursor.execute(sql, data)
        self.cnx.commit()

    def execute_no_data(self, sql):
        self.cursor.execute(sql)
        self.cnx.commit()

    def execute_multi_line_no_data(self, sql):
        self.cursor.execute(sql)
        self.cnx.commit()


# Create an instance of the class
# db_conn = DatabaseConnection(
#     host="ba4wmpjwd2fynuzr9vvq-mysql.services.clever-cloud.com",
#     port=3306,
#     user="u8xcfo4ko24ym54s",
#     password="QP4QNTpnWNYLP0uJMahz",
#     database="ba4wmpjwd2fynuzr9vvq"
# )

# Connect to the database
#db_conn.connect()

# Execute a query
#result = db_conn.query("SELECT * FROM product")

# Print the result
#print(result)

# Close the connection
#db_conn.close()