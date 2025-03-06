class Mydictionary:
    def __init__(self):
        self.data={}

    def create_dict(self,key,value):
        self.data[key]= value
    def display(self):
        print(self.data)


obj= Mydictionary()
obj.create_dict("Name","Ankita")
obj.create_dict("Job","SDE")
obj.create_dict("City","Bangalore")
obj.create_dict("Country","India")
obj.create_dict("Salary","20LPA")

obj.display()



    