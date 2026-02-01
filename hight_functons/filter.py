num = [10, 15, 20, 30, 35]
events = []

# for n in num:
#     if n % 2 == 0:
#         events.append(n)
# print(events)


def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False


# events = list(filter(is_even, num))
# print(events)

events = list(filter(lambda x: x % 2 == 0, num))
print(events)

event_comp = [x for x in num if x % 2 == 0]
print(event_comp)
