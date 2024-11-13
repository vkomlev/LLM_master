# save_file.py

class FileSaver:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, content, mode='w'):
        """
        Сохраняет переданное содержимое в текстовый файл.
        
        Parameters:
        - content (str): текст для сохранения.
        - mode (str): режим записи ('w' для перезаписи, 'a' для добавления). По умолчанию 'w'.
        """
        try:
            with open(self.file_path, mode, encoding='utf-8', errors = 'ignore') as file:
                file.write(content)
            print(f"Файл успешно сохранен: {self.file_path}")
        except PermissionError:
            raise PermissionError(f'Нет прав на запись в файл: {self.file_path}')
        except Exception as e:
            raise RuntimeError(f'Ошибка при сохранении файла: {self.file_path} - {e}')
