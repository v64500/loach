from loach.utils import retry
from queue import Queue
from loach.utils.exception import *

@retry(forever=True)
def func(q, times=None):
    e = q.get()
    print(e)
    raise DouYinUnknowException(msg="times:%d" % times)

q = Queue(maxsize=10)
for i in range(10):
    q.put(i)

func(q)