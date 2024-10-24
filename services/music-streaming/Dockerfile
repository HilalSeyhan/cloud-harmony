FROM python:3.9

WORKDIR /app

COPY ./services/music-streaming/requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt

COPY ./services/music-streaming/ . 

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]
