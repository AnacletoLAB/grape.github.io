"""
    This defines the methodargs table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903
from sqlalchemy import Column, Integer, String, ForeignKey
from . import BASE, MA

class MethodArgsModel(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "method_args"

    argument_id = Column(Integer, primary_key=True)
    argument_name = Column(String)
    description = Column(String)
    default_value = Column(String)
    method_id = Column(Integer, ForeignKey("versions.version_id"))
    return_type_id = Column(Integer, ForeignKey("types.type_id"))

class MethodArgsSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = MethodArgsModel
        strict = True
