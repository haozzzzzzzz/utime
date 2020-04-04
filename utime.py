# -*- coding: utf-8 -*-
import datetime
import time

import pytz
from dateutil.relativedelta import relativedelta
from dateutil.tz import tzoffset

__author__ = "Hao Luo"

TzShanghai = pytz.timezone('Asia/Shanghai')
Timezone = TzShanghai

TzIndia = tzoffset("IST", +19800) # india timezone
TzIndonesia = tzoffset("WIB", +25200) # indonesia timezone


def use_tz_india():
    global Timezone
    Timezone = TzIndia


def use_tz_indonesia():
    global Timezone
    Timezone = TzIndonesia


def use_tz_shanghai():
    global Timezone
    Timezone = TzShanghai


def use_tz(tz):
    global Timezone
    Timezone = tz


def now():
    return datetime.datetime.now(Timezone)


def datetime_to_unix(dt):
    return int(time.mktime(dt.timetuple()))


def unix_to_datetime(unix_time):
    return datetime.datetime.fromtimestamp(unix_time, tz=Timezone)


def now_unix():
    """
    当前时间戳
    """

    return int(time.time())


def day_start(dt):
    """
    一天开始时间
    """
    dt = dt.astimezone(tz=Timezone)
    return datetime.datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        tzinfo=dt.tzinfo,
    )


def day_start_unix(dt):
    return datetime_to_unix(day_start(dt))


def today():
    return day_start(now())


def today_unix():
    return datetime_to_unix(today())


def day_start_offset(dt, offset=0):
    ds = day_start(dt)
    ds += datetime.timedelta(days=offset)
    return ds


def datetime_to_day_str(dt):
    return dt.strftime("%Y-%m-%d")


def datetime_to_str(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def str_to_datetime(s):
    """
    %Y-%m-%d %H:%M:%S
    :param s:
    :return:
    """
    t = time.mktime(time.strptime(s, "%Y-%m-%d %H:%M:%S"))
    return datetime.datetime.fromtimestamp(t, tz=Timezone)


def day_str_to_daytime(s):
    t = time.mktime(time.strptime(s, "%Y-%m-%d"))
    return datetime.datetime.fromtimestamp(t, tz=Timezone)


def format_str_to_datetime(str_time, fmt):
    t = time.mktime(time.strptime(str_time, fmt))
    return datetime.datetime.fromtimestamp(t, tz=Timezone)


def week_start(dt):
    week_day_unix = week_start_unix(dt)
    week_day = unix_to_datetime(week_day_unix)
    return week_day


def week_start_unix(dt):
    day = day_start(dt)
    day_unix = datetime_to_unix(day)
    n_week_day = day.weekday()

    monday_offset = n_week_day * 86400
    week_day_unix = day_unix - monday_offset
    return week_day_unix


def week_start_offset(dt, offset=0):
    week_day = week_start(dt)
    week_day += datetime.timedelta(weeks=offset)
    return week_day


def week_start_offset_unix(dt, offset=0):
    week_day = week_start_offset(dt, offset)
    return datetime_to_unix(week_day)


def week_cur_start():
    """
    current weeek start datetime
    :return:
    """
    return week_start(today())


def month_start(dt):
    return datetime.datetime(
        year=dt.year,
        month=dt.month,
        day=1,
        tzinfo=dt.tzinfo,
    )


def month_start_unix(dt):
    return datetime_to_unix(month_start(dt))


def month_start_offset(dt, offset=0):
    month_day = month_start(dt)
    return month_day + relativedelta(months=0)


def month_start_offset_unix(dt, offset=0):
    return datetime_to_unix(month_start_offset(dt, offset))


def month_cur_start():
    """
    current month start datetime
    :return:
    """
    return month_start(today())


if __name__ == "__main__":
    n = now()
    print(n)
    print(day_start(n))
    print(day_start_unix(n))
    print(today())
    print(today_unix())
    print(day_start_offset(n, 1))
    print(datetime_to_day_str(n))
    print(datetime_to_str(n))
    print(str_to_datetime("2020-03-29 14:14:54"))
    dt = str_to_datetime("2020-02-29 14:14:54")
    print(dt)

    print(week_start(dt))
    week_offset = week_start_offset(dt, -1)
    print(week_offset)

    ms = month_start(dt)
    print(ms)

    # print("20200331150000000"[:-3])
    # print(format_str_to_datetime("20200331150000000"[:-3], "%Y%m%d%H%M%S"))