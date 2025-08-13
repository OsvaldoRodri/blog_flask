from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def home():
    """
    Renderiza la página principal usando la plantilla index.html.
    """
    return render_template("index.html", name="Osvaldo")


if __name__ == "__main__":
    app.run(debug=True)
