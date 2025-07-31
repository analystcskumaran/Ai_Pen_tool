import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GPT_API_KEY = os.getenv('OPENAI_API_KEY')
    MODEL_NAME = "gpt-4"
    SCAN_THREADS = 5
    VULN_MODEL_PATH = "models/vulnerability_model.pkl"
