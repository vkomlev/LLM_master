# main_dialog.py

class MainDialog:
    def __init__(self):
        # Список доступных ролей
        self.roles = {
            "editor": "выпускающий редактор",
            "critic": "профильный критик",
            "programmer": "программист",
            "teacher": "преподаватель"
        }
        # Список задач
        self.tasks = {
            "analyze_and_format": 
                "Ранее отправлял тебе фраменты распознанного текста PDF документа. Так как текст был распознан, в нем возможны опечатки, нарушение последовательности повествования, неправильное форматирование.  Твоя задача: проанализировать контент и сформировать  форматированный, логически последовательный текст без ошибок, максимально близкий по смыслу к оригиналу. Приступай!",
            "summarize_text": 
                "перескажи текст. Ответ должен быть из 10 предложений."
        }

    def form_context(self, fragments, task_name, role_name):
        """
        Формирует контекст для общения с LLM.
        
        Parameters:
        - fragments (list): Список фрагментов текста для отправки.
        - task_name (str): Название задачи (ключ из self.tasks).
        - role_name (str): Название роли (ключ из self.roles).
        
        Returns:
        - dict: Сформированный контекст.
        """
        messages = []
        role_description = f"Твоя роль - {self.roles.get(role_name, 'пользователь')}."
        messages.append({"role": "system", "content": role_description})
        
        # Добавляем сообщение о начале передачи фрагментов
        intro_message = "Я буду тебе присылать фрагменты текста, ничего не делай, просто запоминай."
        messages.append({"role": "user", "content": intro_message})
        answer_intro = "Хорошо, жду"
        messages.append({"role": "assistant", "content": answer_intro})
        # Добавляем фрагменты
        for i, fragment in enumerate(fragments):
            messages.append({"role": "user", "content": f"Фрагмент {i+1}: {fragment}"})
            answer_intro = "Я запомнил, шли дальше"
            messages.append({"role": "assistant", "content": answer_intro})
        
        # Добавляем задание
        task_message = self.tasks.get(task_name, "Выполни задание.")
        messages.append({"role": "user", "content": task_message})
        
        return messages

    def interact_with_llm(self, llm_module, context, model_name="default"):
        """
        Взаимодействует с конкретным LLM модулем.
        
        Parameters:
        - llm_module (object): Объект модуля LLM.
        - context (dict): Контекст общения.
        - model_name (str): Название модели LLM.
        
        Returns:
        - str: Ответ от LLM.
        """
        return llm_module.send_request(context, model_name=model_name)
