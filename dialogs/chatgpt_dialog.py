# chatgpt_dialog.py

import requests

class ChatGPTDialog:
    def __init__(self, api_key, base_url="https://api.proxyapi.ru/openai/v1", verify_ssl=True):
        self.api_key = api_key
        self.base_url = base_url
        self.verify_ssl = verify_ssl

    def send_request(self, context, model_name="gpt-4o-mini"):
        """
        Отправляет запрос в ChatGPT и возвращает ответ.
        
        Parameters:
        - context (list): Контекст для общения с LLM.
        - model_name (str): Название модели LLM.
        
        Returns:
        - str: Ответ от LLM.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": model_name,
            "messages": [{"role": msg["role"], "content": msg["content"]} for msg in context]
        }

        response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=data, verify=self.verify_ssl)

        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        else:
            raise RuntimeError(f"Ошибка при взаимодействии с ChatGPT: {response.status_code} - {response.text}")
