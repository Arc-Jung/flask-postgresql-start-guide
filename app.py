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
# Insert your thnking
# Flask

    conn = psycopg2.connect(host='<000.000.000.000>', 
                                            user='<postgres or username>', 
                                            password='<PASSWORD>', 
                                            port='<5432 or tour port>', 
                                            dbname='<postgres or your dbname>')
    psql_cursor=conn.cursor(cursor_factory=RealDictCursor)
    sql = "SELECT * FROM <Your Table>;"
    psql_cursor.execute(sql) # Excute query
    res = psql_cursor.fetchall() # Save result

#################################################################################################################
    print(res) # View in your bash shell
    return str(res) # View in your browser