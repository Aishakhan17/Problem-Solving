class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"Node({self.val})"


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def reverse_list(self):
        prev = None
        curr = self.head
        following = self.head
        while curr != None:
            following = following.next
            curr.next = prev
            prev = curr
            curr = following
        self.head = prev

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next


def create_nodes(num_list):
    # Create all the nodes of the list
    node_list = []
    for num in num_list:
        node = Node(num)
        node_list.append(node)
    return node_list


def create_linked_list(node_list):
    llist = LinkedList()
    llist.head = node_list[0]

    curr = llist.head
    temp = 1
    while temp < len(node_list):
        curr.next = node_list[temp]
        temp += 1
        curr = curr.next
    return llist


def reverse_list(llist):
    prev = None
    curr = llist
    following = llist
    while curr is not None:
        following = following.next
        curr.next = prev
        prev = curr
        curr = following
    return prev


def llist_to_array(llist):
    current = llist.head
    arr = []
    while current is not None:
        arr.append(current.val)
        current = current.next
    # print("arr", arr)
    return arr


def addTwoNumbers(l1, l2):
    result = []
    remainder = 0
    curr_1 = l1.head
    curr_2 = l2.head

    print("curr_1", curr_1)
    while curr_1 or curr_2:
        if curr_1 is None:
            curr_1_val = 0
        else:
            curr_1_val = curr_1.val

        if curr_2 is None:
            curr_2_val = 0
        else:
            curr_2_val = curr_2.val

        numToAdd = curr_1_val + curr_2_val + remainder
        if numToAdd >= 10:
            numToAdd = numToAdd % 10
            remainder = 1
        else:
            remainder = 0
        result.append(numToAdd)
        if curr_1 and curr_1.next:
            curr_1 = curr_1.next
        else:
            curr_1 = None

        if curr_2 and curr_2.next:
            curr_2 = curr_2.next
        else:
            curr_2 = None
    if remainder != 0:
        result.append(remainder)
    print("result", result)
    return result


def main():
    test_cases = [
        [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]],
        [[0], [0], [0]],
        [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
    ]
    pass_count = 0
    failed_cases = []
    for idx, case in enumerate(test_cases):
        print("idx, case", idx, case)
        num_1 = case[0]
        num_2 = case[1]
        result = case[-1]

        node_list_1 = create_nodes(num_list=num_1)
        node_list_2 = create_nodes(num_list=num_2)
        l1 = create_linked_list(node_list_1)
        l2 = create_linked_list(node_list_2)

        l1.print_list()
        l2.print_list()

        answer = addTwoNumbers(l1, l2)
        if answer == result:
            pass_count += 1
        else:
            failed_cases.append(idx)

        # convert list to linked list
        node_list_3 = create_nodes(answer)
        l3 = create_linked_list(node_list_3)
        l3.print_list()

    print(f"Passed {pass_count}/{len(test_cases)} test cases")
    if len(failed_cases) != 0:
        print("The following test cases failed")
        for idx in failed_cases:
            print(test_cases[idx])


main()
