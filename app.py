from flask import Flask, request, render_template, redirect
import time
import datetime
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__, template_folder="templates", static_folder='static')
@app.route('/') # here is route
@app.route('/check')
def view_event_all():
#################################################################################################################
# Insert your world in Flask

    conn = psycopg2.connect(host='<000.000.000.000>', # IP or DNS
                            user='<postgres or username>', # user name
                            password='<PASSWORD>', # Database password
                            port='<5432 or your port>', # PostgreSQL default setting is '5432'
                            dbname='<postgres or your dbname>') # PostgreSQL database name
    psql_cursor=conn.cursor(cursor_factory=RealDictCursor)
    sql = "SELECT * FROM <Your Table>;" # Change your table name in PostgreSQL database
    psql_cursor.execute(sql) # Excute query
    res = psql_cursor.fetchall() # Save result

    print(res) # View in your bash shell
    return str(res) # View in your browser
