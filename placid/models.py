from sqlalchemy import (
    Column,
    Integer,
    Text,
    Date,
    DateTime,
    Boolean,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class SiteParamModel(Base):
    __tablename__ = 'siteparams'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Text)

    def __init__(self,name,value):
       self.name = name
       self.value = value

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=True, nullable=False)
    displayname = Column(Text, nullable=False)
    created = Column(DateTime, nullable=False)
    lastlogin = Column(DateTime)
    passhash = Column(Text, nullable=False)
    vericode = Column(Text)
    verified = Column(Boolean)

    def __init__(self,email,displayname,created,lastlogin,passhash,vericode,verified):
        self.email = email
        self.displayname = displayname
        self.created = created
        self.lastlogin = lastlogin
        self.passhash = passhash
        self.vericode = vericode
        self.verified = verified

class BlogModel(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    content = Column(Text)
    posted = Column(DateTime)
    modified = Column(DateTime)

    def __init__(self,title,content,posted,modified):
        self.title = title
        self.content = content
        self.posted = posted
        self.modified = modified

class CommentModel(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    userid = Column(Integer,ForeignKey('users.id'))
    text = Column(Text)
    posted = Column(DateTime)

    def __init__(self,userid,text,posted):
        self.userid = userid
        self.text = text
        self.posted = posted


