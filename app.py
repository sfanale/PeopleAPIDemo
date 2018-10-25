from flask import (Flask, render_template )

# create application instance
app = Flask(__name__, template_folder="templates")

# create a url for application at /
@app.route('/')
def hello_world():
    return 'Hello World!'

def home():
    """
        This function just responds to the browser ULR
        localhost:5000/

        :return:        the rendered template 'home.html'
        """
    return render_template("home.html")

# if we are running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
