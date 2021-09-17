"""
This defines the class table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from src.app.model.module_model import ModuleModel
from . import BASE, MA

class ClassModel(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "classes"
    class_id = Column(Integer, primary_key=True)
    class_name = Column(String)
    description = Column(String)
    module_id = Column(Integer, ForeignKey("modules.module_id"))
    module = relationship(ModuleModel)

class ClassSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = ClassModel
        strict = True
