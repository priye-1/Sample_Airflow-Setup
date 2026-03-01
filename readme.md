# Airflow Orchestrator Architecture

This example demonstrates a local  Airflow setup.


## High-Level Overview

- **Airflow**: Schedules and orchestrates workflows
- **DockerOperator**: Launches an external container to run business logic
- **Component Container**: Executes the actual processing logic
- **Docker-out-of-Docker (DooD)**: Airflow communicates with the host Docker Engine to start sibling containers



## Project Structure

> ```text
> config/                 # Airflow configuration (webserver, scheduler, etc.)
> dags/                   # Airflow DAG definitions
> Dockerfile              # Image definition for Airflow services
> docker-compose.yml      # Builds and runs Airflow + component images
> ```


## Getting Started

### Prerequisites

* Docker
* Docker Compose (v2 recommended)


### Clone the Repository

> ```bash
> git clone <repo-url>
> cd airflow
> ```


### Build and Start Infrastructure

Navigate to the Airflow infrastructure directory:

> ```bash
> cd <home directory>
> docker compose build
> docker compose up
> ```

This will:

* Build the **Airflow image**
* Start Airflow services (webserver, dag processor, metadata DB)


To stop the airflow service:

> ```bash
> docker compose down
> ```


### Access the Airflow UI

* URL: [http://localhost:8080](http://localhost:7070)
* Username: `admin`
* Password: This should be retrieved from terminal



### Trigger the Workflow

1. Open the Airflow UI
2. Locate the DAG that runs the example component
4. Trigger it manually from the UI

<img src="readme_images/dag.png" alt="Created DAGS" />


> ### Added DAGs
> 
> Two DAGs have been added:
> 
> 1. **sample ETL DAG**
>   This DAG demonstrates a simple ETL workflow using the Airflow TaskFlow API.

   - Extract 
   Fetches the current Bitcoin price from an external API.

   - Transform 
   Processes the API response into a pandas DataFrame containing:
   - `usd` – current Bitcoin price in USD  
   - `change` – 24-hour price change percentage  

   - Load
   Stores the transformed data into a CSV file (`bitcoin_price.csv`).

<img src="readme_images/dagrun.png" alt="DAGS runs" />

### Managing Environment Variables via Airflow UI

Runtime configuration for tasks and components can also be managed using **Airflow Variables**:

1. Open the Airflow UI
2. Navigate to **Admin → Variables**
3. Create a variable:
   - **Key:** `<my key>`
   - **Value:** `<>my value`



### Airflow Installation Mode Used in This Project

This project uses a **slim, standalone Airflow deployment** where **all core services are embedded into a single container image**:

* Webserver
* Scheduler
* Triggerer
* Metadata database

This setup is intentionally lightweight and suitable for:

* Local development
* Proofs of concept
* Architecture demonstrations



### Full Production Airflow Installation (Recommended for Production)

For a **full production-grade Airflow deployment** with:

* Separate services
* External PostgreSQL
* Redis
* Celery or Kubernetes executors

Use the **official Apache Airflow Docker Compose stack**.

**Official `docker-compose.yaml` (Full Install)**
[https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml](https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml)

**Documentation**
[https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

