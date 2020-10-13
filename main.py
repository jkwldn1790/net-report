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
    return s.results.dict()

def speed_test_upload():
    s = speedtest.Speedtest()
    s.upload()
    return s.results.dict()

download = speed_test_download()
upload = speed_test_upload()

write_results.insert_nettest(time(),download['download'],upload['upload'])