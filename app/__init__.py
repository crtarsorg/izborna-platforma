from flask import Flask,request, g, abort
import os
import ast
import ConfigParser
from logging.handlers import RotatingFileHandler
from flask.ext.babel import Babel
from flask.ext.mail import Mail


mail=Mail()
#Initialize mongo access point

babel = Babel()

def create_app():
    # Here we  create flask instance

    app = Flask(__name__)
    app.secret_key = 'random string'
    # Load application configurations
    load_config(app)

    # Configure logging.
    configure_logging(app)

    # Init modules
    init_modules(app)
    mail.init_app(app)
    # Initialize the app to work with MongoDB



    babel.init_app(app)

    # Get local based on domain name used.
    @babel.localeselector
    def get_locale():
        """Direct babel to use the language defined in the session."""
        return g.get('current_lang', 'sr')


    @app.before_request
    def before():
        if request.view_args and 'lang_code' in request.view_args:
            if request.view_args['lang_code'] not in ('sr', 'en'):
                return abort(404)
            g.current_lang = request.view_args['lang_code']
            request.view_args.pop('lang_code')

    return app

def load_config(app):
    ''' Reads the config file and loads configuration properties into the Flask app.
    :param app: The Flask app object.
    '''
    # Get the path to the application directory, that's where the config file resides.
    par_dir = os.path.join(__file__, os.pardir)
    par_dir_abs_path = os.path.abspath(par_dir)
    app_dir = os.path.dirname(par_dir_abs_path)

    # Read config file
    config = ConfigParser.RawConfigParser()
    config_filepath = app_dir + '/config.cfg'
    config.read(config_filepath)

    app.config['MAIL_SERVER'] = config.get('Mail', 'MAIL_SERVER')
    app.config['MAIL_PORT'] = config.get('Mail', 'MAIL_PORT')
    app.config['MAIL_USE_SSL'] = ast.literal_eval(config.get('Mail', 'MAIL_USE_SSL'))
    app.config['MAIL_USE_TLS'] = ast.literal_eval(config.get('Mail', 'MAIL_USE_TLS'))
    app.config['MAIL_USERNAME'] = config.get('Mail', 'MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = config.get('Mail', 'MAIL_PASSWORD')

    app.config['SERVER_PORT'] = config.get('Application', 'SERVER_PORT')
    app.config['MONGO_DBNAME'] = config.get('Mongo', 'DB_NAME')

    # Logging path might be relative or starts from the root.
    # If it's relative then be sure to prepend the path with the application's root directory path.
    log_path = config.get('Logging', 'PATH')
    if log_path.startswith('/'):
        app.config['LOG_PATH'] = log_path
    else:
        app.config['LOG_PATH'] = app_dir + '/' + log_path

    app.config['LOG_LEVEL'] = config.get('Logging', 'LEVEL').upper()


def configure_logging(app):
    ''' Configure the app's logging.
     param app: The Flask app object
    '''

    log_path = app.config['LOG_PATH']
    log_level = app.config['LOG_LEVEL']

    # If path directory doesn't exist, create it.
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create and register the log file handler.
    log_handler = RotatingFileHandler(log_path, maxBytes=250000, backupCount=5)
    log_handler.setLevel(log_level)
    app.logger.addHandler(log_handler)

    # First log informs where we are logging to.
    # Bit silly but serves  as a confirmation that logging works.
    app.logger.info('Logging to: %s', log_path)


def init_modules(app):
    # Import blueprint modules
    from app.mod_main.views import mod_main
    from app.mod_type.views import mod_type
    from app.mod_api.views import mod_api
    from app.mod_contact.views import mod_contact
    from app.mod_questions.views import mod_questions
    app.register_blueprint(mod_main)
    app.register_blueprint(mod_type)
    app.register_blueprint(mod_api)
    app.register_blueprint(mod_contact)
    app.register_blueprint(mod_questions)



