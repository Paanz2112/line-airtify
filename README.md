# Line Airtify
Line Airtify is Line Notify service and Apache Airflow dags notification  
this project use Line Notify to send notification about airflow dags to specific chat on Line platform  

How to use this script  
1. register line account and login to [Line Notify](https://notify-bot.line.me/)
2. generate API token and link Notify service to line chat room or specific chat
3. create .env file and add NOTIFY_TOKEN, NOTYFY_URL
4. use pip install -r req.txt to install lib  
> (I'm using Python 3.7 if you using other version please see [pypi](https://pypi.org/) for more compatible version of library)
5. create airflow dag file __see example in example_dag.py__
> you can custom your message to whatever you want. See [notify doc](https://notify-bot.line.me/doc/en/) for more infomation about message customization
