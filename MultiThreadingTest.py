import logging
import os
from queue import Queue
from threading import Thread
from time import time

from actionClass import *

##This is a simple test to ensure actionClass.py supports concurrent processing.
##The test instantiates the specified number of 'workers' and attempts to
##concurrently access a shared instance of actionClass. The results can be
##validated by the user

##Steps
##1.) Create sample 'actions'
##2.) Add multiple instances of these actions to a shared queue
##3.) Create the specified number of 'workers' to utilize the
##    actionClass.addAction() functionality
##4.) Print out results



#Global class to be accessed by all instances of ActionWorker
testClass = actionClass()

class ActionWorker(Thread):

  def __init__(self, queue, num):
    Thread.__init__(self)
    self.queue = queue
    self.num = num

  def run(self):
    while True:
      # Get the work from the queue and expand the tuple
      action = None
      action = self.queue.get()
      try:
         testClass.addAction(action)
      finally:
        self.queue.task_done()

def main():
  
  NUM_LOOP_ITERATIONS = 28
  NUM_ACTIONS = 7
  
  action1 = {"action": "jump", "avg":100}
  action2 = {"action": "skip", "avg":200}
  action3 = {"action": "hop", "avg":400}
  action4 = {"this" : "should", "fail" : "validation"} #should fail due to no 'action' or 'avg' k/v pair
  action5 = {"action" : "run", "avg" : "100"} #should fail due to avg type != int/float
  action6 = {"action" : 14, "avg" : 100} # should fail due to action type != str
  action7 = {} #Should fail due to lack of data
  
  actionList = [action1, action2, action3, action4, action5, action6, action7]
  

  # Create a queue to communicate with the worker threads
  queue = Queue()
  # Put the tasks into the queue as a tuple
  for y in range(NUM_LOOP_ITERATIONS):
     queue.put(actionList[y % NUM_ACTIONS])
  # Create 8 worker threads
  for x in range(NUM_LOOP_ITERATIONS):
    worker = ActionWorker(queue, x)
    # Setting daemon to True will let the main thread exit even though the workers are blocking
    worker.daemon = True
    worker.start()
  
  # Causes the main thread to wait for the queue to finish processing all the tasks
  #print(list(queue.queue))
  queue.join()

  print(testClass.getStats())

if __name__ == '__main__':
    main()


