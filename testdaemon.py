import logging
import random
import threading
import time

# https://pypi.python.org/pypi/python-daemon/
from daemon import runner
from queue import Queue


class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name
        self.q = kwargs.get('q')
        self.logger = kwargs.get('logger')
        return

    def run(self):
        while True:
            if not self.q.full():
                item = random.randint(1,10)
                self.q.put(item)
                self.logger.info('Putting ' + str(item)  
                              + ' : ' + str(self.q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return


class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        self.q = kwargs.get('q')
        self.logger = kwargs.get('logger')
        return

    def run(self):
        while True:
            if not self.q.empty():
                item = self.q.get()
                self.logger.info('Getting ' + str(item) 
                              + ' : ' + str(self.q.qsize()) + ' items in queue')
                time.sleep(random.random())
        return


class QueuedBatch(object):

    BUF_SIZE = 5
    
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        self.pidfile_path =  '/Users/admin/Documents/tests/python-tester/python-tester/testdaemon.pid'
        self.pidfile_timeout = 5
        self.q = Queue(self.BUF_SIZE)
            
    def run(self):

        self.p = ProducerThread(name='producer', kwargs={'q': self.q, 'logger': logger})
        self.c = ConsumerThread(name='consumer', kwargs={'q': self.q, 'logger': logger})

        self.p.start()
        # time.sleep(2)
        self.c.start()
        # time.sleep(2)

        while True:
            logger.debug("Debug message")
            logger.info("Info message")
            logger.warn("Warning message")
            logger.error("Error message")
            logger.info("queue: " + str(self.q))
            time.sleep(10)


app = QueuedBatch()
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/Users/admin/Documents/tests/python-tester/python-tester/testdaemon.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

daemon_runner = runner.DaemonRunner(app)
# This ensures that the logger file handle does not get closed during daemonization.
daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()
