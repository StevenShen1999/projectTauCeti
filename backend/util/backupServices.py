import os
from datetime import datetime

currTime = datetime.now().strftime("%d%m%Y_%H%M")

if os.system("cd ~/databaseBackups >/dev/null 2>&1") != 0:
    print("Path doesn't exist, creating ~/databaseBackups")
    os.system("mkdir ~/databaseBackups")
    print("Path created")

os.system(f"pg_dump tauCetiDB > ~/databaseBackups/{currTime}.bak")
print(f"Databased backup copy created in ~/databaseBackups/{currTime}.bak")