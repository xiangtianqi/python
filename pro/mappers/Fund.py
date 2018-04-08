# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Myfund(Base):
    __tablename__ = 'myfund'

    fcode = Column(String(20), primary_key=True)
    fname = Column(String(20))
    NAV = Column(Numeric(5, 4))
    ACCNAV = Column(Numeric(5, 4))
    updatetime = Column(DateTime)
    fdate = Column(DateTime)
