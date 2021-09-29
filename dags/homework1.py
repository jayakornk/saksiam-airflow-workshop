from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator

default_args = {
    "owner": "Jayakorn Karikan",
    "start_date": timezone.datetime(2021, 9, 29)
}

with DAG(
    "homework1",
    schedule_interval="*/5 * * * *",
    default_args=default_args,
    catchup=False,
    tags=["saksiam"],
) as dag:

    task_1 = DummyOperator(task_id="1")
    task_2 = DummyOperator(task_id="2")
    task_3 = DummyOperator(task_id="3")
    task_4 = DummyOperator(task_id="4")
    task_5 = DummyOperator(task_id="5")
    task_6 = DummyOperator(task_id="6")
    task_7 = DummyOperator(task_id="7")
    task_8 = DummyOperator(task_id="8")
    task_9 = DummyOperator(task_id="9")

    task_1 >> [task_2, task_5]
    task_2 >> [task_3, task_6]
    task_3 >> task_4 >> task_9
    task_5 >> [task_6, task_7] >> task_8 >> task_9
