from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator


# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="my_first_dag", description="this is the first dag i write", start_date=datetime(2023, 11, 10), schedule="*/1 * * * *") as dag:

    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()