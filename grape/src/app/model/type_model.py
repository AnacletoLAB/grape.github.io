"""
    This defines the type table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903
from sqlalchemy import Column, Integer, String
from . import BASE, MA

class TypeModel(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "types"
    type_id = Column(Integer, primary_key=True)
    type_name = Column(String)

class TypeSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = TypeModel
        strict = True
