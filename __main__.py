from flask_api.app import app

# api routes
from flask_api.index import index

# set debug to False in production
if __name__ == "__main__":
    app.run(debug=True)
