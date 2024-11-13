# load_image.py

from PIL import Image

class ImageLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        """Загружает изображение из файла."""
        try:
            return Image.open(self.file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не найден: {self.file_path}")
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла: {self.file_path}")
        except Exception as e:
            raise RuntimeError(f"Ошибка при загрузке изображения: {e}")
