import datetime
import datefinder
import winsound


def alarm(command):
    dTimeA = datefinder.find_dates(command)
    for mat in dTimeA:
        print(mat)
    stringA = str(mat)
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA)
    minA = timeA[3:-3]
    minA = int(minA)


    while True:
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                print('alarm started')
                winsound.PlaySound('./alarm.wav',winsound.SND_LOOP)
            elif minA<datetime.datetime.now().minute:
                break
