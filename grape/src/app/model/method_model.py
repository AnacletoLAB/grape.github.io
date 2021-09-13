"""
This defines the example `hellos` table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903


from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from . import BASE, MA
from sqlalchemy.orm import relationship

class Method(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "methods"

    method_id = Column(Integer, primary_key=True)
    method_name = Column(String)
    version_id = Column(Integer, ForeignKey('version.version_id'))
    human_test_coverage = Column(Float)	
    fuzzer_test_coverage = Column(Float)
    description = Column(String)
    return_type_id = Column(Integer, ForeignKey('type.type_id'))
    created = Column(DateTime)


class VersionsSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = Method
        strict = True
