# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "gunicorn", "--workers", "2", "--bind", "0.0.0.0:5000", "sim:app" ]
#CMD [ "python", "sim.py" ]