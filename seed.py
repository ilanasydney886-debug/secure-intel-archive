import models
from database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# 1. Create Mock Users
users = [
    models.User(username="intern_smith", clearance_level=1), # Unclassified
    models.User(username="agent_simpkins", clearance_level=2), # Secret
    models.User(username="director_jones", clearance_level=3) # Top Secret
]

# 2. Create Mock Intel Documents
docs = [
    models.Document(title="Office Menu", content="Pizza Friday.", required_level=1),
    models.Document(title="Project X-Ray", content="Satellite coordinates...", required_level=2),
    models.Document(title="Deep Space Intel", content="Aliens are real.", required_level=3)
]

db.add_all(users)
db.add_all(docs)
db.commit()
db.close()

print("Database seeded successfully! You have users and classified files ready.")