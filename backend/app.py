from flask import Flask, request, jsonify
import pyodbc
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = pyodbc.connect(
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server={os.environ['SQLSERVER_IP']};"
        f"Database={os.environ['SQLSERVER_DB']};"
        f"UID={os.environ['SQLSERVER_USER']};"
        f"PWD={os.environ['SQLSERVER_PASS']};"
    )
    return conn

@app.route('/submit', methods=['POST'])
def submit_data():
    value1 = request.json.get('value1')
    value2 = request.json.get('value2')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO your_table_name (column1, column2) VALUES (?, ?)", (value1, value2))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Data submitted successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

