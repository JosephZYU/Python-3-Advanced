# https://youtu.be/5iWhQWVXosU

import os

# db == database

# 🧠 os.environ.get()
# 😎 Locate from the .zprofile

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)
