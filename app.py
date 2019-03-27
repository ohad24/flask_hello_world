# from flask import Flask, render_template
import flask
import cx_Oracle
import pprint

app = flask.Flask(__name__)

# oracle settings
ip = '192.168.1.101'
port = 49161
SID = 'xe'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
con = cx_Oracle.connect("system", "oracle", dsn_tns)
cur = con.cursor()


@app.route('/ohad')
def hello_world():
    cur.execute('select * from hr.EMPLOYEES')
    print(cur.fetchall())
    return 'Hello, World!'


# https://www.tutorialspoint.com/flask/flask_templates.htm
# https://getbootstrap.com/docs/4.3/content/tables/
@app.route('/emp', methods=['GET','POST'])
def emp():
    first_name = '%'
    if flask.request.method == 'POST':
        first_name = flask.request.form['exampleFormControlInput1']
        first_name = '%' + first_name + '%'
    var1 = 'world'
    cur.execute('select first_name, last_name from hr.EMPLOYEES where first_name like :first_name',
                {'first_name': first_name})
    ora_data = cur.fetchall()
    # print(type(ora_data))
    # pprint.pprint(ora_data)
    return flask.render_template('hello.html',
                                 var=var1,
                                 ora_data = ora_data)

app.run(host='0.0.0.0', debug=True)
