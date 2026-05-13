import logging
import os
from datetime import datetime

# 1. Create the filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path to the 'logs' folder ONLY
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# 3. Create the full path to the file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True  # CRITICAL for Python 3.8+: This forces your config to work
)

if __name__ == "__main__":
    logging.info("Logging has started")
    print(f"Log written to: {LOG_FILE_PATH}")