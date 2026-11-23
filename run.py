#run.py
#En tu compu: python run.py
#En Rnder:   gunicorn run:app
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config["MODO_DESARROLLO"], port=5000)