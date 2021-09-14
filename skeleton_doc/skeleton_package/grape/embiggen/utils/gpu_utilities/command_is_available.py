from typing import *


def command_is_available(command_name: str) -> bool:
    """Return whether given bash command is available in PATH.

    Parameters
    ------------------
    command_name: str,
        The command to check availability for.

    Returns
    ------------------
    Boolean representing if the command is available in PATH.
    """
