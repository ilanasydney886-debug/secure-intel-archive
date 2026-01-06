# Secure Intelligence Archive (SIA) 🛡️

### Overview
The **Secure Intelligence Archive** is a backend API designed to simulate Department of Defense (DoD) data sensitivity protocols. Built with **Python** and **FastAPI**, the system enforces **Role-Based Access Control (RBAC)** to ensure that classified intelligence is only accessible to authorized personnel based on their clearance level.

### Key Features
* **RBAC Logic:** Implements a tiered access system: `1: Unclassified`, `2: Secret`, and `3: Top Secret`.
* **Dynamic Redaction:** Users with insufficient clearance can see document titles, but the content is automatically redacted via the backend logic.
* **RESTful API:** Clean endpoints for retrieving intelligence reports using modern FastAPI standards.
* **Persistent Storage:** Utilizes **SQLAlchemy ORM** and **SQLite** for secure and portable data management.

### Tech Stack
* **Language:** Python 3.9+
* **Framework:** FastAPI
* **Database:** SQLite / SQLAlchemy
* **Server:** Uvicorn

### How It Works
The system compares the `clearance_level` attribute of the requesting `User` against the `required_level` of the `Document`. 

1. **Authorized:** If `User Level >= Document Level`, the full content is returned.
2. **Restricted:** If `User Level < Document Level`, the content is replaced with a "CLASSIFIED/REDACTED" warning.

---
*Note: This project was developed as a technical demonstration of security-first software engineering by Ilana Simpkins, leveraging a background in Critical Intelligence Studies and DoD cybersecurity training.*

### Future Roadmap
- [ ] **JWT Authentication:** Replace simple `user_id` passing with secure JSON Web Tokens.
- [ ] **Logging & Auditing:** Implement a system to log every time a user attempts to access a document they aren't cleared for (Standard DoD auditing).
- [ ] **Frontend Dashboard:** Build a React or Vue.js interface to visualize the redacted archive.# secure-intel-archive
RESTful API built with FastAPI and SQLAlchemy to enforce data sensitivity tiers and secure document retrieval.
