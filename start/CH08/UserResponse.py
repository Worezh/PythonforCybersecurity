class UserResponse:
  def __init__(self, data):
    self.gender = data['gender']
    self.name = Name(data['name'])
    self.location = Location(data['location'])
    self.email = data['email']
    self.login = Login(data['login'])
    self.dob = DOB(data['dob'])
    self.phone = data['phone']
    self.cell = data['cell']

class Name:
  def __init__(self, data):
    self.title = data['title']
    self.first = data['first']
    self.last = data['last']

class Location:
  def __init__(self, data):
    self.street = Street(data['street'])
    self.city = data['city']
    self.state = data['state']
    self.country = data['country']
    self.postcode = data['postcode']

class Street:
  def __init__(self, data):
    self.number = data['number']
    self.name = data['name']

class Login:
  def __init__(self, data):
    self.username = data['username']
    self.password = data['password']

class DOB:
  def __init__(self, data):
    self.date = data['date']
    self.age = data['age']