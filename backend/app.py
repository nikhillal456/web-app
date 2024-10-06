from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import pyodbc
import os

app = Flask(__name__)
CORS(app)

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
@app.route('/')
def serve_html():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('frontend', filename)


@app.route('/submit', methods=['POST'])
def submit_data():
    value1 = request.json.get('Value1')
    value2 = request.json.get('Value2')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO DataEntries (Value1, Value2) VALUES (?, ?)", (value1, value2))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Data submitted successfully!'})

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Value1, Value2 FROM DataEntries")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    data = [{'Value1': row[0], 'Value2': row[1]} for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
