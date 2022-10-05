from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def post_buttons():
    if request.method == 'POST':
        if request.form.get('right') == 'right':
            print("right")

        elif request.form.get('left') == 'left':
            print("left")

        elif request.form.get('up') == 'up':
            print("up")

        elif request.form.get('down') == 'down':
            print("down")

        else:
            return render_template("index.html")

    elif request.method == 'GET':

        print("No Post Back Call")
    return render_template("index.html")


def post_http(value: str, https=None) -> None:
    """
    :param value: Value in post HTTP
    :param https: HTTP
    :return: None
    """
    pass


if __name__ == '__main__':
    app.run(debug=True)
