import json
import threading
import copy

class actionClass:

  action_data = []
  action_count = []
  
  #Used in both addAction and getStats methods to support concurrency
  lock = threading.Lock()

  def __init__(self):
    self.action_data = []
    self.action_count = []


  def addAction(self, data):

    with self.lock:

      #Passed in 'data' value gets manipulated. We need a shallow copy to work with
      dataCopy = copy.copy(data)

      #Flag to return success/failure of method
      success = True

      if self.validateData(data):
        
        #Flag to determine if data is already in action_data
        exists = False

        for index, item in enumerate(self.action_data):

          #'action' already exists. Let's increment it's count
          if ( item["action"] == data["action"] ):
            self.action_count[index]["count"] +=1
            item["avg"] = item["avg"] + dataCopy["avg"]
            exists = True
            break
          
        #New 'action'. Let's add it to our list of action_data and start a count of occurences
        #for calculating the average.
        if ( not exists ):
          self.action_data.append(dataCopy)
          self.action_count.append({"action" : dataCopy["action"], "count" : 1})

      else :
        success = False

    return success

  def getStats(self):
    
    #Make sure nobody is touching our data while printing stats!
    with self.lock:

      for index, item in enumerate(self.action_data):
          countData = self.action_count[index]
          item["avg"] = item["avg"] / self.action_count[index]["count"]
      return json.dumps(self.action_data)



  #Perform some simple checks to verify we are working with valid data
  def validateData(self, data):
    valid = True
    raw_data = json.dumps(data)

    if ( len(data.keys()) != 2 ):
        print("Expecting 2 key/value pairs in data, got: ")
        print("\tLength: " + str(len(data.keys())))
        print("\tInput: " + raw_data)
        valid = False

    if ( "avg" not in data ):
      print("Input missing required value 'avg'.")
      print("\tInput: " + raw_data)
      valid = False
      
    elif ( not isinstance(data["avg"], int) and ( not isinstance(data["avg"], float)) ):
      print("Input 'avg' expected to be int or float, but got:")
      print("\tType: " + str(type(data["avg"])))
      print("\tInput: " + str(raw_data))
      valid = False

    if ( "action" not in data ):
      print("Input missing required value 'action'.")
      print("\tInput: " + raw_data)
      valid = False
      
    elif ( not isinstance(data["action"], str) ):
      print("Input 'action' expected to be type 'str' but got:")
      print("\tType: " + str(type(data["action"])))
      print("\tInput: " + str(raw_data))
      valid = False
      

    if ( not valid ):
      print("\tInvalid Action was not added. See above error. Continuing...")

    return valid







