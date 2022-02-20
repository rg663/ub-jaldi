import sqlite3
import json
import bottle
import requests
def createparkingtable():
  con=sqlite3.connect("parking.db")
  cursor=con.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS PARKING (NUMBER INT(6), UBIT VARCHAR(30),TIME VARCHAR(30))")
  cursor.execute("INSERT INTO PARKING VALUES('0','a','b')")
  con.commit()
  con.commit()
def insertintoparking(pn,ubn,tm,status):
  con=sqlite3.connect("parking.db")
  cursor=con.cursor()
  cursor.execute("INSERT INTO PARKING VALUES('"+str(pn)+"'"+","+"'"+ubn+"'"+","+"'"+tm+"'"+")")
  con.commit()
def testtable():
  con=sqlite3.connect("parking.db")
  cursor=con.cursor()
  x=cursor.execute("SELECT * FROM parking")
  l=[]
  d={}
  for m in x:
    d={"parkingnumber":m[0],"ubitname":m[1],"time":m[2]}
    l.append(d)
  n1=json.dumps(l)
  con.commit()
  return n1
def finder(personname):
  text=requests.get("https://www.buffalo.edu/search/search.html?searchUrl=https://www.buffalo.edu/search/search.html&query="+personname+"%40buffalo.edu&collection=meta-search&f.Tabs%7Cdb-people=People")
  with open("data.txt","w") as f:
    f.write(text.text)
  with open("data.txt","r") as f:
    for m in f.readlines():
      if('              <a href="mailto:'+personname+'@buffalo.edu">'+personname+'@buffalo.edu</a>'in m):
        
        return 1
    else:
      return 0
finder("vrushaal")
@bottle.route("/")
def server():
  return bottle.static_file("/index.html",root=".")
@bottle.route("/index.html")
def htmltwo():
  return bottle.static_file("/index.html",root=".")
@bottle.route("/script.js")
@bottle.route("/style.css")
def csss():
  return bottle.static_file("/style.css",root=".")
@bottle.route("/script.js")
def scriptserver():
  return bottle.static_file("/script.js",root=".")
@bottle.route("/parking.db")
def databasee():
  return bottle.static_file("/parking.db",root=".")
@bottle.route("/ajax.js")
def ajaxserver():
  return bottle.static_file("/ajax.js",root=".")
@bottle.route("/parking.html")
def parkingtogo():
  return bottle.static_file("/parking.html",root=".")
@bottle.route("/studying.html")
def studyingtogo():
  return bottle.static_file("/studying.html",root=".")
@bottle.route("/eating.html")
def khana():
  return bottle.static_file("/eating.html",root=".")
@bottle.route("/calendar.jpg")
def favicon():
  return bottle.static_file("/calendar.jpg",root=".")
@bottle.route("/lib.jpeg")
def libb():
  return bottle.static_file("/lib.jpeg",root=".")
@bottle.route("/khana.jpeg")
def foood():
  return bottle.static_file("/khana.jpeg",root=".")
@bottle.route("/gaari.jpg")
def vroom():
  return bottle.static_file("/gaari.jpg",root=".")
@bottle.route("/main.py")
def py():
  return bottle.static_file("/main.py",root=".")
@bottle.route("/action_page.php")
def formm():
  return None
bottle.static_file("/action_page.php",root=".")
@bottle.route("/opendisplay")
def opendisplay():
  createparkingtable()
  return testtable()

# #Set up Flask:
# app = Flask(__name__)
# #Set up Flask to bypass CORS:
# cors = CORS(app)
# #Create the receiver API POST endpoint:
# @app.route("/receiver", methods=["POST"])
# def postME():
#  data = request.get_json()
#  data = jsonify(data)
#  return data
# if __name__ == "__main__": 
#  app.run(debug=True)

# Setup flask server
# app = Flask(__name__) 
# # Setup url route which will calculate
# # total sum of array.
# @app.route('/arraysum', methods = ['POST']) 
# def sum_of_array(): 
#     data = request.get_json() 
#     print(data)
  
#     # Data variable contains the 
#     # data from the node server
#     ls = data['array'] 
#     result = sum(ls) # calculate the sum
  
#     # Return data in json format 
#     return json.dumps({"result":result})
   
# if __name__ == "__main__": 
#     app.run(port=5000)

  
@bottle.post("/newdata")
def newparking():
  info=bottle.request.body.read().decode()
  info2=json.loads(info)
  ubitname1=info2["ubitname"]
  #if(finder(ubitname1)==1):
  pname=info2["parkingname"]
  timee=info2["time"]
  insertintoparking(pname,ubitname1,timee)
  print(5)
bottle.run(host="0.0.0.0",port=8080)