FROM python:3.8-slim as builder
COPY . /src
ENV PATH=/root/.local/bin:$PATH
RUN pip install --user fastapi uvicorn boto3 flask

FROM python:3.8-slim as app
ENV PATH=/root/.local/bin:$PATH
COPY --from=builder /root/.local /root/.local
COPY --from=builder /src .

EXPOSE 5000

CMD ["python3", "app.py"]
