from concurrent.futures import ThreadPoolExecutor
import random
import string
import time


class ThreadPool:
    
    def __init__(self,workers=None):
        self.pool = ThreadPoolExecutor(max_workers=workers)
        self.workers=workers
        self.thread_pool = []

    def worken_func(self,filename):
        randomnumber = random.randint(1,100)
        filecontent = f"This file contains random number {randomnumber}"
        with open(filename, 'w') as file:
            file.write(filecontent)

    def filename_generator(self):
        letters = string.ascii_letters + string.digits
        filename = "".join([random.choice(letters) for _ in range(10)])+".txt"
        return filename

    def start(self):
        for _ in range(self.workers):
            thread = self.pool.submit(self.worken_func,self.filename_generator())
            self.thread_pool.append(thread)

    def response(self):
        for thread in self.thread_pool:
            if thread._state == "FINISHED":
                print ("File saved successfully")
            else:
                print("File not saved")


if __name__=='__main__':
    pool = ThreadPool(5)
    pool.start()
    time.sleep(5)
    pool.response()