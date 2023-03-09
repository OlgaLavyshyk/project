def check_relation(net, first, second):
    local_net = list(net)
    new_first_name = ""
    for item in net:
        if first in item:
            print("first = ", first)
            if second in item:
                return True
            else:
                print("else")
                for name in item:
                    if name != first:
                        new_first_name = name
                local_net.remove(item)
                print("new net list = ", local_net)
                r = check_relation(local_net, new_first_name, second)
                if r:
                    return True

    # if not net:
    return False
net = (
    ("Ваня", "Лёша"), ("Лёша", "Катя"),
    ("Ваня", "Катя"), ("Вова", "Катя"),
    ("Лёша", "Лена"), ("Оля", "Петя"),
    ("Стёпа", "Оля"), ("Оля", "Настя"),
    ("Настя", "Дима"), ("Дима", "Маша"))
first = "Вова"
second = "Лена"

res = check_relation(net, first, second)
print(res)
#     #
#     # assert check_relation(net, "Петя", "Стёпа") is True
#     # assert check_relation(net, "Маша", "Петя") is True
#     # assert check_relation(net, "Ваня", "Дима") is False
#     # assert check_relation(net, "Лёша", "Настя") is False
#     # assert check_relation(net, "Стёпа", "Маша") is True
#     # assert check_relation(net, "Лена", "Маша") is False
#     # assert check_relation(net, "Вова", "Лена") is True

