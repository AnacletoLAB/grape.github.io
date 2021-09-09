"""
This defines the example `hellos` table for use with sqlalchemy
"""
# Disable "Too few public methods" check
# pylint: disable=R0903


from sqlalchemy import Column, Integer, String, DateTime
from . import BASE, MA


class Hello(BASE):
    """ Keep track of who says hello and when """
    __tablename__ = "hellos"

    id = Column(Integer, primary_key=True)
    when = Column(DateTime)
    who = Column(String)
    another = Column(String)


class HelloSchema(MA.SQLAlchemyAutoSchema): # pylint: disable=too-many-ancestors
    """ Creates a serializer from the sqlalchemy model definition """
    class Meta:
        """ Metaclass """
        model = Hello
        strict = True
