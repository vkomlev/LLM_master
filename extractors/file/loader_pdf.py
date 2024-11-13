# loader_pdf.py

from .loader_file import FileLoader
import PyPDF2
from pdf2image import convert_from_path


class PdfLoader(FileLoader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def load(self, mode='auto'):
        """
        Метод для загрузки и чтения PDF файла в разных режимах.
        
        Parameters:
        - mode (str): режим загрузки ('auto', 'text', 'image').
            'auto' - пытается определить, есть ли текст, и возвращает текст, если он доступен, иначе сохраняет страницы как изображения.
            'text' - возвращает текст страниц.
            'image' - сохраняет страницы как изображения и возвращает их.
        """
        try:
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                if mode == 'text':
                    return self._extract_text(reader)
                if mode == 'image':
                    return self._extract_images(self.file_path)
                elif mode == 'auto':
                    # Проверяем, есть ли текст на первой странице
                    first_page_text = reader.pages[0].extract_text()
                    if first_page_text and first_page_text.strip():
                        return self._extract_text(reader)
                    else:
                        return self._extract_images(reader)
                else:
                    raise ValueError(f"Некорректный режим загрузки: {mode}")
        except FileNotFoundError:
            raise FileNotFoundError(f'Файл не найден: {self.file_path}')
        except PermissionError:
            raise PermissionError(f'Нет прав на чтение файла: {self.file_path}')
        except Exception as e:
            raise RuntimeError(f"Ошибка при загрузке PDF файла: {e}")

    def _extract_text(self, reader):
        """Извлекает текст из страниц PDF."""
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
        return text

    def _extract_images(self, file_path):
        """Извлекает изображения из PDF с использованием pdf2image."""
        try:
            images = convert_from_path(file_path)
            return images
        except Exception as e:
            raise RuntimeError(f"Ошибка при извлечении изображений из PDF: {e}")

