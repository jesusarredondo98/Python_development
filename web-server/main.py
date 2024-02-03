import store
from fastapi import FastAPI
import pandas as pd
from fastapi.responses import HTMLResponse

#Creamos instancia

def run():
    store.get_categories()

app = FastAPI()

@app.get('/', response_class= HTMLResponse) #se le agrega la ruta donde desde la web se ingresará
def get_list():
   return """
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Inicio Llamativa</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: DodgerBlue;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .container {
            text-align: center;
        }

        h1 {
            color: #2c3e50;
        }

        p {
            color: black;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bienvenido a nuestra Página de Inicio</h1>
        <p>En /contact verás información obtenida de la api fake de platzi.</p>
    </div>
</body>
</html>
    """



@app.get('/contact', response_class=HTMLResponse) #endpoint
def get_list():
    a = store.get_categories()
    return HTMLResponse(content=a)


if __name__ == "__main__":
    run()