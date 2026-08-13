from sqlmodel import Session, select
from database.session import engine, create_tables
from models.user import User
from auth import hash_password

def seed_database():
    create_tables()
    with Session(engine) as session:
        admin_exists = session.exec(select(User).where(User.username == "admin")).first()
        if not admin_exists:
            admin = User(
                username="admin",
                email="admin@clinicguard.com",
                hashed_password=hash_password("Admin123!"),
                full_name="System Admin",
                role="admin",
                is_active=True
            )
            session.add(admin)
            session.commit()
            print("Seed: Default Admin user created (username: admin, password: Admin123!)")

if __name__ == "__main__":
    seed_database()