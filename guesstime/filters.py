import re


def solar_chinese_to_num(string) -> str:
    """中文中的阳历月份进行转为阿拉伯数字

    切记：下面是阳历的月份，不是农历的月份

    :param string: 将阳历的月份转为阿拉伯数字
    :return: 转换完毕的阿拉伯数字
    """
    solar = {
        '一月': ' 1月',
        '二月': ' 2月',
        '两月': ' 2月',
        '三月': ' 3月',
        '四月': ' 4月',
        '五月': ' 5月',
        '六月': ' 6月',
        '七月': ' 7月',
        '八月': ' 8月',
        '九月': ' 9月',
        '一十月': ' 10月',
        '一十一月': ' 11月',
        '一十二月': ' 12月',
        '十月': ' 10月',
        '十一月': ' 11月',
        '十二月': ' 12月',
        'yue': '月',
        'Yue': '月',
        'YUE': '月',
        # 'RI': '日',
        # 'Ri': '日',
        # 'ri': '日',
        'hao': '日',
        'Hao': '日',
        'HAO': '日',
        'nian': '年',
        'Nian': '年',
        'NIAN': '年',
        "零":'0',
        "壹":'1',
        "贰":'2',
        "叄":'3',
        "肆":'4',
        "伍":'5',
        "陸":'6',
        "柒":'7',
        "捌":'8',
        "玖":'9',
        "拾":'10',
    }
    solar_re = '|'.join(solar.keys())
    result = re.sub(pattern=solar_re, repl=lambda x: solar[x.group()], string=string)
    return result
