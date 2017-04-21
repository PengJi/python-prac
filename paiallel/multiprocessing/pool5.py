# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random

def long_time_task(name, string):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
    print string

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
	# Pool的默认大小是CPU的核数
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,'test'))
    print 'Waiting for all subprocesses done...'
    p.close()
	# 等待所有子进程执行完毕
    p.join()
    print 'All subprocesses done.'
