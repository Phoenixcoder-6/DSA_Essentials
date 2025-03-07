class MyDictionary:
    def __init__(self):
        self.data={}
    def create_dict(self,key,value):
        self.data[key]= value
    def update_dict(self,key,value):
        self.data[key]= value
    def display(self):
        print(self.data)

obj= MyDictionary()
obj.create_dict("Name","Ankita")
obj.create_dict("Age",24)
obj.create_dict("City","Kolkata")

obj.display()

obj.update_dict("Country","India")
obj.display()


        