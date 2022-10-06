from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_folder='static')


@app.route('/', methods=["GET", "POST"])
def post_buttons():
    spisok_name_move = ['right',
                        'left',
                        'stop',
                        'up',
                        'down', ]

    if request.method == 'POST':
        for elem in spisok_name_move:
            if request.form.get(elem) == elem:
                print(elem)
                break

        else:
            return render_template("index.html", )

    elif request.method == 'GET':

        print("No Post Back Call")
    return render_template("index.html")


def post_http(value: str, https=None) -> None:
    """
    :param value: Value in post HTTP
    :param https: HTTP
    :return: None
    """
    requests.post(https, data=value)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
