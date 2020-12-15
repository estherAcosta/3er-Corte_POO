from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('data.db', check_same_thread=False)
@app.route('/')
def Index():
    return render_template('Index.html')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
    return render_template('login.html')
    email = request.form.get('email')
    password = request.form.get('password')
    usuarios=db.execute("""select * from usuarios where email = ? and passwors = ?"""(email,password,)).fetchone()
    if usuarios is None:
        Flask('Las credenciales no son validas,error')
        return redirect(request.url)
return 'Iniciando Sesion'
@app.route('/Contacto', methods=['GET','POST'])

@app.route('/usuarios')
def usuarios():
    Usuarios = db.execute('select * from Usuarios')
    Usuarios = Usuarios.fetchall()
    return render_template('Usuarios/Listar.html', Usuarios=Usuarios)


#ingrear usuarios
@app.route('/Usuarios/Crear', methods=['GET','POST'])
def Crear_Usuarios():
    if request.method == 'GET':
        return render_template('Usuarios/Crear.html')
    
    Nombres=request.form.get('Nombres')
    Apellidos=request.form.get('Apellidos')
    Email=request.form.get('Email')
    Contraseña=request.form.get('Contraseña')
    cursor=db.cursor()
    cursor.execute("""INSERT INTO Usuarios(
            Nombres,
            Apellidos, 
            Email,
            Contraseña
        )values (?,?,?,?)
    """, (Nombres,Apellidos,Email,Contraseña))
    
    db.commit()
    
    return redirect(url_for('usuarios'))

#eliminar usuarios
@app.route('/Usuarios/Eliminar', methods=['GET','POST'])
def Eliminar():
    if request.method == 'GET':
        return render_template('Usuarios/Eliminar.html')
    Id=request.form.get('Id')
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute("""DELETE FROM Usuarios where Id=?""",(Id))
    db.commit()
    return redirect(url_for('usuarios'))
    
#editar usuarios
@app.route('/Usuarios/Editar', methods=['GET','POST'])
def Editar():
    if request.method == 'GET':
        return render_template('Usuarios/Editar.html')
    Id=request.form.get('Id')
    New_Nombres=request.form.get('nombres')
    New_Apellidos=request.form.get('apellidos')
    New_Email=request.form.get('email')
    New_Contraseña=request.form.get('contraseña')
    cursor = db.cursor()
    cursor.execute("""UPDATE Usuarios SET
                Nombres=?,
                Apellidos=?, 
                Email=?,
                Contraseña=?
                WHERE Id=?
    """,(New_Nombres,New_Apellidos,New_Email,New_Contraseña,Id))
    db.commit()
    return redirect(url_for('usuarios'))

app.run(debug=True)
