class Detail:
    
    details=[]
    
    def __init__(self,new):
        Detail.details.append(new)

    def show_records():
        return Detail.details
    
muhammad = Detail({"name":"Muhammad Firdaus Roslan","id":"S328473","attendance":"External"})
emily  = Detail({"name":"Emily Wai Sum Tsang","id":"S344909","attendance":"External"})
amila = Detail({"name":"Amila Kolamba Arachchige","id":"S356967","attendance":"External"})
putu = Detail({"name":"I Putu Mahesa Gangga Wisuda","id":"S355549","attendance":"External"})

print(Detail.show_records())