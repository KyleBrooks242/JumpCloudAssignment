import json

class actionClass:

  action_data = []

  def __init__(self):
    self.action_data = []


  def addAction(self, data):
    #Flag to return success/failure of method
    success = True

    if self.validateData(data):

      #Flag to determine if data exists or not
      exists = False

      #Add a count value to the incoming data to compute average
      data.update({"count" : 1})
    
      for item in self.action_data:
        if item["action"] == data["action"]:
          print(data["action"] + " already exists. Adding to count...")
          item["count"] = item["count"] + 1
          item["avg"] = item["avg"] + data["avg"]
          exists = True
          break

      if not exists:
        self.action_data.append(data)

    else :
      success = False
    
    return success

  def getStats(self):
    for item in self.action_data:
        item["avg"] = item["avg"] / item["count"]
    return json.dumps(self.action_data)


  
  #Perform some simple checks to verify we are working with valid data
  def validateData(self, data):
    valid = True
    raw_data = json.dumps(data)
    
    if (len(data.keys()) != 2):
        print("Expecting 2 key/value pairs in data, got: " + str(len(data.keys())))
        print("input: " + raw_data) 
        valid = False

    if "avg" not in data:
      print("Input missing required value 'avg'. Input: " + raw_data)
      valid = False

    if "action" not in data:
      print("Input missing required value 'action'. Input: " + raw_data)
      valid = False


    return valid
      



def main():
  test = actionClass()
  action1 = {"action": "jump", "avg":100}
  action2 = {"action": "skip", "avg":50}
  action3 = {"action": "hop", "avg":90}
  action4 = {"action": "jump", "avg":80}
  action5 = {"clown" : "show", "avg" :90,}

  test.addAction(action1)
  test.addAction(action2)
  test.addAction(action3)
  test.addAction(action4)
  test.addAction(action5)

  print("*************\n")
  print(test.getStats() + "\n")
  print("*************\n")
  




if __name__ == '__main__':
  main()


  
  
