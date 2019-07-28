import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.orm
import sqlalchemy.ext.declarative

import config

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html

engine = sqlalchemy.create_engine(config.db_path)
SqlAlchemySession = sqlalchemy.orm.sessionmaker(bind=engine)
Base = sqlalchemy.ext.declarative.declarative_base(bind=engine)


class Game(Base):
    __tablename__ = "game"

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(length=32), unique=True)

    def __repr__(self):
        return f"<Game(id={self.id}, name={repr(self.name)})>"


class User(Base):
    __tablename__ = "user"

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    email_id = sqlalchemy.Column(sqlalchemy.VARCHAR(length=128), unique=True)
    user_name = sqlalchemy.Column(sqlalchemy.VARCHAR(length=128), unique=True)
    preferred_name = sqlalchemy.Column(sqlalchemy.VARCHAR(length=128))
    full_name = sqlalchemy.Column(sqlalchemy.VARCHAR(length=128))
    password_hash = sqlalchemy.Column(sqlalchemy.VARCHAR(length=256))       # TODO: Check hash length and tune.
    net_score = sqlalchemy.Column(sqlalchemy.Integer)
    elo = sqlalchemy.Column(sqlalchemy.Integer)

    def __repr__(self):
        return (f"<User(id={self.id}, email_id={repr(self.email_id)}, user_name={repr(self.user_name)}, "
                f"preferred_name={repr(self.preferred_name)}, full_name={repr(self.full_name)}, "
                f"password_hash={self.password_hash}, net_score={self.net_score}, elo={self.elo}, "
                f"password_hash={repr(self.password_hash)}, net_score={self.net_score}), elo={self.elo})>")


class AppSession(Base):
    __tablename__ = "app_session"

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    beg_dt = sqlalchemy.Column(sqlalchemy.DateTime)
    end_dt = sqlalchemy.Column(sqlalchemy.DateTime)
    ip_address = sqlalchemy.Column(sqlalchemy.DateTime)

    def __repr__(self):
        return f"<AppSession(id={self.id}, beg_dt={str(self.beg_dt)}, end_dt={str(self.end_dt)})>"


class GameSession(Base):
    __tablename__ = "game_session"

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    beg_dt = sqlalchemy.Column(sqlalchemy.DateTime)
    end_dt = sqlalchemy.Column(sqlalchemy.DateTime)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    game_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("game.id"))
    app_session_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("app_session.id"))

    def __repr__(self):
        return f"<GameSession(id={self.id}, beg_dt={str(self.beg_dt)}, end_dt={str(self.end_dt)})>"


class Friendship(Base):
    __tablename__ = "friendship"

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    friend_1_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    friend_2_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))


# TODO: Achievements


Base.metadata.create_all()
