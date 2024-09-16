import yaml
import requests
import openai

class LLM:
    def __init__(self, config_file='AI/config.yaml'):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)

        self.mode = self.config.get('mode', 'openai')
        
        if self.mode == 'openai':
            self.api_key = self.config.get('openai', {}).get('api_key')
            openai.api_key = self.api_key
        elif self.mode == 'custom':
            self.api_url = self.config.get('custom_api', {}).get('url')
            self.api_key = self.config.get('custom_api', {}).get('api_key')
        else:
            raise ValueError(f"Unsupported mode: {self.mode}")

    def request_openai(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response['choices'][0]['message']['content']

    def request_custom_api(self, prompt):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'prompt': prompt
        }
        response = requests.post(self.api_url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json().get('response', 'No response found.')
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def ask(self, prompt):
        if self.mode == 'openai':
            return self.request_openai(prompt)
        elif self.mode == 'custom':
            return self.request_custom_api(prompt)
        else:
            raise ValueError(f"Unsupported mode: {self.mode}")
