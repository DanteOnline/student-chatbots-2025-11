import os
from dotenv import load_dotenv

load_dotenv()
DEFAULT_TIMEOUT = os.getenv('DEFAULT_TIMEOUT', 1)
