"""
This defines the example `hellos` table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from . import BASE, MA
from sqlalchemy.orm import relationship

class MethodArgs(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "method_args"

    argument_id = Column(Integer, primary_key=True)
    argument_name = Column(String)
    description = Column(String)
    default_value = Column(String)
    method_id = Column(Integer, ForeignKey('version.version_id'))
    return_type_id = Column(Integer, ForeignKey('type.version_id'))


class VersionsSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = MethodArgs
        strict = True
