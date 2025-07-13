from common_utils.constants import QUEUE_MAX_SIZE

class Queue():
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = -1

    def is_empty(self):
        return self.tail - self.head == -1

    def is_full(self):
        return (self.tail - self.head) == (QUEUE_MAX_SIZE - 1)

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full, cannot enqueue anymore.")
            return
        else:
            self.queue.append(element)
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot remove elements.")
            return
        else:
            self.queue.remove(self.queue[0])
            self.head += 1

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty, no elements to print out.")
        else:
            print(" ".join([str(element) for element in self.queue]))

def main():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print("Initial queue")
    queue.print_queue()

    queue.dequeue()

    print("After removing an element from the queue")
    queue.print_queue()

    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)

    print("Current queue")
    queue.print_queue()

    queue.enqueue(11)

    print("Current queue")
    queue.print_queue()

    queue.enqueue(1)

    for _ in range(9):
        queue.dequeue()

        print("After removing an element from the queue")
        queue.print_queue()


if __name__ == "__main__":
    main()