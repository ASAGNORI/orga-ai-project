from sqlalchemy import create_engine, Column, String, DateTime, Integer, ForeignKey, Boolean, JSON, ARRAY, UUID
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import uuid

# Create the base class
Base = declarative_base()

def generate_uuid():
    return uuid.uuid4()

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    email = Column(String, unique=True, index=True)
    nome = Column(String)
    perfil = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    titulo = Column(String)
    descricao = Column(String)
    status = Column(String)
    prioridade = Column(String)
    data = Column(DateTime)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

class Goal(Base):
    __tablename__ = "goals"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    meta = Column(String)
    progresso = Column(Integer)
    prazo = Column(DateTime)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class MindMap(Base):
    __tablename__ = "mind_maps"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    title = Column(String)
    description = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    nodes = Column(JSON)  # Lista de nós do mapa mental
    theme = Column(String, default="default")
    is_public = Column(Boolean, default=False)
    tags = Column(ARRAY(String), default=list)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    content = Column(String)
    type = Column(String)  # user, assistant, system, error
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id"), nullable=True)
    meta_info = Column(JSON)  # Renamed from metadata to avoid conflict
    status = Column(String, default="pending")  # pending, delivered, read, failed
    parent_id = Column(UUID(as_uuid=True), ForeignKey("messages.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv, dotenv_values
    
    # Load environment variables from .env file directly
    config = dotenv_values(".env")
    
    # Get database URL from .env file
    database_url = config.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:54322/postgres")
    print(f"Using database URL: {database_url}")
    
    # Create engine
    engine = create_engine(database_url)
    
    # Create tables
    Base.metadata.create_all(engine)
    print("Tables created successfully!") 