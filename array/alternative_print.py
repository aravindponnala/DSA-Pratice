"""
Given an array arr[], the task is to print every alternate element of the array starting from the first element.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50
Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).


Input: arr[] = [-5, 1, 4, 2, 12]
Output: -5 4 12


"""


# metod 1 python inbuilt
def array_alternative(ar):
    return ar[::2]


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5]
    res = array_alternative(ar)
    print(res)


# method with loops


def array_alternative2(ar):
    res = []
    for i in range(0, len(ar), 2):
        print(i)
        print(res)
        res = res.append(ar[i])

    return res


if __name__ == "__main__":
    ar = [10, 20, 30, 40, 50]
    res = array_alternative2(ar)
    print(res)
