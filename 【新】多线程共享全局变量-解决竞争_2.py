import threading
import time

R_num = 0
def test1():
    global R_num

    for i in range(1000000):
        mutex.acquire()
        R_num += 1
        mutex.release()
    print('-----in test1----R_num = %d-----' % R_num)

def test2():
    global R_num

    for i in range(1000000):
        mutex.acquire()
        R_num += 1
        mutex.release()
    print('-----in test2----R_num = %d-----' % R_num)

mutex = threading.Lock()

def main():
    t1 = threading.Thread(target = test1)
    t2 = threading.Thread(target = test2)

    t1.start()

    t2.start()
    time.sleep(1)

    print('-----in main----R_num = %d-----' % R_num)

if __name__ == '__main__':
    main()