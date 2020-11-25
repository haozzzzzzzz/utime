# -*- coding: utf-8 -*-
import datetime
import time

import pytz
from dateutil.relativedelta import relativedelta
from dateutil.tz import tzoffset
from dateutil import parser

__author__ = "Hao Luo"

TzChina = tzoffset("CST", +28800) # 北京时间
Timezone = TzChina

TzIndia = tzoffset("IST", +19800) # india timezone
TzIndonesia = tzoffset("ICT", +25200) # indonesia timezone. UTC+7
TzVietnam = tzoffset("ICT", +25200) # vienam timezone. using indonesia timezone UTC+7


def use_tz_utc():
    global Timezone
    Timezone = pytz.UTC


def use_tz_india():
    global Timezone
    Timezone = TzIndia


def use_tz_indonesia():
    global Timezone
    Timezone = TzIndonesia


def use_tz_vietnam():
    global Timezone
    Timezone = TzVietnam


def use_tz_china():
    global Timezone
    Timezone = TzChina


def use_tz(tz):
    global Timezone
    Timezone = tz


def use_tzoffset(tz_name, utc_offset):
    global Timezone
    Timezone = tzoffset(tz_name, utc_offset)


def now():
    return datetime.datetime.now(Timezone)


def datetime_to_unix(dt):
    return int(dt.timestamp())


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
    dt = dt.astimezone(tz=Timezone) # 时区转换
    return datetime.datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        tzinfo=dt.tzinfo,
    )


def day_start_to_unix(dt):
    """
    Get day start unix timestamp from datetime
    """
    return datetime_to_unix(day_start(dt))


def unix_to_day_start(unix_time):
    """
    Get day start datetime from unix timestamp
    """
    return day_start(unix_to_datetime(unix_time))


def unix_to_day_start_str(unix_time):
    """
    Get str day start time from unix timestamp
    :param unix_time:
    :return:
    """
    return datetime_to_day_str(unix_to_day_start(unix_time))


def today():
    return day_start(now())


def today_unix():
    return datetime_to_unix(today())


def tomorrow():
    return day_start_offset(today(), 1)


def tomorrow_unix():
    return datetime_to_unix(tomorrow())


def yesterday():
    return day_start_offset(today(), -1)


def yesterday_unix():
    return datetime_to_unix(yesterday())


def day_start_offset(dt, offset=0):
    ds = day_start(dt)
    ds += datetime.timedelta(days=offset)
    return ds


def day_start_offset_unix(dt_unix, offset=0):
    """
    Get offset day start unix timestamp
    """
    dt = unix_to_day_start(dt_unix)
    ds_offset = day_start_offset(dt, offset)
    ds_unix = datetime_to_unix(ds_offset)
    return ds_unix


def datetime_to_day_str(dt):
    return dt.strftime("%Y-%m-%d")


def datetime_to_str(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def unix_to_str(unix_time):
    """
    unix timestamp in seconds to string datetime format
    """
    return datetime_to_str(unix_to_datetime(unix_time))


def str_to_datetime(s):
    """
    %Y-%m-%d %H:%M:%S
    :param s:
    :return:
    """
    dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    return datetime.datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=dt.hour,
        minute=dt.minute,
        second=dt.second,
        tzinfo=Timezone,
    )


def str_to_unix(s):
    return datetime_to_unix(str_to_datetime(s))


def day_str_to_daytime(s):
    dt = datetime.datetime.strptime(s, "%Y-%m-%d")
    new_dt = datetime.datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        tzinfo=Timezone,
    )
    return new_dt


def day_str_to_unix(s):
    return datetime_to_unix(day_str_to_daytime(s))


def common_parse(str_time):
    '''
    通用解析时间字符串
    :param str_time:
    :return:
    '''
    return parser.parse(str_time).astimezone(Timezone)


def format_str_to_datetime(str_time, fmt):
    dt = datetime.datetime.strptime(str_time, fmt)
    return datetime.datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=dt.hour,
        minute=dt.minute,
        second=dt.second,
        microsecond=dt.microsecond,
        tzinfo=Timezone,
    )


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
    return month_day + relativedelta(months=offset)


def month_start_offset_unix(dt, offset=0):
    return datetime_to_unix(month_start_offset(dt, offset))


def month_cur_start():
    """
    current month start datetime
    :return:
    """
    return month_start(today())


def season_start(dt):
    """
    季开始日期
    :param dt: Datetime
    :return:
    """
    session = int((dt.month - 1) / 3)
    month = session * 3 + 1
    return datetime.datetime(
        year=dt.year,
        month=month,
        day=1,
        tzinfo=dt.tzinfo,
    )


def season_start_unix(dt):
    return datetime_to_unix(season_start(dt))


def season_num(dt):
    return int((dt.month - 1) / 3) + 1


def season_cur():
    return season_start(today())


def season_cur_unix():
    return datetime_to_unix(season_cur())


def season_offset(dt, offset=0):
    cur_season = season_start(dt)
    offsets_month = 3 * offset
    offset_season = cur_season + relativedelta(months=offsets_month)
    return offset_season


if __name__ == "__main__":
    # n = now()
    # print(n)
    # print(day_start(n))
    # print(day_start_unix(n))
    # print(today())
    # print(today_unix())
    # print(day_start_offset(n, 1))
    # print(datetime_to_day_str(n))
    # print(datetime_to_str(n))
    # print(str_to_datetime("2020-03-29 14:14:54"))
    # dt = str_to_datetime("2020-02-29 14:14:54")
    # print(dt)
    #
    # print(week_start(dt))
    # week_offset = week_start_offset(dt, -1)
    # print(week_offset)
    #
    # ms = month_start(dt)
    # print(ms)
    #
    # print("20200331150000000"[:-3])
    # print(format_str_to_datetime("20200331150000000"[:-3], "%Y%m%d%H%M%S"))
    # print(season_start(str_to_datetime("2020-11-29 18:30:00")))

    # use_tz_india()
    # dt = day_str_to_daytime("2020-01-02")
    # print(dt)
    # print(str_to_datetime("2020-01-02 18:30:00"))
    # print(format_str_to_datetime("2020-01-02 18:30:00", "%Y-%m-%d %H:%M:%S"))
    # print(season_offset(dt, -1))

    # print(day_str_to_daytime("2020-04-17"))
    
    # print(unix_to_str(today_unix()))

    use_tz_india()
    print(common_parse("2020-11-24T10:00:10Z"))
