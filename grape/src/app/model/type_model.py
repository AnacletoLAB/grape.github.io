"""
This defines the example `hellos` table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relation, relationship
from . import BASE, MA


class Type(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "types"
    type_id = Column(Integer, primary_key=True)
    type_name = Column(String)
    methods = relationship("Method")
    method_args = relationship("MethodArgs")


class VersionsSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = Type
        strict = True
