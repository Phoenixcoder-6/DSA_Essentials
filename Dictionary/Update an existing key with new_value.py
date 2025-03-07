class MyDictionary:
    def __init__(self):
        self.data={}
    def create_dict(self,key,value):
        self.data[key]=value
    def update_dict(self,key,updated_value):
        if key in self.data:
            self.data[key]= updated_value
        else:
            print(f"{key} is not present")

    def display(self):
        print(self.data)


obj= MyDictionary()
obj.create_dict("Name","Ankita")
obj.create_dict("Job","SDE")
obj.create_dict("City","Bangalore")
obj.create_dict("Country","India")
obj.create_dict("Salary","20LPA")
obj.display()
obj.update_dict("Salary","45LPA")
obj.display()


