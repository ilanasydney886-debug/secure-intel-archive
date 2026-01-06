from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Database Dependency
def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.get("/documents/{doc_id}")
def read_document(doc_id: int, user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    doc = db.query(models.Document).filter(models.Document.id == doc_id).first()

    if not user or not doc:
        raise HTTPException(status_code=404, detail="Document or User not found")

    # THE REDACTION LOGIC
    if user.clearance_level >= doc.required_level:
        # User has high enough clearance
        return {
            "status": "AUTHORIZED",
            "title": doc.title,
            "content": doc.content
        }
    else:
        # User is too low level - we REDACT the content
        return {
            "status": "RESTRICTED ACCESS",
            "title": doc.title,
            "content": " [ REDACTED - CLASSIFIED LEVEL " + str(doc.required_level) + " REQUIRED ] "
        }