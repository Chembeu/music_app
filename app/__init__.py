from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_migrate import Migrate

# Initialize extensions (without app)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
socketio = SocketIO()
cors = CORS()

def create_app():
    """Application factory function"""
    app = Flask(__name__)

    # Configure application
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:7629@localhost/music',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_ENABLED=False,
        SECRET_KEY='your-secret-key'
    )

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    cors.init_app(app)

    # Configure login manager
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    from app.login import load_user  # Import user loader function
    # Import models after db initialization


    # Register blueprints (import here to avoid circular imports)
    from app.auth import auth_bp
    from app.routes import main_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app

# Create application instance
app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)