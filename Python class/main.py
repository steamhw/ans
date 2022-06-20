from datetime import datetime

class Person :
  def __init__(self, name = None) :
    self.__name = name #Assign name to __name data attribute
    self.__gender = None #Default is None datatype
    self.__day = None
    self.__month = None
    self.__year = None
    self.__phone = None
  def setGender(self, gender) :
    if (gender[0].upper() == 'M') or (gender[0].upper() == 'F') :
      self.__gender = gender[0].upper()
  def getDOB(self, format='B') : #Default to British date format
    if self.__day and self.__month and self.__year :
      if (format == 'A') : #Date in America format
        return "{}/{}/{}".format(self.__month, self.__day, self.__year)
      elif (format == 'B') : #Date in British format
        return "{}/{}/{}".format(self.__day, self.__month, self.__year)
      elif (format == 'C') : #Date in Chinese format
        return "{}/{}/{}".format(self.__year, self.__month, self.__day)
  def getAge(self) :
   if self.__year : #Return age only if year of birth is available
     return datetime.today().year - self.__year #Calculate age
  def setPhoneNumber(self, phoneNum):
    self.__phone = phoneNum
  def getPhoneNumber(self):
    return '('+self.__phone[:3]+')'+self.__phone[3:6]+'-'+self.__phone[-4:]
  def getGender(self):
    if self.__gender == 'M':
      return 'Male'
    else:
      return 'Female'


p1 = Person('example')
p1.setPhoneNumber('0123456789')
print(p1.getPhoneNumber())
p1.setGender('f')
print(p1.getGender())
