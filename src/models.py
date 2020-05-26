import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(), nullable=False)
    photo = Column(String) #Because it's a HTML Structure at the end

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    photo = Column(String()) #Because it's a HTML structure at the end
    date = Column(String())
    number_of_likes = Column(Integer)
    number_of_comments = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    story_video = Column(String()) #Because it's a HTML structure at the end
    date = Column(String()) #Actually it's a date but I can't put it as a date without an error
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Comment(Base):
    __tablename__ = 'comment'
    id = id = Column(Integer, primary_key=True)
    content = Column(String())
    person_id = Column(Integer, ForeignKey('person.id'))
    date = Column(String())
    person = relationship(Person)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Like(Base):
    __tablename__ = 'like'
    id = id = Column(Integer, primary_key=True)
    like = Column(String()) #Actually it's a Boolean, but I can't put it as a boolean without an error
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship(Comment)

class Chat(Base):
    __tablename__ = 'chat'
    id = id = Column(Integer, primary_key=True)
    messages = Column(Integer)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Message(Base):
    __tablename__ = 'messages'
    id = id = Column(Integer, primary_key=True)
    content = Column(String())
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    chat_id = Column(Integer, ForeignKey('chat.id'))
    chat = relationship(Chat)
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')