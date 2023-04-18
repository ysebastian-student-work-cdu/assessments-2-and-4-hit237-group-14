from group14_app.schema import *

class Table:
    
    def __init__(self,table,row):
            self.add_record(table, row)
   
    def add_record(self,table,row):
        if len(row) != len(table.table_schema):
            raise TypeError(f'takes only {len(table.table_schema)} arguments but {len(row)} given')
        else:
            record ={}
            for col, index in zip(table.table_schema,range(0,len(table.table_schema))):
                record[col] = row[index]
            table.records.append(record)
            
#insert rows to items table        
Table(items,["Household waste","'This is the food waste that occurs in our homes, including food that is left uneaten on plates, expired or spoiled food, and food that is thrown away because it is no longer wanted.","1"])         
Table(items,['Retail waste','This includes food that is thrown away by supermarkets, grocery stores, and other food retailers due to overstocking, expiration, or damage.',"2"])         
Table(items,['Restaurant waste','This is the food waste that occurs in restaurants, cafes, and other food service establishments, including food that is left uneaten by customers, overproduction, and spoilage.',"3"])         
Table(items,['Agricultural waste','This includes food that is lost during the production and harvesting of crops, such as fruits and vegetables that are left in the field due to overproduction or damage.',"4"])         
Table(items,['Processing waste','This is the food waste that occurs during the processing and manufacturing of food products, including scraps, trimmings, and packaging waste.',"5"])         
Table(items,['Transportation and distribution waste','This includes food that is lost during transportation and distribution, such as spoilage and damage during transit.',"6"])         

#insert rows to contacts table
Table(contacts,["Muhammad Firdaus Roslan","S328473","External"])
Table(contacts,["Emily Wai Sum Tsang","S344909","External"])
Table(contacts,["Amila Kolamba Arachchige","S356967","External"])
Table(contacts,["I Putu Mahesa Gangga Wisuda","S355549","External"])





