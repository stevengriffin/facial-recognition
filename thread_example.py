import queue
import threading
import time

q = queue.Queue()
frame_length = 0.2


def pull_from_queue():
    target_time = time.time()
    while True:
        target_time += frame_length
        item = q.get()
        if item is None:
            break
        print(item)
        q.task_done()
        end = time.time()
        time.sleep(max(0, target_time - time.time()))

def add_to_queue():
    while True:
        start = time.time()
        for i in range(5):
            q.put(i)
        end = time.time()
        time.sleep(frame_length * 5 - (end - start))

pull_thread = threading.Thread(target=pull_from_queue)
pull_thread.start()
add_thread = threading.Thread(target=add_to_queue)
add_thread.start()
