import datetime
import time
import random



def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)  # Formato Day-Month-Year


start_date = random_date("1/1/2022", "31/12/2022", random.random())
hola = datetime.datetime.strptime(start_date, "%d/%m/%y")
end_date = hola+ datetime.timedelta(days=10)

print(start_date)
print(end_date)