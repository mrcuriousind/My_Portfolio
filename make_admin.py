#!/usr/bin/env python3
"""
Make a user an admin
Usage: python make_admin.py <username_or_email>
"""

import sys
from app import app, db, User

def make_user_admin(identifier):
    with app.app_context():
        # Try to find user by username or email
        user = User.query.filter(
            (User.username == identifier) | (User.email == identifier)
        ).first()
        
        if not user:
            print(f"❌ User not found: {identifier}")
            print("\nAvailable users:")
            users = User.query.all()
            for u in users:
                admin_badge = " [ADMIN]" if u.is_admin else ""
                print(f"  - {u.username} ({u.email}){admin_badge}")
            return False
        
        if user.is_admin:
            print(f"✓ {user.username} is already an admin!")
            return True
        
        user.is_admin = True
        db.session.commit()
        print(f"✓ {user.username} is now an admin!")
        print(f"\nAccess admin panel at: http://127.0.0.1:5000/admin")
        return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python make_admin.py <username_or_email>")
        print("\nExample:")
        print("  python make_admin.py john")
        print("  python make_admin.py john@example.com")
        sys.exit(1)
    
    identifier = sys.argv[1]
    make_user_admin(identifier)
