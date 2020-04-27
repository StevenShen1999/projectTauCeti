import os
from datetime import datetime

currTime = datetime.now().strftime("%d%m%Y_%H%M")
os.system(f"pg_dump tauCetiDB > ~/databaseBackups/{currTime}.bak")