# net-report
Application to report network performance over a period of time

## Setup
Installing psycopg2 `pip3 install psycopg2-binary`

## Running
`docker run -it --network host test:v1`

## Database Structure

Table | NetResults
Time | Download | Upload

1. Create_table.py
2. insert_vendor.py


## Roadmap
- Move the workload to kubernetes to be scheduled as a cronjob
- Incorporate flask to present a single webpage with the intention of using prometheus/grafana setup to graph results.