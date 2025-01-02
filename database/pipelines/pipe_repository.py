# pipe_repository.py

from database.pipelines.pipe_storages import PipelineStorage

class PipelineRepository:
    def __init__(self):
        self.storage = PipelineStorage()

    def add_pipeline(self, pipeline):
        """
        Добавляет новый пайплайн в коллекцию.
        
        Parameters:
        - pipeline (dict): Словарь с данными пайплайна.
        """
        self.storage.get_pipelines_collection().insert_one(pipeline)

    def get_pipeline_by_id(self, pipeline_id):
        """
        Получает пайплайн по идентификатору.
        
        Parameters:
        - pipeline_id (str): Уникальный идентификатор пайплайна.
        
        Returns:
        - dict: Найденный пайплайн или None.
        """
        return self.storage.get_pipelines_collection().find_one({"_id": pipeline_id})

    def add_role(self, role):
        """
        Добавляет новую роль LLM в коллекцию.
        
        Parameters:
        - role (dict): Словарь с данными роли.
        """
        self.storage.get_roles_collection().insert_one(role)

    def get_role_by_id(self, role_id):
        """
        Получает роль по идентификатору.
        
        Parameters:
        - role_id (str): Уникальный идентификатор роли.
        
        Returns:
        - dict: Найденная роль или None.
        """
        return self.storage.get_roles_collection().find_one({"_id": role_id})

    def add_task(self, task):
        """
        Добавляет новую задачу LLM в коллекцию.
        
        Parameters:
        - task (dict): Словарь с данными задачи.
        """
        self.storage.get_tasks_collection().insert_one(task)

    def get_task_by_id(self, task_id):
        """
        Получает задачу по идентификатору.
        
        Parameters:
        - task_id (str): Уникальный идентификатор задачи.
        
        Returns:
        - dict: Найденная задача или None.
        """
        return self.storage.get_tasks_collection().find_one({"_id": task_id})
