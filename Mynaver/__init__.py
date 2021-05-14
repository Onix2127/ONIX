from flask import Flask

# --------------------------------- [edit] ---------------------------------- #
def create_app():
    app = Flask(__name__)

    from .Naver import movie_views
    app.register_blueprint(movie_views.bp)

    return app
# --------------------------------------------------------------------------- #

