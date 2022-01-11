from flask import Flask, render_template, request, redirect, url_for, flash,g
from functools import wraps

from werkzeug.security import generate_password_hash, check_password_hash
import  flask_bcrypt
import db_esports
from jinja2 import *
from flask import session
import sqlite3
app = Flask(__name__)
bcrypt = flask_bcrypt.Bcrypt(app)
app.config['SESSION_PARMANENT']=False
app.config['SESSION_TYPE']='filesystem'
app.secret_key='fgvdxfqwcgvhbjnkmlñuqwleiyqqwe'



@app.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        username = request.form.get('username')
        password = request.form.get('password')
       
        conn = sqlite3.connect('db.db')
        sql = "Select Password from Usuaris where username =? "
        values = [username]
        cursor = conn.execute(sql, values)
        passwords = []
        for row in cursor:
            passwords.append(row[0])
        conn.close
        password_db = passwords[0]
        if bcrypt.check_password_hash(password_db, password):
            session['logged_in']= True
            session['user'] = username
            rol= db_esports.rol(username)
            session['rol']= rol
            if check_def_admin(username, password):
                session['admin']= True
                return redirect ('/admin/')
            return render_template('index.html')
        
        
        else:
            return render_template('404.html')              
    if request.method == 'GET':
        return render_template('login.html')
def check_def_admin(user, password):
    conn = sqlite3.connect('db.db')
    cursor = conn.execute ('Select password From usuaris where username=?', [user])
    login= cursor.fetchone()[0]
    if bcrypt.check_password_hash(login, password) and password == 'admin' and user == 'admin':
        return True
    else:
        return False


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'logged_in' in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
def admini(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'admin' in session:
            return redirect(url_for('admin'))
        return f(*args, **kwargs)
    return decorated_function
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'logged_in' in session:
            return redirect(url_for('login'))
        if not 'rol' in session:
            return redirect(url_for('login'))
        rol = session['rol']
        if not rol == 'admin':
            return render_template("notadmin.html")
            
        return f(*args, **kwargs)
    return decorated_function
@app.route('/admin/' , methods=['GET', 'POST'])
@admin_required
def admin():
    if request.method == 'GET':
        return render_template('admin.html')
    else:
        conn = sqlite3.connect('db.db')
        username = request.form['username']
        password = request.form['password']
        hashed=  bcrypt.generate_password_hash(password)
        sql = 'UPDATE usuaris SET password=? WHERE username=?' 
        values=[hashed, username]
        cursor = conn.execute(sql,values)
        conn.commit()
        conn.close()
        return redirect('/logout/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        rgu= request.form['rgusername']
        rgp= request.form['rgpassword']
        rol='user'
        generte= bcrypt.generate_password_hash(rgp).decode('utf-8')
        conn= sqlite3.connect('db.db')
        sql = 'INSERT into usuaris (Username,Password,Rol) VALUES(?,?,?)'
        values = [rgu,generte,rol]
        cursor = conn.execute(sql,values)
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('Register.html')
@app.route ('/')
@login_required
def home():
    
    
    return render_template('index.html')
@app.route ('/profile/')
@login_required
def profile():
    if login.username in session:
        user =[]
    
    return render_template('profile.html')


@app.route('/logout/')
@login_required
def logout():
    session.pop('logged_in')
    return redirect(url_for('home'))
@app.route('/equips/')
@login_required
def equips():
    equips = db_esports.taula_equips()
    return render_template('equips.html', datos=equips)
@app.route('/jocs/')
@login_required
def jocs():
    jocs = db_esports.taula_jocs()
    return render_template('jocs.html', datos=jocs)
@app.route('/jugadors/')
@login_required
def jugadors():
    jugadors = db_esports.taula_jugadors()
    return render_template('jugadors.html', datos=jugadors)

@app.route('/insert_jugadors', methods=['GET', 'POST'])
@admin_required
@login_required
def insert_jugadors():
    if request.method == 'GET':  
        return render_template('insert_jugadors.html')
    else:
        nom = request.form['nom']
        anys = request.form['anys']
        equip = request.form['equip']
        ciutat = request.form['ciutat']
        db_esports.insert_jugadors(nom,anys,equip,ciutat)
        return redirect('/jugadors')
@app.route('/insert_equips', methods=['GET', 'POST'])
@admin_required
@login_required
def insert_equips():
    if request.method == 'GET':  
        return render_template('insert_equips.html')
    else:
        nom = request.form['nom']
        any_creacio = request.form['any_creacio']
        pressupost = request.form['pressupost']
        ciutat = request.form['ciutat']
        db_esports.insert_equips(nom,any_creacio,pressupost,ciutat)
        return redirect('/equips')
@app.route('/insert_jocs', methods=['GET', 'POST'])
@admin_required
@login_required
def insert_jocs():
    if request.method == 'GET':  
        return render_template('insert_jocs.html')
    else:
        nom = request.form['nom']
        any_llençament = request.form['any_llençament']
        empresa = request.form['empresa']
        numero_de_jugadors = request.form['numero_de_jugadors']
        img = request.form['/static/img']
        db_esports.insert_jocs(nom,any_llençament,empresa,numero_de_jugadors,img)
        return redirect('/jocs')
@app.route('/jocs/<id>/delete')
@admin_required
@login_required
def del_joc(id):
    db_esports.del_joc(id)
    return redirect(url_for('jocs'))
@app.route('/jocs/<id>/modify', methods=['GET', 'POST'])
@admin_required
@login_required
def modify_joc(id):
    if request.method == 'GET':
        jocs = db_esports.get_jocs(id)
        return render_template('modify_jocs.html',joc=jocs[0] )
    nom = request.form['nom']
    any_llençament = request.form['any_llençament']
    empresa = request.form['empresa']
    numero_de_jugadors = request.form['numero_de_jugadors']
    img = request.form['/static/img']
    db_esports.modify_joc(nom,any_llençament,empresa,numero_de_jugadors,img, id)
    return redirect(url_for('jocs'))
@app.route('/equips/<id>/delete')
@admin_required
@login_required
def del_equips(id):
    db_esports.del_equips(id)
    return redirect(url_for('equips'))
@app.route('/equips/<id>/modify', methods=['GET', 'POST'])
@admin_required
@login_required
def modify_equips(id):
    if request.method == 'GET':
        equips = db_esports.get_equips(id)
        return render_template('modify_equips.html',equip=equips[0] )
    nom = request.form['nom']
    any_creacio = request.form['any_creacio']
    pressupost = request.form['pressupost']
    ciutat = request.form['ciutat']
    db_esports.modify_equips(nom, any_creacio, pressupost, ciutat,id)
    return redirect(url_for('equips'))
@app.route('/jugadors/<id>/modify', methods=['GET', 'POST'])
@admin_required
@login_required
def modify_jugadors(id): 
    if request.method == 'GET':
        jugadors = db_esports.get_jugadors(id)
        return render_template('modify_jugadors.html',jugador=jugadors[0] )
    nom = request.form['nom']
    anys = request.form['anys']
    equip = request.form['equip']
    ciutat = request.form['ciutat']
    db_esports.modify_jugadors(nom,anys,equip,ciutat, id)
    return redirect(url_for('jugadors'))
@app.route('/jugadors/<id>/delete')
@admin_required
@login_required
def del_jugadors(id):
    db_esports.del_jugadors(id)
    return redirect(url_for('jugadors'))
@app.route('/usuaris/', methods=['GET', 'POST'])
@admin_required
@login_required
def mostrarusurais():
     if request.method == 'GET':
        usuaris = db_esports.getusuariusername()
        return render_template('usuari.html', datos=usuaris )
@app.route('/usuaris/<id>/modify', methods=['GET', 'POST'])
@admin_required
@login_required
def modificarrols(id):
    if request.method == 'GET':
        usuaris = db_esports.getusuaris(id)
        return render_template('modify_usuaris.html',usuari=usuaris[0] )
    rol = request.form['rol']
    db_esports.modify_rols(rol,id)
    return redirect(url_for('mostrarusurais'))
    
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000')