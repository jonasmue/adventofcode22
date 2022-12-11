from collections import deque


def game(rounds, divide_worry_level):
    monkeys = setup()
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.take_turn(divide_worry_level)
    monkey_inspections = sorted([monkey.inspections for monkey in monkeys])
    return monkey_inspections[-2] * monkey_inspections[-1]


def setup():
    monkey_0 = Monkey([97, 81, 57, 57, 91, 61], lambda x: x * 7)
    monkey_1 = Monkey([88, 62, 68, 90], lambda x: x * 17)
    monkey_2 = Monkey([74, 87], lambda x: x + 2)
    monkey_3 = Monkey([53, 81, 60, 87, 90, 99, 75], lambda x: x + 1)
    monkey_4 = Monkey([57], lambda x: x + 6)
    monkey_5 = Monkey([54, 84, 91, 55, 59, 72, 75, 70], lambda x: x * x)
    monkey_6 = Monkey([95, 79, 79, 68, 78], lambda x: x + 3)
    monkey_7 = Monkey([61, 97, 67], lambda x: x + 4)

    monkey_0.set_monkey_test(MonkeyTest(11, monkey_5, monkey_6))
    monkey_1.set_monkey_test(MonkeyTest(19, monkey_4, monkey_2))
    monkey_2.set_monkey_test(MonkeyTest(5, monkey_7, monkey_4))
    monkey_3.set_monkey_test(MonkeyTest(2, monkey_2, monkey_1))
    monkey_4.set_monkey_test(MonkeyTest(13, monkey_7, monkey_0))
    monkey_5.set_monkey_test(MonkeyTest(7, monkey_6, monkey_3))
    monkey_6.set_monkey_test(MonkeyTest(3, monkey_1, monkey_3))
    monkey_7.set_monkey_test(MonkeyTest(17, monkey_0, monkey_5))

    return [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]


class MonkeyTest:
    def __init__(self, divisor, target_true, target_false):
        self.divisor = divisor
        self.target_true = target_true
        self.target_false = target_false


class Monkey:
    def __init__(self, items, operation):
        self.items = deque(items)
        self.operation = operation
        self.inspections = 0
        self.test = None

    def take_turn(self, divide_worry_level=True):
        while len(self.items):
            self.inspect(self.items.popleft(), divide_worry_level)

    def inspect(self, item, divide_worry_level):
        self.inspections += 1
        worry_level = self.operation(item)
        if divide_worry_level:
            worry_level //= 3
        worry_level %= 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
        if worry_level % self.test.divisor == 0:
            self.test.target_true.receive_item(worry_level)
        else:
            self.test.target_false.receive_item(worry_level)

    def receive_item(self, item):
        self.items.append(item)

    def set_monkey_test(self, monkey_test):
        self.test = monkey_test
