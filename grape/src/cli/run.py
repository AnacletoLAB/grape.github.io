"""
Starts the dev server
"""

from flask_script import Command, Option
from src.app import create_app
from .utils import start_subprocess_and_wait
from ..config import DEFAULT_CONFIG


class RunCommand(Command):
    """
    The main entrypoint to running the app
    :return: None
    """

    option_list = (
        Option('--config', '-c', dest='config', default=None),
        Option('--host', '-h', dest='host', default=None),
        Option('--port', '-p', dest='port', default=None),
    )

    def run(self, config=None, host=None, port=None):  # pylint: disable=E0202,W0221
        """ invoked by the command """
        host = host or DEFAULT_CONFIG.HOST
        port = port or DEFAULT_CONFIG.PORT
        app = create_app(config_name=config)
        app.run(host=host, port=port)


class GunicornRunCommand(Command):
    """
    Gunicorn version of RunCommand for use in the docker container
    """

    def run(self):  # pylint: disable=E0202
        gunicorn_command = 'gunicorn -b 0.0.0.0:8000 wsgi:application'
        start_subprocess_and_wait(gunicorn_command)
