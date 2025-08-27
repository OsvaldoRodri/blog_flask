from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def home():
    """
    Renderiza la página principal usando la plantilla index.html.
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    Renderiza la página about us.
    """
    return render_template("about.html")


@app.route("/contact")
def contact():
    """
    Renderiza la página contactos.
    """
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
