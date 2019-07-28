import flask
import config

import db

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return flask.render_template("index.html", card_info="Display video here.")


if __name__ == '__main__':
    def main():
        # app.run(debug=config.debug)
        app.run(debug=False)

    def db_test_main():
        session = db.SqlAlchemySession()
        user = session.query(db.User).filter_by(id=1).first()
        session.commit()
        print(repr(user))

    main()
    # db_test_main()
