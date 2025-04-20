from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Boolean, Float, JSON, Table, ARRAY
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=generate_uuid)
    email = Column(String, unique=True, index=True)
    nome = Column(String)
    perfil = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    tasks = relationship("Task", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    mind_maps = relationship("MindMap", back_populates="user")
    messages = relationship("Message", back_populates="user")

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(String, primary_key=True, default=generate_uuid)
    titulo = Column(String)
    descricao = Column(String)
    status = Column(String)
    prioridade = Column(String)
    data = Column(DateTime)
    user_id = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="tasks")
    messages = relationship("Message", back_populates="task")

class Goal(Base):
    __tablename__ = "goals"
    
    id = Column(String, primary_key=True, default=generate_uuid)
    meta = Column(String)
    progresso = Column(Integer)
    prazo = Column(DateTime)
    user_id = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="goals")

class MindMap(Base):
    __tablename__ = "mind_maps"
    
    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String)
    description = Column(String)
    user_id = Column(String, ForeignKey("users.id"))
    nodes = Column(JSON)  # Lista de nós do mapa mental
    theme = Column(String, default="default")
    is_public = Column(Boolean, default=False)
    tags = Column(ARRAY(String), default=list)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="mind_maps")

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(String, primary_key=True, default=generate_uuid)
    content = Column(String)
    type = Column(String)  # user, assistant, system, error
    user_id = Column(String, ForeignKey("users.id"))
    task_id = Column(String, ForeignKey("tasks.id"), nullable=True)
    meta_info = Column(JSON)
    status = Column(String, default="pending")  # pending, delivered, read, failed
    parent_id = Column(String, ForeignKey("messages.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="messages")
    task = relationship("Task", back_populates="messages")
    replies = relationship("Message", 
                         backref=relationship("parent", remote_side=[id]),
                         cascade="all, delete-orphan") 