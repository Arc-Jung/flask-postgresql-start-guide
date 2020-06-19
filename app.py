from flask import Flask, request, render_template, redirect
import time
import datetime
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__, template_folder="templates", static_folder='static')
@app.route('/')
@app.route('/check')
def view_event_all():
#################################################################################################################
# Insert your thnking
# Lambda & flask


    conn = psycopg2.connect(host='<000.000.000.000>', 
                                            user='<postgres>', 
                                            password='<PASSWORD>', 
                                            port='<5432 or tour port>', 
                                            dbname='<postgres or your dbname>')
    psql_cursor=conn.cursor(cursor_factory=RealDictCursor)
    sql = "SELECT * FROM event;"
    psql_cursor.execute(sql) # Excute query
    res = psql_cursor.fetchall() # Save result


#################################################################################################################
    print(res)
    return str(res)
