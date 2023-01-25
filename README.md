## Тестовое задание для вакансии ReLabs


### Для запуска проекта:

Создайте и активируйте виртуальное окружение:

Windows:
```bash
python -m venv env
source env/Scripts/activate
```
Linux:
```bash
python3 -m venv env
source env/bin/activate
```

Установите зависимости:
```bash
pip install -r requirements.txt
```

Запустите приложение с помощью команды:
```bash
uvicorn main:app --reload
```

Приложение будет доступно по адресу: http://127.0.0.1:8000


### Используемые библиотеки
- FastAPI
- Jinja2 - шаблонизатор для отправки HTML-страницы
- uvicorn - ASGI сервер
- starlette websockets
