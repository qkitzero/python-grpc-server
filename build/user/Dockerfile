FROM python:3.9
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH=/src:/src/pb
CMD ["python", "app/main.py"]
