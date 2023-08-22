import queue as q


def main():

    q1 = q.LQueue()

    for i in range(10):
        q1.insert(i)

    for i in range(10):
        print(q1.pop())

    print(q1.is_empty())


main()
