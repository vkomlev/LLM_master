# gigachat_dialog.py

from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

class GigaChatDialog:
    def __init__(self, api_key, verify_ssl=False):
        self.api_key = api_key
        self.verify_ssl = verify_ssl

    def send_request(self, context, model_name = "GigaChat:latest"):
        """
        Отправляет запрос в GigaChat и возвращает ответ.
        
        Parameters:
        - context (list): Контекст для общения с LLM.
        
        Returns:
        - str: Ответ от LLM.
        """
        messages = []
        for msg in context:
            role = MessagesRole.SYSTEM if msg["role"] == "system" else MessagesRole.USER
            messages.append(Messages(role=role, content=msg["content"]))
        
        chat_context = Chat(messages=messages, update_interval=0.1)
        with GigaChat(credentials=self.api_key, verify_ssl_certs=self.verify_ssl, model=model_name) as giga:
            response = giga.chat(chat_context)
            return response.choices[0].message.content
