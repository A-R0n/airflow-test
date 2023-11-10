# airflow-test

This is an Apache Airflow application running as a docker container that executes a single task, within a DAG. The task outputs "Hello" to the console every minute. The results are available through the UI on localhost:8080 after installing docker-compose locally, initializing a SQLite database with Airflow, creating an admin user, and then running a webserver and scheduler