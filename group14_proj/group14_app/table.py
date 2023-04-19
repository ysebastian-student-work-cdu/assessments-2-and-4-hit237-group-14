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

#insert rows to website intro table
Table(briefs,["Welcome to our website which is focused on food waste and mitigation! We are dedicated to addressing one of the pressing global issues of our time: food waste. Every year, billions of tons of food are wasted worldwide, contributing to environmental, social, and economic challenges, especially in Australia. Our website serves as a comprehensive resource for individuals, businesses, and communities seeking information and solutions to reduce food waste and its impacts, specifially in household waste, retail waste, restaurant waste, agricultural waste, processing waste, and transportation and distribution waste. We will provide some solutions from practical tips on reducing food waste at home, to innovative strategies for businesses and policymakers, our website offers a wealth of knowledge, tools, and resources to promote sustainable practices and mitigate the adverse effects of food waste. Join us in the fight against food waste, and together, we can make a positive impact on our planet and society. Explore our website and discover how you can contribute to the global effort to reduce food waste and create a more sustainable future for all"])

#insert rows to mitigation table
Table(mitigations,["Household Waste", "○ Reduce, reuse and reycle plastic, bottles, glass and newspapers to recycling centers or local charities", "○ Clean tools, store toys and resell outdoor furnitures to keep them out of landfills"])
Table(mitigations,["Retail Waste", "○ Reduce energy output of LED lights as it contributes to gashouse emissions", "○ Avoid using plastic grocery bags but instead stock up reusable grocery bags"])
Table(mitigations,["Restaurant Waste", "○ Practise efficient stock control by labelling foods with 'best before' and 'sell by' dates to avoid food waste", "○ Donate food that are close to the best before date to charities as they contribute to homeless"])
Table(mitigations,["Agricultural Waste", "○ Compost food waste by making them into natural fertilisers to help grow fruits and vegetables", "○ Avoid buying too much products as coming in to stores regularly is better than increasing food waste"])
Table(mitigations,["Processing Waste", "○ Manage hazardous waste by using specialised handling tools and proper disposal to ensure that there is no risk to the environment", "○ Turning waste to energy involves turning processed waste into energy products like electricity and heat that would otherwise get dumped in landfills"])
Table(mitigations,["Transportation Waste", "○ Using alternative transporation like bikes, walking, running and etc. will reduce fuel consumption and lower emissions", "○ Sharing shipments with other companies can help reduce the number of trips that needs to be taken from the warehouse and to the destination"])




