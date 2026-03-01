FROM apache/airflow:slim-3.1.6-python3.12


ENV AIRFLOW_VERSION=3.1.6
ENV PYTHON_VERSION=3.12

# Copy requirements and install
ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# When adding packages via apt you should switch to the root
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# switch back to the airflow user after installation
USER airflow