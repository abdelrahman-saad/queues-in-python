import imporoved_queue as IQ


def main():

    q1 = IQ.ImprovedQueue(10, 'first queue')
    # q1 = IQ.ImprovedQueue('abc', 'first queue')

    for i in range(10):
        q1.insert(i)

    search_queue = IQ.ImprovedQueue.get_queue('first queue')
    print(search_queue)
    print(search_queue['data'])
    for i in range(10):
        print(q1.pop())

    print(q1.is_empty())


main()
