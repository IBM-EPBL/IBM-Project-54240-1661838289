from site import USER_BASE
from flask import Flask,render_template, request,url_for,redirect,session
from flask import request
import ibm_db
conn = ibm_db.connect ("DATABASE=bludb;HOSTNAME=9938aec0-8105-433e-8bf9-0fbb7e483086.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32459;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=brk74172;PWD=Hope@1234567890;","","")
print(conn)

print("connection successfully...")


app = Flask(__name__)

@app.route("/")
def home():
    if 'email' not in session:
      return redirect (url_for('login'))
    return render_template('home.html',name="home")

@app.route("/about")
def about():
    return render_template('about.html',name="about")

@app.route("/signin")
def signin():
       if request.method == 'POST':
         email = request.form['email']
         password = request.form['password']

         if not email or not password:
           return render_template('signin.html',error='Please fill all fields')
           query = "SELECT * FROM USER WHERE email=?"
           stmt = ibm_db.prepare(conn, query)
           ibm_db.bind_param(stmt,1,email)
           ibm_db.execute(stmt)
           isUser = ibm_db.fetch_assoc(stmt)
           print(isUser,password)

         if not isUser:
          return render_template('signin.html',error='Invalid Credentials')
      
         isPasswordMatch = bcrypt.checkpw(password.encode('utf-8'),isUser['PASSWORD'].encode('utf-8'))

         if not isPasswordMatch:
           return render_template('signin.html',error='Invalid Credentials')

         session['email'] = isUser['EMAIL']
         return redirect(url_for('home'))
    
       
       return render_template('signin.html',name="signin")

@app.route("/signup")
def signup():
     if request.method == 'POST':
       name= request.form['name']
       email= request.form['email']
       password = request.form['password']
       repassword = request.form['repassword']

       if not name or not email or not password or not repassword:
        return render_template('signup.html',error='Please fill all fields')
    
        hash=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        query = "SELECT * FROM USER WHERE name=? OR email =?"
        stmt = ibm_db.prepare(conn, query)
        ibm_db.bind_param(stmt,1,name)
        ibm_db.bind_param(stmt,2,email)
        ibm_db.execute(stmt)
        isUser = ibm_db.fetch_assoc(stmt)
    
     if not isuser:
      insert_sql = "INSERT INTO User(name,email,PASSWORD,repassword) VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, password)
      ibm_db.bind_param(prep_stmt, 4, repassword)
      ibm_db.execute(prep_stmt)
      return render_template('signup.html',success="You can login")
     else:
        return render_template('signup.html',error='Invalid Credentials')
     return render_template('signup.html',name="signup")

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run()

