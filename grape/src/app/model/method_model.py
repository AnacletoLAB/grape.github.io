"""
    This defines the method table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903
from src.app.model.type_model import TypeModel
from src.app.model.version_model import VersionModel
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from . import BASE, MA

class MethodModel(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "methods"

    method_id = Column(Integer, primary_key=True)
    method_name = Column(String)
    version_id = Column(Integer, ForeignKey("versions.id"))
    version = relationship(VersionModel)
    human_test_coverage = Column(Float)
    fuzzer_test_coverage = Column(Float)
    description = Column(String)
    return_type_id = Column(Integer, ForeignKey("types.type_id"))
    return_types = relationship(TypeModel)
    created = Column(DateTime)

class MethodSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = MethodModel
        strict = True
