import time
import datetime
from guesstime import GuessTime

if __name__ == '__main__':
    print(datetime.timedelta(seconds=time.time()).__str__())
    print(GuessTime("Wed Mar 16 01:33:53 +0000 2016").offset(seconds=-60).to_datetime())
    print((GuessTime(" 01:33:53").offset(seconds=-60, hours=6) - 6 - '2022-1-1'))
    print(GuessTime("Wed Mar 16 01:33:53 +0000 2016").to_datetime())
    print(GuessTime("Wed Mar 16 01:33:53 +0000 2016").to_datetime_with_change_timezone())
    print(GuessTime("Wed Mar 16 01:33:53 +0000 2016").to_date_str_with_change_timezone())
    print(GuessTime("Wed Mar 16 01:33:53 +0000 2016").to_date_str())
    print(GuessTime("2021一月一hao").to_datetime())
    print(GuessTime("2021一月2hao十八點").to_datetime())
    print(GuessTime("2021.10 12 5:08pm CNT").to_datetime())
    print(GuessTime("2021。10 12 5:08pm CNT").to_datetime())
    print(GuessTime("2021/March.2 5:08pm CNT").to_datetime())
    print(GuessTime("2021/10/12 5:08pm CNT").to_datetime())
    print(GuessTime("(10/12 5:08pm CNT").to_datetime())
    print(GuessTime("2021-10/12 5:08pm CNT").to_datetime())
    print(GuessTime("2021-03-10T 17:08:00 +00:00").to_datetime())
    print(GuessTime("March 10, 2021 5:08pm EST").to_arrow())
    print(GuessTime(time.time()).to_datetime())
    print(GuessTime(datetime.datetime.now()).to_timestamp())
    print(GuessTime(datetime.date.today()).to_timestamp())
    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").to_datetime())
    print(GuessTime("2022-03-11 18:14:27.913229-08:00").to_timestamp())
    print(GuessTime(datetime.datetime.now()).to_timestamp_int())
    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('这个月的第三个星期天').to_datetime())
    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('今年的大寒').to_datetime())
    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('今天中午十二点').to_datetime())
    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('今天晚上8点').to_datetime())
    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('今天晚上8点').to_arrow().weekday())
    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('今天晚上8点').to_datetime().hour)
    print(GuessTime("Wed 000 2016", raise_err=False).to_datetime(datetime.datetime.now()))
    print(GuessTime("Wed 000 2016", raise_err=False).to_guess_filter_string())

"""
19284 days, 14:53:31.507912
2016-03-16 01:32:53+00:00
291 days, 7:32:47
2016-03-16 01:33:53+00:00
2016-03-16 09:34:53+08:00
2016-03-16 09:34:53 CST
2016-03-16 09:33:53
2021-01-01 00:00:00+00:00
2021-01-02 18:00:00+00:00
2021-10-12 17:08:00+00:00
2021-10-12 17:08:00+00:00
2021-03-02 17:08:00+00:00
2021-10-12 17:08:00+00:00
2022-10-12 17:08:00+00:00
2021-10-12 17:08:00+00:00
2021-03-10 17:08:00+00:00
2021-03-10T17:08:00+00:00
2022-10-19 14:53:31.556651+00:00
1666220011.558058
1666137600.0
2022-03-12 02:14:27.913229+00:00
1647051267.913229
1666220011
2022-03-27 02:14:27+00:00
2023-01-20 02:14:27+00:00
2022-03-12 12:14:27+00:00
2022-03-12 20:14:27+00:00
5
20
2022-10-19 22:53:31.590662
Wed 000 2016
"""
