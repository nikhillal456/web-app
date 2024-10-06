from flask import Flask, render_template, request, jsonify
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
@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML file

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
i
