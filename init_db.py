#!/usr/bin/env python3
"""
Database Initialization Script
Run this to create the database and tables
"""

from app import app, db

def init_database():
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✓ Database initialized successfully!")
        print("✓ All tables created")
        print("\nYou can now:")
        print("1. Run the app: python app.py")
        print("2. Create an account through the signup form")
        print("3. Login and access your profile")

if __name__ == '__main__':
    init_database()
