from datetime import timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import sys
sys.path.insert(1, '/home/maholan/line-airtify')
from notify import line_notify
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
def task_success_alert(context):
    dag_id = context['dag'].dag_id
    task_id = context['task_instance'].task_id
    dag_state = context['task_instance'].state
    exec_date = context['task_instance'].execution_date
    end_date = context['task_instance'].end_date
    job_id_ = context['task_instance'].job_id
    dag_duration = context['task_instance'].duration
    line_notify(dag_id=dag_id,task_id=task_id,dag_state=dag_state,exec_date=exec_date,end_date=end_date,job_id_=job_id_,dag_duration=dag_duration)

default_args = {
    'owner': 'paan',
    'depends_on_past': False,
    'email': ['phandit.j@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    'on_failure_callback': task_success_alert,
    'on_success_callback': task_success_alert,
    'on_retry_callback': task_success_alert,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

with DAG(
    'cache_clearing_airtify',
    default_args=default_args,
    description='Dags for execute bash command',
    schedule_interval='*/20 * * * *',
    start_date=days_ago(1),
    tags=['hourly', 'cache','bash'],
) as dag:
    t1 = BashOperator(
        task_id='clear_cache',
        bash_command="sudo free -h && echo 3 > /proc/sys/vm/drop_caches && free -h",
        dag=dag
    )