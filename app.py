from flask import (Flask, render_template )
import connexion

# create application instance
app = connexion.App(__name__, specification_dir="./")

# read swagger.yml file to configure endpoints
app.add_api('swagger.yml')


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
    app.run(host='0.0.0.0', port=5000, debug=True)
