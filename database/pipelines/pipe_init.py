
from settings import get_mongo_db_connection


def initialize_database():
    """
    Инициализация структуры базы данных и заполнение начальных данных.
    """
    # Подключаемся к БД
    db = get_mongo_db_connection()

    # Создаем коллекции
    pipelines_collection = db["pipelines"]
    roles_collection = db["llm_roles"]
    tasks_collection = db["llm_tasks"]

    # Очистка существующих данных (при необходимости)
    pipelines_collection.drop()
    roles_collection.drop()
    tasks_collection.drop()

    # Инициализация данных

    # Роли
    roles = [
        {"_id": "editor", "name": "editor", "description": "Выпускающий редактор"},
        {"_id": "critic", "name": "critic", "description": "Профильный критик"},
        {"_id": "programmer", "name": "programmer", "description": "Программист"},
        {"_id": "teacher", "name": "teacher", "description": "Преподаватель"}
    ]
    roles_collection.insert_many(roles)

    # Задачи
    tasks = [
        {
            "_id": "analyze_and_format",
            "name": "analyze_and_format",
            "description": "Присылаю тебе распознанный текст PDF документа. Так как текст был распознан, в нем возможны опечатки, нарушение последовательности повествования, неправильное форматирование. Твоя задача: проанализировать контент и сформировать форматированный, логически последовательный текст без ошибок, максимально близкий по смыслу к оригиналу."
        },
        {
            "_id": "summarize_text",
            "name": "summarize_text",
            "description": "Перескажи текст. Ответ должен быть из 10 предложений."
        }
    ]
    tasks_collection.insert_many(tasks)

    print("База данных инициализирована и заполнена начальными данными!")


