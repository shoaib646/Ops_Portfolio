#!/bin/bash
nohub airflow scheduler &
airflow webserver