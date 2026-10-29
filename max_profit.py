import math


def max_profit(prices):
    buy_day = max_profit_recorded = 0
    sell_day = buy_day + 1

    if len(prices) <= 1:
        return 0

    while sell_day < len(prices):
        diff = prices[sell_day] - prices[buy_day]
        if diff < 0:
            buy_day = sell_day
        elif diff > max_profit_recorded:
            max_profit_recorded = diff
        sell_day += 1

    print(max_profit_recorded)
    return max_profit_recorded


def main():
    test_cases = [
        [5, [7, 1, 5, 3, 6, 4]],
        [0, [7, 6, 4, 3, 1]],
        [1, [1, 2]],
        [4, [3, 2, 6, 1, 1]],
        [4, [1, 5, 3]],
    ]
    length = count = 0
    for test_case_data in test_cases:
        result = test_case_data[0]
        test_case = test_case_data[-1]
        print("test_case", test_case, "result", result)
        length += 1
        answer = max_profit(test_case)
        if answer == result:
            count += 1

    print(f"passed {count}/{length} testcases")


main()
