import multiprocessing as mp
import time

def job(v,num):
# def job(v, num, l):

    # l.acquire()
    for _ in range(5):
        time.sleep(0.1)
        v.value+=num
        print(v.value,end='\n')
    # l.release()

def multicore():
    # l=mp.Lock()
    v=mp.Value("i",0)
    # p1=mp.Process(target=job,args=(v,1,l))
    # p2=mp.Process(target=job,args=(v,3,l))
    p1=mp.Process(target=job,args=(v,1))
    p2=mp.Process(target=job,args=(v,3))
    p1.start()
    p2.start()
    p2.join()
    p1.join()

if __name__=='__main__':
    multicore()