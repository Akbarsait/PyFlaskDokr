from flask import Flask

def create_app():
    """
    Create a Flask application using the app pattern.
    """
    app = Flask(__name__)

    @app.route('/')
    def index():
        """
        Render a Hello World response.
        :return: Flask response
        """
        return 'Welcome to PyFlaskDokr Series!'

    return app

  