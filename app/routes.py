from flask import Flask             # from the flask module import the Flask
                                    # class is the blue print and object is a house. 


app = Flask(__name__)               # create an instance of the Flask class 
                                    # into the app variable (now an object).



@app.get("/")                       # Flask decorator that creates routes.
def index():                        # Flask calls these "view functions".
    me = {                          # Python dictionary with key/value pairs.
        "first_name": "JoseLuis",
        "last_name": "Sanchez",
        "hobbies": "DIY stuff",
        "is_active": True
    }
    return me                       # When a view function returns a dict. 
                                    # Flask automatically converts is to 
                                    #JSON. 

