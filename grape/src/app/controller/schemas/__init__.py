"""
This module holds serialization schemas for flask-restplus endpoints
"""
import pkgutil
from pathlib import Path
from importlib import import_module


def register_all_schemas(api):
    """
    Automatically register schemas (that end in _schema.py) defined in this schemas module
    :param api: Api to register models on
    :return: Same Api with registered models
    """
    names = [name for _, name, _ in pkgutil.iter_modules([Path(__file__).parent])
             if name.endswith('_schema')]
    modules = [(import_module('.'.join(['src.app.controller.schemas', tool])), tool)
               for tool in names]
    dicts = [map(mod[0].__dict__.get, mod[0].__all__) for mod in modules]

    for module in dicts:
        for model in module:
            api.models[model.name] = model

    return api
