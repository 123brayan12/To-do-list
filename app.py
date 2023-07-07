from flask import Flask, render_template,request,redirect

app=Flask(__name__)

nombre="Brayan"
lista_tareas=[]

#ruta
@app.route('/')
#vista
def home():
    return render_template('home.html',nom=nombre, lista_tareas=lista_tareas )

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/agregar', methods=['GET','POST'] )
def agregar():
    if request.method=='POST':
        nueva_tarea=request.form.get('tarea')
        lista_tareas.append(nueva_tarea)
    return redirect('/')
