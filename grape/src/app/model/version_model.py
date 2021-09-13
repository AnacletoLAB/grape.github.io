"""
This defines the example `hellos` table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903


from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from . import BASE, MA


class Version(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "versions"

    version_id = Column(Integer, primary_key=True)
    version_code = Column(String)
    version_name = Column(String)
    created = Column(DateTime)
    methods = relationship("Method")
    modules = relationship("Module")
    method_args = relationship("MethodArgs")

class VersionsSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = Version
        strict = True
