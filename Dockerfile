# FROM python:3.10-slim-buster
# USER root
# RUN mkdir /app
# COPY . /app/
# WORKDIR /app/
# RUN pip3 install -r requirements.txt
# ENV AIRFLOW_HOME="/app/airflow"
# ENV AIRFLOW_CORE_DAGBAG_IMPORT_TIMEOUT=1000
# ENV AIRFLOW_CORE_ENABLE_XCOM_PICKLING=True
# RUN airflow db init
# RUN airflow users create -e cruzai.contact@gmail.com -f shoaib -l ahmed -p admin -r Admin -u admin
# RUN chmod 777 start.sh
# RUN apt update -y
# ENTRYPOINT [ "/bin/sh" ]
# CMD ["start.sh"]


# Stage 1: Build dependencies (with layer caching)
FROM python:3.10-slim-buster as builder

WORKDIR /app

# Copy only dependency files first for caching
COPY pyproject.toml setup.py ./
COPY requirements.txt .

# Install build system and dependencies
RUN pip install --upgrade pip && \
    pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime image
FROM python:3.10-slim-buster

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /root/.local /root/.local
ENV PATH="/root/.local/bin:${PATH}"

# Copy application code (including your package)
COPY . .

# Install local package in editable mode (requires setup.py/pyproject.toml)
RUN pip install --no-deps -e .

# Airflow setup
ENV AIRFLOW_HOME="/app/airflow" \
    AIRFLOW__CORE__LOAD_EXAMPLES="false"

RUN airflow db init && \
    airflow users create \
    --username admin \
    --firstname Shoaib \
    --lastname Ahmed \
    --role Admin \
    --email cruzai.contact@gmail.com \
    --password admin

ENTRYPOINT ["/bin/sh", "start.sh"]