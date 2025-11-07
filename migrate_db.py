#!/usr/bin/env python3
"""
Database Migration Script
Adds is_admin column to existing users
"""

import sqlite3

def migrate_database():
    conn = sqlite3.connect('instance/portfolio.db')
    cursor = conn.cursor()
    
    try:
        # Check if column exists
        cursor.execute("PRAGMA table_info(user)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'is_admin' not in columns:
            print("Adding is_admin column...")
            cursor.execute("ALTER TABLE user ADD COLUMN is_admin BOOLEAN DEFAULT 0")
            conn.commit()
            print("✓ is_admin column added successfully!")
        else:
            print("✓ is_admin column already exists")
        
        conn.close()
        print("\n✓ Database migration completed!")
        print("\nNext steps:")
        print("1. Make a user admin: python make_admin.py <username>")
        print("2. Restart the server: python app.py")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.close()

if __name__ == '__main__':
    migrate_database()
