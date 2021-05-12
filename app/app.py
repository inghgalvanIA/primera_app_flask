#importar flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
   print("Antes de la peticion..")

@app.after_request
def after_request(response):
   print("Despues de la peticion...")
   return response

@app.route('/')
def index():
    print("Estamos realizando la peticion")
    #return render_template('index.html',titulo='Index 1')
    #return "Codigo Facilito"
    data ={
        'titulo':'Pagina orincipal',
        'encabezado':'Bienvenido a Flask'
    }

    return render_template('index.html',data=data)

@app.route('/contacto')
def contacto():
    data ={
        'titulo':'Contacto',
        'encabezado':'Bienvenido a Flask'
    }

    return render_template('contacto.html',data=data)


@app.route('/saludo/<nombre>')
def saludo(nombre):
   return f"Hola, {nombre}"


@app.route('/suma/<int:valor_uno>/<int:valor_dos>')
def suma(valor_uno,valor_dos):
    
   return f"EL resultado es: {(valor_uno + valor_dos)}"

@app.route('/perfil/<nombre>/<int:edad>')
def method_name(nombre,edad):

   return f"Hola {nombre} tu edad es: {edad}"

@app.route('/lenguajes')
def lenguajes():
   data={
       "Hay_lenguajes":True,
       "lenguajes":["PHP","Python","Swift","Java","C#","Java"]
   }
   return render_template('lenguajes.html',data=data)


@app.route('/datos')
def datos():
   #print(request.args)
   valor1 = request.args.get("valor1")
   valor2 = request.args.get("valor2")
   return f"Estos son los datos: {valor1} y {valor2}"

@app.route('/hola')
def hola_mundo():
    return "Hola mundo"



if __name__=='__main__':
    app.run(debug=True)

    