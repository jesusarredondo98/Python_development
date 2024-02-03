### Game project

Para correr el juego debes de seguir las siguientes instrucciones en la terminal

```sh
cd game/
python3 main.py
```

### App project

```sh
git clone
cd app/
python3.11 -m venv env
source env/bin/activate
pip intall -r requirements.txt
python main.py
```

### Web server

Presenta en dockerizacion un api web que se obtiene de [Platzi Fake Api](https://fakeapi.platzi.com/en/about/introduction/) ocupando FastApi, Requests y Docker

```sh
git clone
cd web-server
python3.11 -m venv
source env/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```