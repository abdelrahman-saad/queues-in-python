import LQueue as Q


def prog():

    # This adds 3 queues in the file and load them

    data = Q.LQueue.load('./queue_data.txt')
    Q.LQueue.append_all(data)
    q1 = Q.LQueue()
    q2 = Q.LQueue()
    q3 = Q.LQueue()

    for i in range(10):
        q1.insert(i)
        q2.insert(i + 10)
        q3.insert(i + 20)

    print(Q.LQueue.save("./queue_data.txt"))

    # q1 = IQ.ImprovedQueue(10, 'first queue')
    # # q1 = IQ.ImprovedQueue('abc', 'first queue')
    #
    # for i in range(10):
    #     q1.insert(i)
    #
    # search_queue = IQ.ImprovedQueue.get_queue('first queue')
    # print(search_queue)
    # print(search_queue['data'])
    # for i in range(10):
    #     print(q1.pop())
    #
    # print(q1.is_empty())


prog()
