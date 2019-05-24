import threading
import time
def T1_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():
    print("T2 start\n")
    print("T2 finish\n")

added_thread1=threading.Thread(target=T1_job, name='T1')
added_thread2=threading.Thread(target=T2_job, name='T2')
added_thread1.start()
added_thread2.start()
added_thread2.join()
added_thread1.join()
# added_thread1.join()
print("all done\n")
print(threading.active_count())