FROM python:3.9

WORKDIR /app

COPY ./api-gateway/requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt

COPY ./api-gateway/ .  

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]
