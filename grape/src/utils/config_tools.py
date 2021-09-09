"""
Utilities to help manage the 'grape.config' configuration file
"""
import os
import secrets
import configparser

from src.utils.logging import get_module_logger

CONFIG_FILE_NAME = 'grape.ini'
ENV_PREFIX = 'GR'
NEEDED_SECRETS = ['FLASK_SECRET']

LOGGER = get_module_logger()


def getappenv(relative_name, default=None):
    """
    Helper util to simplify getting an app env variable
    Looks up environment variable that starts with the ENV_PREFIX for this application
    e.g f"{ENV_PREFIX}_{relative_name}"
    :param relative_name:
    :param default: A default to use if nothing found
    :return: env value or default
    """
    return os.getenv(f'{ENV_PREFIX}_{relative_name}', default)


def __env_or_create_secret(use_env=False, env_name=None):
    """
    Helper util to apply conditional for checking environment variables before
    generating new secrets
    :param use_env: Bool, should environment variables be checked before creating new secrets
    :param env_name: name of the environment variables to check
    :return: found or created secret
    """
    if use_env:
        return os.getenv(env_name, secrets.token_hex(32))
    return secrets.token_hex(32)


def generate_secrets(use_env=False):
    """
    Write secret keys to NEEDED_SECRETS fields in CONFIG_FILE_NAME
    :param use_env: Will use environment variables, if they exist, before generating new secrets
    :return:
    """
    config_dict = configparser.ConfigParser(allow_no_value=True)
    config_dict.read(CONFIG_FILE_NAME)
    for key_name in NEEDED_SECRETS:
        LOGGER.warning(f"{key_name} not found, INITIALIZING with `use_env`={use_env}")
        secret = __env_or_create_secret(use_env, f'{ENV_PREFIX}_{key_name}')
        config_dict['MAIN'][key_name] = secret

    with open(CONFIG_FILE_NAME, 'w', encoding='utf-8') as configfile:
        config_dict.write(configfile)


def create_empty_config():
    """
    Creates an empty config file for the user to fill out
    """
    # TODO: Include user prompts
    config_dict = configparser.ConfigParser(allow_no_value=True)

    config_dict['MAIN'] = {
        'FLASK_SECRET': getappenv('FLASK_SECRET'),
        'ADMIN_NAME': getappenv('ADMIN_NAME')
    }

    if getappenv('DATABASE_DIALECT', 'sqlite') != 'sqlite':
        config_dict['DATABASE'] = {
            'DIALECT': getappenv('DATABASE_DIALECT'),
            'USERNAME': getappenv('DATABASE_USERNAME'),
            'PASSWORD': getappenv('DATABASE_PASSWORD'),
            'HOST': getappenv('DATABASE_HOST'),
            'PORT': getappenv('DATABASE_PORT'),
            'DATABSE': getappenv('DATABASE_NAME')
        }
    else:
        config_dict['DATABASE'] = {
            'DIALECT': 'sqlite',
            'PATH': getappenv('DATABASE_PATH',
                              'gr.dev.sqlite.db')
        }

    with open(CONFIG_FILE_NAME, 'w', encoding='utf-8') as configfile:
        config_dict.write(configfile)


def generate_database_uri(params_dict=None, **kwargs):
    """
    Creates a database URI from individual components, lets unwanted options silently pass
      If a parameters dictionary is not provided, this will check kwargs for the needed values.
    :param params_dict: dict with connection parameters:
                        dialect, username, password, host, port, and database as items
    :param kwargs: (optional) keyword arguments representing each key/value in the param_dict
    :return: string representing the database connection URI
    """
    prms = params_dict or kwargs

    if prms['dialect'] == 'sqlite':
        return f"{prms['dialect']}:///" \
            f"{prms.get('path', 'gr.sqlite.db')}"

    return f"{prms['dialect']}://{prms['username']}:{prms['password']}@" \
        f"{prms['host']}:{prms['port']}/{prms['database']}"


def get_config_file_attribute(key, section=None, check_all=False):
    """
    Get the value of an item in the .config static file. Useful for scripts, tasks, etc that
    do not have access to the config object in the flask app context, but which depend on
    manual configuration.
    :param key: The key to look for
    :param section: What section the key is in, defaults to 'MAIN'
    :param check_all: If true, will look in all sections for the key. Returns first found.
    :return: The value of the key in the config file
    """
    section = section or 'MAIN'
    config = configparser.ConfigParser(allow_no_value=True)
    config_was_read = config.read(CONFIG_FILE_NAME)

    if not config_was_read:
        raise FileNotFoundError(f"No file found at {CONFIG_FILE_NAME}")

    if section not in config.sections():
        raise KeyError(f"No section: {section}")

    value = config.get(section, key)

    if not value and check_all:
        for alt_section in config.sections():
            value = config.get(alt_section, key)
            if value:
                log_string = f"'{key}' not found in {section}, instead found in {alt_section}"
                LOGGER.warning(log_string)
                break

    if not value:
        raise KeyError(f"[{section}]: {key} does not have a value")

    return value
