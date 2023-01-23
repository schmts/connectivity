FROM python:3.7 as compiler
ENV PYTHONUNBUFFERED 1
WORKDIR /app/

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

FROM python:3.7 as runner
WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
COPY . /app/
CMD ["python", "app.py"]
