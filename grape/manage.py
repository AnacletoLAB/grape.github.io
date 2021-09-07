"""
This is the manager entrypoint to the application
"""

import os
import multiprocessing
from flask_script import Manager

from src.app import create_app
from src.cli.run import RunCommand, GunicornRunCommand
from src.cli.test import RunTestsCommand, RunTestsXMLCommand
from src.cli.celery import StartCeleryWorkersCommand
from src.cli.config import GenerateSecretsCommand, InitConfigCommand

MANAGER = Manager(create_app(os.getenv('FLASK_CONFIG') or None))

# Run the application
MANAGER.add_command('run', RunCommand())
MANAGER.add_command('gunicorn_run', GunicornRunCommand())

# Manage the 'grape.ini' file
MANAGER.add_command('create_secrets', GenerateSecretsCommand)
MANAGER.add_command('init_config', InitConfigCommand)

# Run tests
MANAGER.add_command('test', RunTestsCommand())
MANAGER.add_command('test_xml', RunTestsXMLCommand())


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    MANAGER.run()
