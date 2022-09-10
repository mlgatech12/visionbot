from flask import Flask, redirect, render_template, request, session, abort
from flaskext.mysql import MySQL
from passlib.hash import sha256_crypt
import datetime


app = Flask(__name__)

now=datetime.datetime.now()
app=Flask(__name__,static_url_path="/static")
app.secret_key='visionbot'
mysql=MySQL()


app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='lisara43'
app.config['MYSQL_DATABASE_DB']='visionbot'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)


@app.route("/")  #this sets the route to this page
def home():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/createUser/", methods = ["POST", "GET"])
def createUser():
    if request.method == 'POST':
        _firstName=request.form['fname']
        _lastName=request.form['lname']
        _email=request.form['email']
        _password=sha256_crypt.encrypt((str(request.form['password'])))
        
        conn=mysql.connect()
        cursor=conn.cursor()
        
        
        insert_stmt=("INSERT INTO users (first_name,last_name,email,password ) VALUES (%s,%s,%s,%s)")
        insert_data=(_firstName, _lastName, _email, _password)
           
        cursor.execute(insert_stmt,insert_data)
           
        conn.commit()
        cursor.close()
        conn.close()
    
    
    
    return render_template("login.html", error="")

# @app.route("/login")
# def login():
#     return render_template("login.html", error="")

# @app.route("/login/")
# def login1():
#     return render_template("login.html", error="")


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['username'] = ""
    return render_template("index.html")


@app.route("/logon", methods = ["POST", "GET"])
def userlogin():
    print("userlogin")
    print("request method", request.method)
    
    if request.method == 'POST':
        _userName=request.form['userid']
        
        print("username received = ", _userName)
        
        try:
        
            conn=mysql.connect()
            cursor=conn.cursor()
            
            print("2")
            
            select_stmt=("select * from users where email = %s")
            query_data=(_userName)
               
            cursor.execute(select_stmt,query_data)
            
            print("3")
            data = cursor.fetchone()

            print(data)  
            
            conn.commit()
            cursor.close()
            conn.close()
        
        except Exception as e:
            print(e)
    
        
        
        
        #if sha256_crypt.verify(str(request.form['password']) , data[4]):
        session['logged_in'] = True
        session['username'] = data[1]
        return render_template("index.html")
        
        #else:
        #    error = "Invalid credentials, Try Again."
        #    return redirect("login.html", error=error)
    else:
        return render_template("login.html", error="")
           

@app.route("/persons")
def persons():
    return render_template("persons.html")        

    
@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/search")
def search():
    
    #return render_template('search.html'), {"Refresh": "5.0; url=/searchresult"}

    return render_template('search.html')

@app.route("/searchresult")
def searchresult():
    return render_template('search1.html')


@app.route("/configure")
def configure():
    return render_template('configure.html')


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()