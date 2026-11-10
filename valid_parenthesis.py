# Check if a string contains valid parenthesis.
def is_valid_parenthesis(test_case):
    parenthesis_pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []  # implement last in first out

    if len(test_case) % 2 != 0:
        return False
    for char in test_case:
        if char in parenthesis_pairs:
            stack.append(char)
        elif char not in parenthesis_pairs:
            if len(stack) == 0:
                stack.append(char)
                return False
            last_open = stack[-1]
            if char != parenthesis_pairs[last_open]:
                return False
            else:
                stack.pop()
    return len(stack) == 0


def main():
    test_cases = [
        ["()[]{}", True],
        ["(])", False],
        ["((", False],
        ["[()]", True],
        ["(())", True],
        ["())", False],
    ]
    failed_test_cases = []
    count = 0
    for case in test_cases:
        test_case = case[0]
        result = case[-1]
        answer = is_valid_parenthesis(test_case)
        if answer == result:
            count += 1
        else:
            failed_test_cases.append(case)

    print(f"Passed {count}/{len(test_cases)} test cases")
    if len(failed_test_cases) != 0:
        print("The following test cases failed: ")
        for case in failed_test_cases:
            print(case)


main()
