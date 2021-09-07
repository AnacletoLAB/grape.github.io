"""
This module contains the configuration environments for the flask app
"""

# The next line disables specific pylint checking
# pylint: disable=W0223, R0903, W0511
# TODO: Remove previous lines when config file attributes and methods are fully implemented


import os
import configparser

from src.utils.config_tools import CONFIG_FILE_NAME, generate_secrets, create_empty_config, \
    generate_database_uri

BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Try to read the grape.ini file
_CFG = configparser.ConfigParser(allow_no_value=True)
_CFG_READ = _CFG.read(CONFIG_FILE_NAME)

# If nothing read, create it
if not _CFG_READ:
    create_empty_config()
    _CFG.read(CONFIG_FILE_NAME)

# Create secrets if not present
if not _CFG.get('MAIN', 'FLASK_SECRET'):
    generate_secrets()
    _CFG.read(CONFIG_FILE_NAME)


class Config:
    """ This is the base config that's used by all other configs """

    # Defaults
    ENV = 'Default'
    DEBUG = False
    TESTING = False
    LOG_LEVEL = 'DEBUG'
    HOST = _CFG.get('MAIN', 'default_host', fallback='0.0.0.0')
    PORT = _CFG.get('MAIN', 'default_port', fallback=8000)

    # Secrets
    SECRET_KEY = _CFG.get('MAIN', 'FLASK_SECRET')


    ERROR_404_HELP = False
    RESTPLUS_MASK_SWAGGER = False
    SQLALCHEMY_DATABASE_URI = generate_database_uri(dict(_CFG.items('DATABASE')))


class DevelopmentConfig(Config):
    """ Development Specific Config """
    ENV = 'Development'
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

    if _CFG.has_section('DATABASE_DEVELOPMENT'):
        SQLALCHEMY_DATABASE_URI = generate_database_uri(dict(_CFG.items('DATABASE_DEVELOPMENT')))


class TestingConfig(Config):
    """ Testing Specific Config """
    ENV = 'Testing'
    DEBUG = True
    TESTING = True
    LOG_LEVEL = 'INFO'
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    if _CFG.has_section('DATABASE_TESTING'):
        SQLALCHEMY_DATABASE_URI = generate_database_uri(dict(_CFG.items('DATABASE_TESTING')))


class ProductionConfig(Config):
    """ Production Config. WARNING: BE CAREFUL """
    ENV = 'Production'
    DEBUG = False
    LOG_LEVEL = 'ERROR'

    # TODO: Use a production quality database in production
    if _CFG.has_section('DATABASE_PRODUCTION'):
        SQLALCHEMY_DATABASE_URI = generate_database_uri(dict(_CFG.items('DATABASE_PRODUCTION')))


DEFAULT_CONFIG = DevelopmentConfig  # pylint: disable=C0103

CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

KEY = Config.SECRET_KEY
