import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#Creamos instancia

app = FastAPI()

@app.get('/') #se le agrega la ruta donde desde la web se ingresará
def get_list():
    return [1,2,3,]

@app.get('/contact',response_class=HTMLResponse) #endpoint
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>

    """

def run():
    store.get_categories()

if __name__ == "__main__":
    run()