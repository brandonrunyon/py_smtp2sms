class NameResolution():

#default constructor to create object like this:
# nr = NameResolution()

   def __init__(self):
      self.__doc__ =  "Object to handle service provider to SMS Gateway name resolution."
      pass

#member that takes a string and 
#

   def get_server(self, name):
      self.__doc__ = "EXAMPLE: nr.get_server('at&t') ---> 'txt.att.net'"
      self.gatewayList = {'alltel': 'message.alltel.com','at&t':'txt.att.net', 'verizon':'vtext.com','uscellular':'email.uscc.net' }    
      self.name = name.lower()
      return self.gatewayList[name]






 



