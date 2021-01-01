import speedtest
import json
import psycopg2
import write_results
from config import config
from datetime import datetime

def time():
    now = datetime.now()
    return now.strftime("%D %H:%M:%S")

def speed_test_download():
    s = speedtest.Speedtest()
    s.download()
    results = s.results.dict()
    return round(results['download'] / 1000000, 2)

def speed_test_upload():
    s = speedtest.Speedtest()
    s.upload()
    results = s.results.dict()
    return round(results['upload'] / 1000000, 2)

def avg(results_given): # Function to take in an array and average the values.
    return round(sum(results_given) / len(results_given), 2)

def retrieve_by_column(column):
    results = []
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("SELECT * FROM netresults")
    rows = cur.fetchall()
    for row in rows:
        results.append(float(row[int(column)]))
    return results
    conn.close()

download = speed_test_download()
upload = speed_test_upload()

write_results.insert_nettest(time(),download,upload)

average_download = avg(retrieve_by_column(2))
average_upload = avg(retrieve_by_column(3))

stats_template = """
Upload Speed: {} Mb/s
Download Speed: {} Mb/s

Average Download Speed: {} Mb/s
Average Upload Speed: {} Mb/s
""".format(
    upload,
    download,
    average_download,
    average_upload
)

print(stats_template)