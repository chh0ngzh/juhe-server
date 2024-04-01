from time import time


if "START_TIME" not in vars():
    print("Init stats.")

    START_TIME = time()
    TOTAL_REQ_COUNT = 0
    TOTAL_ERR = 0
