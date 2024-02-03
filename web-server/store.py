import requests

def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print("El status de la consulta es: " + str(r.status_code))
    print("___________________________")
    #print(r.text)
    #print(type(r.text)) #Verificamos que sea string
    categories = r.json() #Obtenemos el resultado en formato json
    for category in categories:
        print(category["name"])