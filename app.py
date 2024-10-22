from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Configure SQL Server connection
def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your_server;'
        'DATABASE=your_database;'
        'UID=your_username;'
        'PWD=your_password;'
    )
    return conn

# Home route - search page
@app.route('/')
def search_page():
    return render_template('search.html')

# Search route - fetch data based on journal_id
@app.route('/search', methods=['POST'])
def search_journal():
    journal_id = request.form.get('journal_id')
    
    # Connect to database and fetch data
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM journals WHERE journal_id = ?"
    cursor.execute(query, (journal_id,))
    result = cursor.fetchall()

    # Close the connection
    conn.close()

    # Render the results in result.html
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
