This assignment is to create a class that allows for the manipulation of 'actions'
There are two methods required for this class:

1. Add Action
addAction (string) returning error
This function accepts a json serialized string of the form below and maintains an average time
for each action. 3 sample inputs:
1) {"action":"jump", "time":100}
2) {"action":"run", "time":75}
3) {"action":"jump", "time":200}
Assume that an end user will be making concurrent calls into this function.
2. Statistics
getStats () returning string
Write a second function that accepts no input and returns a serialized json array of the average
time for each action that has been provided to the addAction function. Output after the 3
sample calls above would be:
[
{"action":"jump", "avg":150},
{"action":"run", "avg":75}
]
Assume that an end user will be making concurrent calls into this function.


USAGE:
This class can be imported into your python program using the following:
  `from actionClass import *`


Example:

`from actionClass import *

def main():
  testClass = actionClass()

  sampleAction1 = {"action" : "jump", "avg" : 100}
  sampleAction2 = {"action" : "skip", "avg" : 50}

  testClass.addAction(sampleAction1)
  testClass.addAction(sampleAction2)

  testClass.getStats()

  `

  Output would be:

  '[{"action": "jump", "avg": 100.0}, {"action": "skip", "avg": 50.0}]'


Please see sample 'ConcurrencyTest' to see a full example use case.

**Note that actionClass.py will need to be in the same directory as your python program,
or the file location added to your PYTHON_PATH**

Linux/Mac:
Edit your  ~/.bashrc file and include this line at the bottom:
`export PYTHONPATH="${PYTHONPATH}:/my/other/path"`
Run the following to pick up these changes in your terminal:
`source ~/.bashrc`

Windows:
https://youtu.be/Y2q_b4ugPWk?t=49






FUTURE CONSIDERATION:
Currently, the code supports adding 'actions', but not removing them. I think
this would be neat functionality to have.

TRICKY SPOTS:
If you take a look in actionClass.addAction(self, data), you'll notice this line
`copyData = copy.copy(copyData)`
In my testing, it became apparent that somehow, somewhere, `data` was getting
modified, subsequently throwing off the final average stats. I spent some time
trying to track down where this was happening with no luck. I'm not giving up
just yet, though.
