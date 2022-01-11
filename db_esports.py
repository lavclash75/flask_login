import sqlite3
from flask import Flask, render_template


def taula_equips():
    conn = sqlite3.connect('db.db')
    sql = 'SELECT id, nom, any_creacio,pressupost,ciutat from Equips'
    cursor = conn.execute(sql)
    equips =[]
    for row in cursor:
        equip={}
        equip['id'] = row[0]
        equip['nom'] = row[1]
        equip['any_creacio'] = row[2]
        equip['pres'] = row[3]
        equip['ciutat'] = row[4]
        equips.append(equip)
    conn.close()
    return equips
def taula_jocs():
    conn = sqlite3.connect('db.db')
    sql = ('SELECT id, nom, any_llençament,empresa,numero_de_jugadors,img from Jocs')
    cursor= conn.execute(sql)
    jocs=[]
    for row in cursor:
        joc={}
        joc['id'] = row[0]
        joc['nom'] = row[1]
        joc['any_llençament'] = row[2]
        joc['empresa'] = row[3]
        joc['numero_de_jugadors']= row[4]
        joc['img']= row[5]
        jocs.append(joc)
    conn.close()
    return jocs
def taula_jugadors():
    conn = sqlite3.connect('db.db')
    sql=('SELECT id, equip, nom,anys,ciutat from Jugadors')
    cursor= conn.execute(sql)
    jugadors=[]
    for row in cursor:
        jugador={}
        jugador['id'] = row[0]
        jugador['equip']= row[1]
        jugador['nom']= row[2]
        jugador['anys'] = row[3]
        jugador['ciutat']= row[4]
        jugadors.append(jugador)
    conn.close
    return jugadors
def insert_jugadors(nom,anys,equip,ciutat):
    conn = sqlite3.connect('db.db')
    sql = 'INSERT INTO Jugadors(nom,anys,ciutat,equip) VALUES(?,?,?,?)'
    values=[nom,anys,ciutat,equip]
    cursor = conn.execute(sql,values)
    conn.commit()
    conn.close()
def insert_equips(nom,any_creacio,pressupost,ciutat):
    conn = sqlite3.connect('db.db')
    sql = 'INSERT INTO Equips(nom,any_creacio,pressupost,ciutat) VALUES(?,?,?,?)'
    values=[nom,any_creacio,pressupost,ciutat]
    cursor = conn.execute(sql,values)
    conn.commit()
    conn.close()
def insert_jocs(nom,any_llençament,empresa,numero_de_jugadors,img):
    conn = sqlite3.connect('db.db')
    sql = 'INSERT INTO Jocs(nom,any_llençament,empresa,numero_de_jugadors,img) VALUES(?,?,?,?,?)'
    values=[nom,any_llençament,empresa,numero_de_jugadors,img]
    cursor = conn.execute(sql,values)
    conn.commit()
    conn.close()
def del_joc(id):
        conn = sqlite3.connect('db.db')
        sql = 'DELETE FROM Jocs WHERE id= ?'
        values = [id]
        conn.execute(sql,values)
        conn.commit()
        conn.close()
def modify_joc(nom,any_llençament,empresa,numero_de_jugadors,img,id):
    conn = sqlite3.connect('db.db')
    sql = 'UPDATE Jocs SET nom=?, any_llençament=?, empresa=?, numero_de_jugadors=?, img=? WHERE id=?' 
    values=[nom,any_llençament,empresa,numero_de_jugadors,img,id]
    cursor = conn.execute(sql,values)
    conn.commit()
    conn.close()
def get_jocs(id=None):
    
    conn = sqlite3.connect('db.db')
    sql = 'SELECT DISTINCT id, nom, any_llençament, empresa, numero_de_jugadors, img FROM Jocs'
    if id is not None:
        sql += ' WHERE id=' + id
    cursor = conn.execute(sql)
    jocs = []
    for row in cursor:
        joc={}
        joc['id'] = row[0]
        joc['nom'] = row[1]
        joc['any_llençament'] = row[2]
        joc['empresa'] = row[3]
        joc['numero_de_jugadors']= row[4]
        joc['img']= row[5]
        jocs.append(joc)
    conn.close()
    return jocs
def del_equips(id):
        conn = sqlite3.connect('db.db')
        sql = 'DELETE FROM Equips WHERE id= ?'
        values = [id]
        conn.execute(sql,values)
        conn.commit()
        conn.close()
def get_equips(id=None):
    
    conn = sqlite3.connect('db.db')
    sql = 'SELECT DISTINCT id, nom, any_creacio, pressupost, ciutat FROM Equips'
    if id is not None:
        sql += ' WHERE id=' + id
    cursor = conn.execute(sql)
    equips = []
    for row in cursor:
        equip={}
        equip['id'] = row[0]
        equip['nom'] = row[1]
        equip['any_creacio'] = row[2]
        equip['pressupost'] = row[3]
        equip['ciutat']= row[4]
        equips.append(equip)
    conn.close()
    return equips
def get_jugadors(id=None):
    
    conn = sqlite3.connect('db.db')
    sql = 'SELECT DISTINCT id, equip, nom, anys, ciutat FROM Jugadors'
    if id is not None:
        sql += ' WHERE id=' + id
    cursor = conn.execute(sql)
    jugadors= []
    for row in cursor:
        jugador={}
        jugador['id'] = row[0]
        jugador['equip']= row[1]
        jugador['nom'] = row[2]
        jugador['anys'] = row[3]
        jugador['ciutat'] = row[4]
        jugadors.append(jugador)
    conn.close()
    return jugadors
def modify_equips(nom, any_creacio, pressupost, ciutat,id):
    conn = sqlite3.connect('db.db')
    sql = 'UPDATE Equips SET nom=?, any_creacio=?, pressupost=?, ciutat=? WHERE id=?' 
    values=[nom, any_creacio, pressupost, ciutat,id]
    cursor = conn.execute(sql,values)
    conn.commit()
    conn.close()
def modify_jugadors(nom, anys,equip,ciutat,id):
    conn = sqlite3.connect("db.db")
    conn.execute(
        "UPDATE Jugadors SET nom=?, anys=?, equip=?, ciutat=? WHERE id=?",
        (nom,anys,equip,ciutat, id))
    conn.commit()
def del_jugadors(id):
        conn = sqlite3.connect('db.db')
        sql = 'DELETE FROM Jugadors WHERE id= ?'
        values = [id]
        conn.execute(sql,values)
        conn.commit()
        conn.close()
def check_user(username, password):
    conn = sqlite3.connect('db.db')
    sql = "SELECT Username, Password From usuaris Where Username = '{un}' AND Password = '{pw}'", format(un = UN, pw = PW)
    conn.execute(sql)
    conn.commit()
    conn.close()
def save_to_db():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
def comprobar(username, password):
    conn = sqlite3.connect('db.db')
    sql = "Select Password from Usuaris where username =? "
    values = [username]
    cursor = conn.execute(sql, values)
    passwords = []
    for row in cursor:
        passwords.append(row[0])
    conn.close

    password_db = passwords[0]
    if bcrypt.check_password_hash(password_db,password):
        return True
    else:
        return False
def rol(username):
    conn = sqlite3.connect('db.db')
           
    sql2 = "Select Rol from Usuaris where username =? "
    val= [username]
    cursor2 = conn.execute(sql2, val)
    rols=[]
    for row in cursor2:
        rols.append(row[0])
        conn.close
        rol = row[0]
        print(rol)
        return rol
def getusuaris(id=None):
    conn = sqlite3.connect('db.db')
    sql = 'SELECT DISTINCT id, Username, Rol FROM usuaris'
    if id is not None:
        sql += ' WHERE id=' + id
    cursor = conn.execute(sql)
    usuaris= []
    for row in cursor:
        usuari={}
        usuari['id'] = row[0]
        usuari['Username']= row[1]
        usuari['Rol']=[2]
        usuaris.append(usuari)
    conn.close()
    return usuaris
def getusuariusername():
    conn = sqlite3.connect('db.db')
    sql=('SELECT id, Username, Password, Rol from Usuaris')
    cursor= conn.execute(sql)
    usuaris=[]
    for row in cursor:
        usuari={}
        usuari['id'] = row[0]
        usuari['Username']= row[1]
        usuari['Password']= row[2]
        usuari['Rol'] = row[3]
        usuaris.append(usuari)
    conn.close
    return usuaris



def modify_rols(rol, id):
    conn = sqlite3.connect("db.db")
    conn.execute(
        "UPDATE Usuaris SET rol=? WHERE id=?",
        (rol,  id))
    conn.commit()
    conn.close()