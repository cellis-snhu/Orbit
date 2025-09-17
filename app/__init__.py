from flask import Flask


def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config.update(
            TESTING=True,
        )

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app
