import flask

import config

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return flask.render_template("index.html", card_info="Display video here.")

if __name__ == '__main__':
    def main():
        app.run(debug=config.debug)

    main()
