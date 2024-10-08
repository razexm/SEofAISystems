from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, Integer, String

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:8080/postgres"

# create engine, session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine.connect()
print(engine)

# create models
class Base(DeclarativeBase): pass

class CurrentState(Base):
    __tablename__ = 'current_State'
    
    state = Column(Integer, primary_key=True, nullable=False)

# class Edges(Base):
#     __tablename__ = 'edges'
    
#     Beginning = Column(Integer, primary_key=True, nullable=False)
#     Finish = Column(Integer, primary_key=True, nullable=False)
#     User_Answer = Column(String(255), nullable=False)
    
#     # __table_args__ = (
#     #     PrimaryKeyConstraint('Beginning', 'Finish'),
#     # )
class Edges(Base):
    __tablename__ = 'edges'
    
    beginning = Column(Integer, primary_key=True, nullable=False)
    finish = Column(Integer, primary_key=True, nullable=False)
    user_answer = Column(String(255), nullable=False)

class Questions(Base):
    __tablename__ = 'questions'
    
    state = Column(Integer, primary_key=True, nullable=False)
    question = Column(String(255), nullable=False)
    
    # __table_args__ = (
    #     PrimaryKeyConstraint('State',),
    # )

class Names(Base):
    __tablename__ = 'names'
    
    state = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    
    # __table_args__ = (
    #     PrimaryKeyConstraint('State',),
    # )

# create session
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()
