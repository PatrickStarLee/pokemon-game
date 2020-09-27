print("Hello world")
#comment using #

import json
#Notes:
#how to load a json file to an obj and how to print something from a json file
#instead of open(filename) and filename.close(), use 'with' to make opening files more efficient
with open('message.json') as message_json:#message.json is a file name
  message = json.load(message_json)
  print(message['text'])

#dumping an obj into a json file
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)
  #first arg is the obj you're dumping from, second obj is the file you're dumping to

#Additional notes:
#.read() is to read the whole file
#.readline() is to read the first line in the file
#.write() is to write something in the file 
#'w' is used to create a new file and write contents; 'a' is to append or add something to the file

#classes and methods
class Rules:
  def washing_brushes(self):#when declaring a method, 1st arugment is always self b/c methods have >= 1 argument
                            #happens if self is the only argument u must pass
    return 'Point bristles towards the basin while washing your brushes.'


class Circle:
  pi = 3.14
  def area(self, radius):
    area = Circle.pi * radius**2#when calling a class variable, must do classname.variable name
    return area

circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):#__init__ refers to a constructor of that class
    print("New circle with diameter: " + str(diameter))

teaching_table = Circle(36)


#Instant variables
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()
#store name is specific to the objs
alternative_rocks.store_name = 'Alternative Rocks'
isabelles_ices.store_name = "Isabelle's Ices"

#Review
'''
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
'''

'''
Cheat Sheet on CSV Files (related to JSON files)
In Python, the csv module implements classes to read and write tabular data in CSV format.
It has a class DictWriter which operates like a regular writer but maps a dictionary onto output rows.
The keys of the dictionary are column names while values are actual data.
The csv.DictWriter constructor takes two arguments.
The first is the open file handler that the CSV is being written to.
The second named parameter, fieldnames, is a list of field names that the CSV is going to handle.

'''