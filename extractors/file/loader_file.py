# loader_file.py

class FileLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self, mode='r'):
        """Базовый метод загрузки файла, который может быть переопределен в дочерних классах."""
        try:
            with open(self.file_path, mode, encoding='utf-8', errors = 'ignore') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f'Файл не найден: {self.file_path}')
        except PermissionError:
            raise PermissionError(f'Нет прав на чтение файла: {self.file_path}')
        except Exception:
            raise Exception(f'Ошибка при загрузке файла: {self.file_path}')


