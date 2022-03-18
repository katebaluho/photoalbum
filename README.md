# photoalbum
Photo album Django+DRF
Для запуска проекта:

git clone https://github.com/katebaluho/photoalbum.git\n
проверить нахождениe в виртуальном окружении\n
установить зависимости pip install -r requirements.txt\n
python manage.py makemigrations\n
python manage.py migrate\n

Создать файл в корне проекта '.env'
Поместить в него информацию:
DEBUG=
SECRET_KEY=
EMAIL_HOST_PASSWORD=0
CELERY_BROKER=redis://localhost:6379 
CELERY_BACKEND=redis://localhost:6379
(Брокер и бэкенд надо скрывать но для pet-проекта пусть остается в readmi)

Для работы с api подключен Swagger: 
http://127.0.0.1:8000/api/swagger/

Для проверки отправки email c использованием celery одновременно запустить
celery -A app beat -l info
celery -A app worker -l info

