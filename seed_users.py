#!/usr/bin/env python3
"""
Seed users from environment variables.

Options:
1) USERS_SEED_JSON: JSON array of objects with keys:
   name, email, password, is_admin (boolean or "true"/"false").

2) USER1_*/USER2_* style:
   USER1_NAME, USER1_EMAIL, USER1_PASSWORD, USER1_IS_ADMIN
   USER2_NAME, USER2_EMAIL, USER2_PASSWORD, USER2_IS_ADMIN

Emails are normalized to lowercase.
Passwords are hashed using app.User.set_password.
"""

import json
import os
import re
from app import app, db, User


def parse_bool(value, default=False):
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def generate_username(email):
    base = re.sub(r"[^a-zA-Z0-9]", "", email.split("@")[0]).lower()
    username = base
    counter = 1
    while User.query.filter_by(username=username).first():
        username = f"{base}{counter}"
        counter += 1
    return username


def load_users_from_env():
    users = []

    users_json = os.getenv("USERS_SEED_JSON")
    if users_json:
        try:
            data = json.loads(users_json)
            if isinstance(data, list):
                users.extend(data)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid USERS_SEED_JSON: {exc}")

    for idx in (1, 2):
        name = os.getenv(f"USER{idx}_NAME")
        email = os.getenv(f"USER{idx}_EMAIL")
        password = os.getenv(f"USER{idx}_PASSWORD")
        is_admin = os.getenv(f"USER{idx}_IS_ADMIN")
        if any([name, email, password, is_admin]):
            users.append(
                {
                    "name": name,
                    "email": email,
                    "password": password,
                    "is_admin": is_admin,
                }
            )

    return users


if __name__ == "__main__":
    users = load_users_from_env()
    if not users:
        raise SystemExit("No users found in env vars. Set USERS_SEED_JSON or USER1_/USER2_ variables.")

    created = []
    updated = []

    with app.app_context():
        for u in users:
            name = (u.get("name") or "").strip()
            email = (u.get("email") or "").strip().lower()
            password = u.get("password")
            is_admin = parse_bool(u.get("is_admin"), default=False)

            if not email or not password:
                updated.append((email or "<missing email>", "skipped (missing email/password)"))
                continue

            existing = User.query.filter_by(email=email).first()
            if existing:
                if existing.is_admin != is_admin:
                    existing.is_admin = is_admin
                    updated.append((email, "admin updated"))
                else:
                    updated.append((email, "exists"))
                continue

            username = generate_username(email)
            user = User(username=username, email=email)
            user.set_password(password)
            user.is_admin = is_admin

            if name:
                parts = name.split()
                user.first_name = parts[0]
                if len(parts) > 1:
                    user.last_name = " ".join(parts[1:])

            db.session.add(user)
            created.append(email)

        db.session.commit()

    print("Created:", created)
    print("Updated/Skipped:", updated)
