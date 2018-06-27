#-*- coding: utf-8 -*-
from flask import Flask, render_template
import requests

app= Flask(__name__)

@app.route('/')
def index():
    #jinja2
    palabra = "lebenslangerschicksalschats"
    definicion= "tu tesoro dado de por vida desde tu momento de nacer"

    context={
        'palabra':palabra,
        'definicion':definicion,
        'nombre': 'cesar'
    }
    return render_template('index.html', **context)

@app.route('/word/<value>')
def word(value):
    #Encabezados para la peticion de oxford api, nos pide api_id & api_key en los headers
    headers_value = {
    "app_id": "9a258bda",
    "app_key": "723d33b80902d687f6877ff6f36af42e"
    }
    #hacemos una peticion a la api
    result = requests.get('https://od-api.oxforddictionaries.com/api/v1/entries/es/' + value , headers=headers_value)

    #result = requests.get(f'https://od-api.oxforddictionaries.com/api/v1/entries/es/{value}', headers=headers_value)
    print(result.json())


    if result.status_code != 200:
        print("hubo un problema: ", result.json)
    #si no hubo problema uardar en una variable
    data = result.json()

    #palabra = value

    definiciones = data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]

    context = {
        'palabra': value,
        'definiciones':definiciones,
    }

    #callenge hacerlo con un for en cada uno de los diccionario entries,senses, llegar a definitions
    return render_template('index.html', **context)
#tarea enlistar definiciones pista la manera de hacerlo es con ginja es un valor especial de ginja



if __name__ == '__main__':
    app.run(debug=True)
