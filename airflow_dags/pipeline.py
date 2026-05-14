from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="team13_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    preprocess = BashOperator(
        task_id="preprocess",
        bash_command="python src/preprocess.py"
    )

    train = BashOperator(
        task_id="train_model",
        bash_command="python src/train.py"
    )

    lineage = BashOperator(
        task_id="lineage_tracking",
        bash_command="python src/lineage.py"
    )

    preprocess >> train >> lineage
