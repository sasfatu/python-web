FROM python:3.10.14-alpine3.19

# Update Alpine packages to address vulnerabilities
RUN apk update && apk upgrade

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /src

CMD ["python", "/src/app.py"]