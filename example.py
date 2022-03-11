import time
import datetime
from guesstime import GuessTime


if __name__ == '__main__':
    print(GuessTime(time.time()).to_datetime())

    print(GuessTime(datetime.datetime.now()).to_timestamp())

    print(GuessTime(datetime.date.today()).to_timestamp())

    print(GuessTime("March 10, 2021 5:08pm EST").to_datetime())

    print(GuessTime("2021 10.2 5:08pm CNT").to_datetime())

    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").to_datetime())

    print(GuessTime("2022-03-11 18:14:27.913229-08:00").to_timestamp())

    print(GuessTime(datetime.datetime.now()).to_timestamp())

    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('这个月的第三个星期天').to_datetime())

    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('今年的大寒').to_datetime())

    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('今天中午十二点').to_datetime())

    print(GuessTime("2022-03-11 18:14:27.913229 -08:00").parse('今天晚上8点').to_datetime())

    """
    2022-03-11 10:54:04.418433+00:00
    1647024844.423416
    1646956800.0
    2021-03-10 17:08:00+00:00
    2021-10-11 17:08:00+00:00
    2022-03-12 02:14:27.913229+00:00
    1647051267.913229
    1647024844.453098
    2022-03-20 02:14:27+00:00
    2023-01-20 02:14:27+00:00
    2022-03-12 12:14:27+00:00
    2022-03-12 20:14:27+00:00
    """

