# string slicing
#lang = "Selenium"
#print(lang[1])


#Step Argument
#print("Shivam Bhargava"[2:9:3])


class classname:
    def createname(self,name):
        self.name = name
    def displayname(self):
        return self.name
    def saying(self):
        print ("hello %s" % self.name)



first = classname()
second = classname()
first.createname("shivam")
second.createname("bhargav")
print(first.displayname())