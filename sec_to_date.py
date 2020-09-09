import datetime


def format_duration(seconds):
    time_dict = {}
    time = datetime.timedelta(seconds=seconds)
    time_dict['year'] = time.days//365
    time_dict['day'] = time.days - time_dict['year']*365
    time_dict['hour'] = time.seconds//3600
    time_dict['minute'] = (time.seconds - time_dict['hour']*3600)//60
    time_dict['second'] = time.seconds - time_dict['hour']*3600 - time_dict['minute']*60
    result = []
    for key, item in time_dict.items():
        if item != 0:
            result.append(f"{item} {key}" + ("s" if item > 1 else ""))
    res = ', '.join(result[:-1])
    if res == '':
        res = result[-1]
    else:
        res += f' and {result[-1]}'
    return res


print(format_duration(60*60 + 60))