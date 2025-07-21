def CheckSpeed(speed):
    if speed < 70:
        raise Exception("速度太慢")
    elif speed > 100:
        raise Exception("速度太快")


for speed in (60, 90, 120):
    try:
        CheckSpeed(speed)
    except Exception as e:
        print(f"現在速度: {speed} ,{e}")
    else:
        print(f"目前速度: {speed}")
