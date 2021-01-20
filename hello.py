"""Cloud Foundry test"""
from flask import Flask, request, render_template, jsonify
import os
import psycopg2
import csv
import json


#from os.path import exists
#from os import makedirs

#url = urlparse.urlparse(os.environ.get('DATABASE_URL'))
#db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
#schema = "schema.sql"
#conn = psycopg2.connect(db)

#cur = conn.cursor()


port = 5432

app = Flask(__name__)

wport = int(os.getenv("PORT"))

# 2020.12.18
@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(wport)

# 2021.01.01
# 2021.01.08 : WORKING : JW
@app.route('/meow')
def meow():
    # conn_string = "host='suleiman.db.elephantsql.com' dbname='ykkrfsmz' user='ykkrfsmz' password='3q9KA8PBaS1rjrkeRYyCy9ip_VWxZxNo' port=5432"

    # print the connection string we will use to connect
    # print ("Connecting to database %s" % conn_string)
    print ("Connecting to database!")

    # get a connection, if a connect cannot be made an exception will be raised here
    # conn = psycopg2.connect(conn_string)
    conn = psycopg2.connect("dbname='ykkrfsmz' user='ykkrfsmz' host='suleiman.db.elephantsql.com' password='3q9KA8PBaS1rjrkeRYyCy9ip_VWxZxNo'")

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cur = conn.cursor()

    cur.execute( "SELECT pname, pplanet, pgender FROM sithlord" )

    # results = cur.fetchall()
    vname = cur.fetchone()
    buzz = vname[0] +' '+ vname[1] +' '+ vname[2]

    return buzz

# 2021.01.06
# 2021.01.08 : WORKING : JW
@app.route("/apicat")
def apicat():
    """
    places.csv:
    city,attraction,gif
    Rome,Trevi Fountain,http://giphygifs.s3.amazonaws.com/media/FPLcTlwoaszC/giphy.gif
    Venice,St. Mark's Basilica,https://media.giphy.com/media/xT9Ighh4t2CyU4PhaE/giphy.gif
    Florence,Ponte Vecchio,https://media.giphy.com/media/TkLCp8NeGuKpa/giphy.gif

    Desired output:
    [
      {
        "city": "Rome",
        "attraction": "Trevi Fountain",
        "gif": "http://giphygifs.s3.amazonaws.com/media/FPLcTlwoaszC/giphy.gif"
      },
      {
        "city": "Venice",
        "attraction": "St. Mark's Basilica",
        "gif": "https://media.giphy.com/media/xT9Ighh4t2CyU4PhaE/giphy.gif"
      },
      {
        "city": "Florence",
        "attraction": "Ponte Vecchio",
        "gif": "https://media.giphy.com/media/TkLCp8NeGuKpa/giphy.gif"
      }
    ]
    
    Current message:
    IndexError
    IndexError: list assignment index out of range
    """
    csvFilePath = 'places.csv'
    # jsonFilePath = 'meowmix.json'
    
    bigdata = []
    with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            data = {}
            xa = rows['city']
            xb = rows['attraction']
            xc = rows['gif']
            data['city'] = xa
            data['attraction'] = xb
            data['gif'] = xc
            bigdata.append(data)
            
    """
    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))
    """
    
    vb = (json.dumps(bigdata, indent=4))
    
    return vb
    
    """
    with open('./places.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        places = []
        for row in data:
            if not first_line:
                places.append({
                    "city": row[0],
                    "attraction": row[1],
                    "gif_url": row[2]
                })
            else:
                first_line = False
    # return render_template("index.html", places=places)
    print jsonify(places)
    """
  
# 2021.01.05
@app.route('/meowkeys')
def meowkeys():
    print (os.environ.keys())

# 2021.01.05
@app.route('/meowtest')
def meowx():
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect(database=url.path[1:],
      user=url.username,
      password=url.password,
      host=url.hostname,
      port=url.port
    )

# 2021.01.05
@app.route('/meowtoo')
def meowtoo():
	#Define our connection string    
	conn_string = "host='jedimaster.cpjt5qwricvv.us-east-1.rds.amazonaws.com' dbname='jedimaster' user='pgmaster' password='sinciyslave123'"

	# print the connection string we will use to connect
	print ("Connecting to database\n	->%s" % (conn_string))

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print ("Connected!\n")

# 2021.01.04
@app.route('/boomtest')
def boom():
    conn = psycopg2.connect(database=db, user=user, password=password, host=host, port=5432)
    # cursor = conn.cursor()
    # cursor.execute('SELECT COUNT(MemberID) as count FROM Members WHERE id = 1')
    # row = cursor.fetchone()
    # conn.close()
    # print(row)
    return "meow"

# 2021.01.01
@app.route('/zulu')
def zulu():
    environment_variables = { key: os.environ[key] for key in os.environ.keys() }
    # return jsonify(environment_variables["VCAP_SERVICES"]["elephantsql"]["uri"])
    return(os.environ['VCAP_SERVICES'][0])

# 2020.12.24
@app.route("/name/<name>")
def get_book_name(name):
    return "name : {}".format(name)

# 2020.12.24
@app.route("/details")
def get_book_details():
    author = request.args.get('author')
    published = request.args.get('published')
    return "Author : {}, Published: {}".format(author,published)

# 2020.12.21
@app.route('/contacts')
def contacts():
    return 'Contacts'

# 2020.12.24
incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

# 2020.12.24
@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)



# 2020.12.11
if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=wport)
