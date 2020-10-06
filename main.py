import speedtest
import json

# s = speedtest.Speedtest()
# s.download()
# results_dict = s.results.dict()
# print(results_dict['download'])

def speed_test_download():
    s = speedtest.Speedtest()
    s.download()
    return s.results.dict()

def speed_test_upload():
    s = speedtest.Speedtest()
    s.upload()
    return s.results.dict()

test_download = speed_test_download()
test_upload = speed_test_upload()
print("\nDownload Speed: {}\nUpload Speed: {}\n".format(test_download['download'], test_upload['upload']))