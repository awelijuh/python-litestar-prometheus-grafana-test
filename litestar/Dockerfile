FROM python:3.12-slim

WORKDIR app

RUN pip install uv
RUN uv venv
COPY ./requirements.txt .
RUN uv pip install -r requirements.txt

COPY ./litestar .

CMD ./.venv/bin/uvicorn main:app --host 0.0.0.0 --port 8012