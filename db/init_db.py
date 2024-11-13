from models import Base, engine

def initialize_database():
    """
    Initialize the database by creating all tables defined in the models.
    """
    print("Creating database tables...")
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()
