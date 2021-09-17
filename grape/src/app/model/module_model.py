"""
    This defines the module table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903
from src.app.model.version_model import VersionModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from . import BASE, MA


class ModuleModel(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "modules"
    module_id = Column(Integer, primary_key=True)
    module_name = Column(String)
    created = Column(DateTime)
    version_id = Column(Integer, ForeignKey("versions.id"))
    version = relationship(VersionModel)

class ModuleSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = ModuleModel
        strict = True
