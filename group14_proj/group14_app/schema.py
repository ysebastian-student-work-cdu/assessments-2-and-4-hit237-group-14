# class Detail:
    
#     details=[]
    
#     def __init__(self,new):
#         Detail.details.append(new)

#     def show_records():
#         return Detail.details
    
# muhammad = Detail({"name":"Muhammad Firdaus Roslan","id":"S328473","attendance":"External"})
# emily  = Detail({"name":"Emily Wai Sum Tsang","id":"S344909","attendance":"External"})
# amila = Detail({"name":"Amila Kolamba Arachchige","id":"S356967","attendance":"External"})
# putu = Detail({"name":"I Putu Mahesa Gangga Wisuda","id":"S355549","attendance":"External"})

# print(Detail.show_records())

#This class creates table schema

class Create:
    
    def __init__(self,name,*args):
        self.create_table(name,*args)
        
    def create_table(self,name,*args):
        self.records = []
        self.table_schema=[]
        self.name = name
        for arg in args:
            self.table_schema.append(arg)
            
    def show_attributes(self):
        for i in range(0,len(self.table_schema)):
            print(self.table_schema[i])
            
    def show_records(self):
        for i in self.records:
            print(i)
            
#create items table
items = Create("Item",'type','description','id')

#create contacts table
contacts = Create("contacts","name","id","attendance")

#create website intro table
briefs = Create("intro","brief")

#create new table for mitigations
mitigations = Create("mitigation","one","two","three") 