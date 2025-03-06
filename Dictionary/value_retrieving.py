class Mydictionary:
    def __init__(self):
        self.data={}
    def create_dict(self,key,value):
        self.data[key]= value
    def display(self):
        print(self.data)
    def fetch_data(self,key):
        if key in self.data:
            print(self.data[key])
        else:
            print(f"Key '{key}' not found.")


obj= Mydictionary()
obj.create_dict("Name","Ankita")
obj.create_dict("Job","SDE")
obj.create_dict("City","Bangalore")
obj.create_dict("Country","India")
obj.create_dict("Salary","20LPA")

obj.fetch_data("job")