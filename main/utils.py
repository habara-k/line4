def time(func):
    """ 関数の実行時間を表示するデコレータ """
    import functools
    import datetime
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.today()
        result = func(*args, **kwargs)
        end = datetime.datetime.today()
        print('計算時間:', end - start)
        return result
    return wrapper

def flatten(x):
    if isinstance(x, list):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

def max_arg(nested_list):
    """ 入力された2次元のリストの最大値を与えるIndexを返す """
    max_value = max(flatten(nested_list))
    arg_list = [(p, q)
                for p in AXIS
                for q in AXIS
                if nested_list[q][p] == max_value]
    return choice(arg_list)
