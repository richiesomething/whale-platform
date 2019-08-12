from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY']='thisismysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'

    db.init_app(app)

    login_manager =  LoginManager()
    login_manager.login_view = 'pages.login'
    login_manager.init_app(app)

    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from pages import pages as pagesBlueprint
    app.register_blueprint(pagesBlueprint)

    return app


if __name__ == '__main__':
    def main():
        app = create_app()
        app.run(debug=True)

    main()

    def db_test_main():
        session = db.SqlAlchemySession()
        user = session.query(db.User).filter_by(id=1).first()
        session.commit()
        print(repr(user))
    db_test_main()

