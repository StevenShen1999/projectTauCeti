from app import db, app
import os

if (not os.environ.get('SQLPassword')):
    print("Missing environment password for the PostgreSQL Account")
    exit(1)
elif (not os.environ.get('TAUCETI_SECRET_KEY')):
    print("Missing environment password for JWT Secret Key")
    exit(1)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
