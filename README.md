# DE Zero to Hero

A production-grade data engineering project built from scratch.
Covers ingestion, transformation, orchestration, cloud deployment,
and streaming — built session by session.

## Project structure
```
de-zero-to-hero/
├── ingestion/     # Python scripts that fetch and land raw data
├── dags/          # Airflow DAG definitions
├── models/        # dbt transformation models
│   ├── staging/   # clean and typed raw data
│   └── marts/     # business-ready aggregations
├── tests/         # pipeline unit tests
└── docs/          # architecture diagrams and decisions
```

## Setup

1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in your credentials

## Built with

Python 3.13 · dbt · Apache Airflow · AWS · Apache Kafka