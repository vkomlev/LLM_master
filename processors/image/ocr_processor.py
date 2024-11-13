# ocr_processor.py

import pytesseract
from PIL import Image

class BaseOCR:
    def __init__(self, content, language='eng+rus'):
        self.content = content
        self.language = language  # Язык по умолчанию - английский

    def recognize_text(self):
        """Метод для распознавания текста, должен быть реализован в подклассах."""
        raise NotImplementedError("Метод recognize_text должен быть реализован в подклассах.")

class ImageOCR(BaseOCR):
    def __init__(self, image, language='eng+rus'):
        super().__init__(image, language)

    def recognize_text(self):
        """Распознает текст из изображения."""
        try:
            return pytesseract.image_to_string(self.content, lang=self.language)
        except Exception as e:
            raise RuntimeError(f"Ошибка при распознавании текста из изображения: {e}")

class PdfOCR(BaseOCR):
    def __init__(self, pdf_pages, language='eng+rus'):
        super().__init__(pdf_pages, language)

    def recognize_text(self):
        """Распознает текст из страниц PDF."""
        recognized_text = ""
        try:
            for page_image in self.content:
                recognized_text += pytesseract.image_to_string(page_image, lang=self.language) + "\n"
            return recognized_text
        except Exception as e:
            raise RuntimeError(f"Ошибка при распознавании текста из PDF: {e}")
