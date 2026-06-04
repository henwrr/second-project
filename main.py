import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные из .env
    load_dotenv()
    
    # Читаем переменную AUTHOR
    author = os.getenv("AUTHOR")
    
    # Печатаем имя автора
    print(f"Автор проекта: {author}")

# Вызываем функцию
if __name__ == "__main__":
    print_author()
