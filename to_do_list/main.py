#you should install them in the terminal
#pip install flask
#pip install flask_login
#pip install flask-sqlalchemy

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)