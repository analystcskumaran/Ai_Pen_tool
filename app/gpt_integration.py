import openai
from config.settings import Config
from config.prompts import SCAN_REPORT_PROMPT

class GPTIntegration:
    def __init__(self):
        openai.api_key = Config.GPT_API_KEY

    def generate_report(self, scan_results: dict) -> str:
        response = openai.ChatCompletion.create(
            model=Config.MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a cybersecurity expert."},
                {"role": "user", "content": SCAN_REPORT_PROMPT.format(scan_results=scan_results)}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
