import os
import sys

'''
if (not os.environ.get('SQLPassword')):
    print("Missing environment password for the PostgreSQL Account")
    exit(1)
elif (not os.environ.get('TAUCETI_SECRET_KEY')):
    print("Missing environment password for JWT Secret Key")
    exit(1)
'''
if len(sys.argv) < 3:
    print("Usage: python3 run.py [SQLPassword] [TAUCETI_SECRET_KEY]")
    exit(0)

os.environ['SQLPassword'] = sys.argv[1]
os.environ['TAUCETI_SECRET_KEY'] = sys.argv[2]

from app import db, app

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
