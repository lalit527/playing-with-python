"""
Prefer classes over bookkeeping with Dictionaries and tuples
"""
class SimpleGraderbook:
  def __init__(self):
    self._grades = {}
  
  def add_student(self, name):
    self._grades[name] = []

  def report_grade(self, name, score):
    self._grades[name].append(score)

  def average_grade(self, name):
    grades = self._grades[name]
    return sum(grades) / len(grades)

book = SimpleGraderbook()
book.add_student('Isaac')
book.report_grade('Issac', 90)
print(book.average_grade('Isaac'))

"""
Storing student as key, which has a dictonary which has subject as key and value marks
"""
class BySubjectGradebook: 
  def __init__(self): 
    self._grades = {} 
  
  def add_student(self, name): 
    self._grades[name] = {}

  def report_grade(self, name, subject, grade):
    by_subject = self._grades[name] 
    grade_list = by_subject.setdefault(subject, []) 
    grade_list.append(grade)

  def average_grade(self, name):
    by_subject = self._grades[name] 
    total, count = 0, 0 
    for grades in by_subject.values():
      total += sum(grades)
      count += len(grades) 
    return total / count

print("========================================================")
print("=======Refactoring to classes=====")
print("========================================================")
class Subject:
  def __init__(self):
    self.grades = []
  
  def report_grade(self, score, weight):
    self._grades.append(Grade(score, weight))

  def average_grade(self):
    total, total_weight = 0, 0
    for grade in self._grades:
      total += grade.score * grade.weight
      total_weight += grade.weight
    return total / total_weight

class Student:
  def __init__(self):
    self._subjects = {}
  def subject(self, name):
    if name not in self._subjects:
      self._subjects[name] = Subject() 
    return self._subjects[name]
  def average_grade(self):
    total, count = 0, 0 
    for subject in self._subjects.values():
      total += subject.average_grade()
      count += 1 
    return total / count


class Gradebook(object):
  def __init__(self):
    self._students = {}
  def student(self, name):
    if name not in self._students:
      self._students[name] = Student() 
    return self._students[name]

book = Gradebook()
albert = book.student('Albert')
math = albert.subject('Math')
math.report_grade(80, 0.10)
print(albert.average_grade())