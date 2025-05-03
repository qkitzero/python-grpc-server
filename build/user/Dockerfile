FROM python:3.13-alpine
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH=/src:/src/gen/python
CMD ["python", "app/main.py"]
