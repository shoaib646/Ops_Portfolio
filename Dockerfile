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


# Stage 1: Build (if needed for Python wheels or compiled dependencies)
FROM python:3.10-slim-buster as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.10-slim-buster
WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Ensure scripts are executable
RUN chmod +x start.sh

# Environment variables
ENV AIRFLOW_HOME="/app/airflow" \
    AIRFLOW__CORE__DAGBAG_IMPORT_TIMEOUT=1000 \
    AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True \
    PATH="/root/.local/bin:${PATH}"

# Initialize Airflow and create user (combine RUN commands to reduce layers)
RUN airflow db init && \
    airflow users create \
    -e cruzai.contact@gmail.com \
    -f shoaib \
    -l ahmed \
    -p admin \
    -r Admin \
    -u admin

ENTRYPOINT ["/bin/sh", "start.sh"]