def can_drink_alcohol(age):
    """
    引数 age を受け取り、20以上なら '飲酒可能です' という文字列を返す

    age が float の場合は TypeError を発生させる
    age が整数でない場合は TypeError を発生させる
    age が負の数の場合は ValueError を発生させる
    age が20未満の場合は ValueError を発生させる

    :param age: int
    :return: str
    """

    if isinstance(age, float):
        raise TypeError("整数を入力してください")
    elif not isinstance(age, int):
        raise TypeError("整数以外は判定できません")
    elif age < 0:
        raise ValueError("正の数を入力してください")
    elif age < 20:
        raise ValueError("飲酒不可です")

    return "飲酒可能です"


def my_partial_func(x):
    y = 0
    if x:
        y = 10
    return y
