from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config


db = SQLAlchemy()
migrate = Migrate()
# --------------------------------------------------------------------------- #
app = Flask(__name__)
# --------------------------------- [edit] ---------------------------------- #
app.config.from_object(config)

# ORM
db.init_app(app)
migrate.init_app(app, db)
# --------------------------------- [edit] ---------------------------------- #
from . import models
# --------------------------------------------------------------------------- #

# 블루프린트
# --------------------------------------------------------------------------- #
from .views import main_views, question_views, answer_views, auth_views, naver_views, movie_views, chat_views
app.register_blueprint(main_views.bp)
app.register_blueprint(question_views.bp)
app.register_blueprint(answer_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(naver_views.bp)
app.register_blueprint(movie_views.bp)
app.register_blueprint(chat_views.bp)

from .filter import format_datetime
app.jinja_env.filters['datetime'] = format_datetime

