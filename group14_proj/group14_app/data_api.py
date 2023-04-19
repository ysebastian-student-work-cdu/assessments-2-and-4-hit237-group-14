"""
Data Model API configuration for for group14_proj project.

1. To create a table use the below framwork.
    items = Create("Item","Type","Description","ID")

    item -> is the name of the table instance 
    first argument is the table name and the rest are table attributes.

2. To insert records into a table use the below syntax. 

    Table(contacts,["Muhammad Firdaus Roslan","S328473","External"])
    
    contacts - > name of the table instance 
    [] -> inclues the records to go into the table on a list 
    
3.To print all the records in a table use the below syntax
    contacts.show_records()
    
    contacts -> name of the table instance 
    show_records() is a method in Create class 
    
4.To print a single nominated record in a table use the below syntax
    items.show_item(0)
    
    items -> name of the table instance 
    show_item(0) is a method in Create class 
    attribute to the show_item() is the position of the reocrd 
    
5. To show attributes of a table use below syntax
    items.show_attributes()
    
    items-> name of the table instance 
    show_attributes() is a method in Create class
    
6. To get all the records of a table use below syntax
    items.get_records()
    
    items-> name of the table instance 
    get_records() is a method in Create class
    
    
7. To get a single record in a table use the below syntax
    items.item_item(0)ccf
    
    items -> name of the table instance 
    get_item(0) is a method in Create class 
    attribute to the get_item() is the position of the reocrd 
"""

from group14_app.schema import *
from group14_app.table import *

#----------------------create tables---------------------

items = Create("Item",'type','description','id')
contacts = Create("contacts","name","id","attendance")
briefs = Create("intro","brief")
mitigations = Create("mitigation","one","two","three") 


#-----------------------insert records------------------

#insert rows to Items table
Table(items,["Household waste","'This is the food waste that occurs in our homes, including food that is left uneaten on plates, expired or spoiled food, and food that is thrown away because it is no longer wanted.","1"])         
Table(items,['Retail waste','This includes food that is thrown away by supermarkets, grocery stores, and other food retailers due to overstocking, expiration, or damage.',"2"])         
Table(items,['Restaurant waste','This is the food waste that occurs in restaurants, cafes, and other food service establishments, including food that is left uneaten by customers, overproduction, and spoilage.',"3"])         
Table(items,['Agricultural waste','This includes food that is lost during the production and harvesting of crops, such as fruits and vegetables that are left in the field due to overproduction or damage.',"4"])         
Table(items,['Processing waste','This is the food waste that occurs during the processing and manufacturing of food products, including scraps, trimmings, and packaging waste.',"5"])         
Table(items,['Transportation and distribution waste','This includes food that is lost during transportation and distribution, such as spoilage and damage during transit.',"6"])         

#insert rows to Contacts table
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
