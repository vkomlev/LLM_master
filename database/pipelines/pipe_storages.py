# pipe_storages.py

from settings import get_mongo_db_connection

class PipelineStorage:
    def __init__(self):
        # Подключение к коллекциям базы данных
        self.db = get_mongo_db_connection()
        self.pipelines_collection = self.db["pipelines"]
        self.roles_collection = self.db["llm_roles"]
        self.tasks_collection = self.db["llm_tasks"]

    def get_pipelines_collection(self):
        """Возвращает коллекцию для пайплайнов."""
        return self.pipelines_collection

    def get_roles_collection(self):
        """Возвращает коллекцию для ролей LLM."""
        return self.roles_collection

    def get_tasks_collection(self):
        """Возвращает коллекцию для задач LLM."""
        return self.tasks_collection
