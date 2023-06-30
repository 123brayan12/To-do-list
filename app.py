from flask import Flask, render_template

app=Flask(__name__)

nombre="Brayan"
lista_nombres=['Brayan','Jose','Mathias','Ana','Alonso']

#ruta
@app.route('/')
#vista
def home():
    return render_template('home.html',nom=nombre, lista_nombres=lista_nombres)

@app.route('/about/')
def about():
    return render_template('about.html')
