from entities.Base import Base
from sqlalchemy import Column,Integer,String

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    bio = Column(String(200))
    country = Column(String(20))


    def __repr__(self):
        return "<User(name='%s', country='%s', bio='%s')>" % (
                        self.name, self.country, self.bio)