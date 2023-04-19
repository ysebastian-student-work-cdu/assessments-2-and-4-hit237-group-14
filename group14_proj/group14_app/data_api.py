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
food_details = Create("food_details","name","desc")

#-----------------------insert records------------------

#insert rows to Items table
Table(items,["Household waste","'This is the food waste that occurs in our homes, including food that is left uneaten on plates, expired or spoiled food, and food that is thrown away because it is no longer wanted.",0])         
Table(items,['Retail waste','This includes food that is thrown away by supermarkets, grocery stores, and other food retailers due to overstocking, expiration, or damage.',1])         
Table(items,['Restaurant waste','This is the food waste that occurs in restaurants, cafes, and other food service establishments, including food that is left uneaten by customers, overproduction, and spoilage.',2])         
Table(items,['Agricultural waste','This includes food that is lost during the production and harvesting of crops, such as fruits and vegetables that are left in the field due to overproduction or damage.',3])         
Table(items,['Processing waste','This is the food waste that occurs during the processing and manufacturing of food products, including scraps, trimmings, and packaging waste.',4])         
Table(items,['Transportation and distribution waste','This includes food that is lost during transportation and distribution, such as spoilage and damage during transit.',5])         

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

#insert rows to fooddetails table
title_1 = 'Household Waste'
wordings_1 = '''

Every Australians have been throwing out 550 killogrammes of household waste per person in a single year. Every person in a household would be throwing out roughly 15 kg every week. This have been accumulating 67 million tonnes of recycled rubbish which have been produced in the span of a single year, while 20 million tonnes are left to be thrown out in landfills. Over 150,000 million tonnes of plastics have been moving through the rivers and ocean, contaminating the saltwater which affects the aquatic species heavily. 

Household wastes have been accumulating for 1.88 million tonnes in 2007, left to be thrown in landfills rather than recycling plastics. This has been collected from kerbside bin services, roughly around 1.24 million tonnes of rubbish. 

So what are the examples of Household Waste?

• Plastic Bags and Bin Liners
• Foam Cups and Food Trays
• Clothing and Fabrics
• Nappies

But how does Household Waste affect the environment?

It affects the environment by contributing to the dangerous effects on animals and water contamination to name a few. Piles of trash have been left on beaches of discarded into the ocean affects 90% of aquatic species as they cannot distinguish what is edible and what is not edible. This results in death as aquatic animals are not able to process trash into their systems.

1. Effects on animals

Increasingly, improper household waste management practises and inadequate solid waste collection lead to several diseases and even the death of animals, particularly cows, birds, and stray dogs which feed among the trash while scavenging erratically. These wastes come in a variety of forms and contain hazardous substances. Cows and buffalos regularly consume plastics with their food, which causes the animals to die. The consumption of this meal has an impact on both the quantity and quality of animal milk products.

2. Water contamination

Poor management of beaches and improper disposal of household waste results in water contamination. As a result, the contamination and the wastes that have not been picked up after disposal will spread into different parts of the ocean. Moreover, the water will contain hazardous chemicals. This will also affect the agricultural part as crops will need fresh water. 

References: 
https://www.stateoftheenvironment.des.qld.gov.au/pollution/waste/household-waste-landfilled
https://www.cleanup.org.au/clean-up-our-waste

'''

Table(food_details,[title_1, wordings_1])
# Table(food_details,[items.table_schema[1],wordings_1])

title_2 = 'Retail Waste'
wordings_2='''
25,775 million tonnes of plastic and 26,000 million tonnes of paper have been dumped in landfills yearly by Australian shops. 2.4 million tonnes of plastic and 1.5 million tonnes of paper have been arising every year.

60% of retail wastes have been filled with plastic, paper, cardboard as those are the components that packs customer’s materials. All of these materials can be easily recycled.

If businesses can reuse and recycle these materials, this can help them to keep the environment as well as save money. 

There are some retail businesses that contain chemicals such as makeup stores and pharmacies. These can impact greenhouse gasses and environment such as:
• Water and energy used in production
• Natural Resource extraction
• Pollution
• Transportation
• Use of Product
• Disposal
• Waste management
• Chemicals

1. Energy

The environment may be severely impacted by how much energy businesses consume. They know how much energy will be used for electrical appliances and lights in stores, as well as indirect effects on how much gashouse gasses will be produced during the energy producing process. Switching from fluorescent to LED lighting can have a significant impact because lighting is one of the largest direct energy consumers.

2. Chemicals

Many retail products contain chemicals as a result of the production process. Yet, these substances typically pose little threat but poses a huge threat to animals and the environment especially hazardous chemicals. As the majority of retailers do not make the goods they sell, they must collaborate with producers and suppliers to ensure that all environmental requirements are met with regard to the chemicals used and emissions generated during production. Most of the goods they sell are environment friendly but even some are only harmless to humans, but poses are great harm to animals. 

3. Waste management

One aspect of waste management is the handling of solid waste. Solid waste is generally accumulated through the destruction of end-of-product trash, the disposal of shipment packing, and the use of shopping bags. In order to achieve zero waste, many retailers must recycle all solid waste 100 percent of the time.

References:
https://medium.com/retailcrc/top-5-environmental-sustainability-issues-in-retail-815aa0310779

'''
Table(food_details,[title_2, wordings_2])
# Table(food_details,[items.table_schema[1],wordings_2])

title_3 = 'Restaurant Waste'
wordings_3='''
Almost 150,529 tonnes of food waste could have been recovered by businesses in Australia. This includes keeping 291 million meals out of the trash. Food waste will often accumulate 60% of the rubbish bins in a café or restaurant, with the occasional paper and cardboard taking up the remaining 20%. That means that 80% of the rubbish bin’s contents could have been recycled or salvaged rather than thrown away.

80% of cafes and restaurants have agreed that reducing waste and increasing recycling are essential components of operating a sustainable and moral business.

1. Greenhouse gas emission

Methane, a gashouse gas which has the potential to cause global warming easily as this can be released from the decomposition of landfills from food being thrown out. 11% of the gas emissions can be reduced if we put them into food waste treatment systems instead of throwing them out into landfills. Methane has the ability to stay in the atmosphere for 12 years if food ends out breaking down, also being able to absorb the majority of the solar heat. Even if Methane contributes 20% to the gas emissions, it is still harmful. Food waste reduction results in a reduction in methane emissions into the atmosphere.

2. Meat production

13% of global gashouse gas emission and 11% of the gas emission in Australia have been produced by livestock. Yet not all livestock has the same effect on global warming.

Lamb, mutton and beef emits around 60 kg of global gashouse gas emissions compared to any other meat. By far, the highest source of global gashouse gas emission is beef. Actually, in Australia, it takes 526 litres to produce just 1 kg of beef fit for a restaurant.

References:
https://www.lightspeedhq.com.au/blog/restaurant-sustainability-practices/

'''
Table(food_details,[title_3, wordings_3])
# Table(food_details,[items.table_schema[1],wordings_3])

title_4 = 'Agricultural waste'
wordings_4='''
In 2017, 30 million tonnes of Agricultural waste has been generated in Australia in which 5 million tonnes of it were sent to landfills

Examples of agricultural waste include food, garden waste, wood, agricultural trash, and hazardous agricultural waste (i.e. sludge from grease traps and abattoir waste).

Agricultural waste in Australian landfills accounts for about 4% of the country's gashouse gas emissions.

Almost 76% of all agricultural waste, including food and garden waste, is sent to the landfill.

So how does Agricultural Waste contribute poorly to the economy?

1. Waste of Natural Resources

When restaurants waste food, they are wasting the resources that are used in producing the food. The main aspects of this are energy, fuel and water. 

Water is a natural process in food production as this includes irrigation and spraying of crops. Wasting food also means wasting fresh water that is used for producing the crop.  

In order to grow plants and animals, farmers tend to use a sizeable amount of fresh water. Fruits and vegetables, which have a high-water content, require a lot of water to maintain. Also another thing farmers need to keep, different plant species have different water needs. Water is also essential for the nourishment and growth of animals. Though, the food that is thrown out is a lot more dire. 

2. Degradation of Land

There are two ways as to how people waste land. That is the land for producing food and land that is used for dumping food. 

Most of Australian agricultural land area is 11 million hectares. Land can be divided into two categories: land that is able to support crop growth and land that cannot grow crops. Over 900 million hectares of land that cannot grow crops, cows are raised for the production of meat and dairy products. As the demand for meat increases, more land that is able to support crop growth is being converted into pastures for animals to graze. This means that the natural land (eg. Forests and open lands) are beginning to be chopped and mowed down, making it so that plants and animals that inhabit the land cannot survive there. 

These numbers show that farmers are using too much area for food production, and if farmers don't take precautions, the yield will gradually decrease as the soil deteriorates. By converting land that is able to support crop growth into pastures, farmers not only endanger the biodiversity that already exists in nature but also threaten to seriously disrupt the ecosystem's food chains. As a result, the loss of animal habitat that results from this conversion to pastures threatens to seriously disrupt the food chains of the ecosystem.

3. Harm to biodiversity

Biodiversity refers to the numerous species and other living things that make up an ecosystem.

Agriculture in general has a negative impact on our biodiversity. Converting wild lands into pastures and suitable agricultural terrains are common practises where there is an increase in the requirement for the production of animals. This destroys our environment unnecessarily.

Deforestation and converting lands that are inhabited by our ecosystems to be turned into land that are able to grow crops means obliterating the existing plants and animals, frequently to the point of extinction.

References:
https://www.energy.gov.au/households/reducing-waste#:~:text=In%202016%2D17%20around%206.7,than%20carbon%20dioxide%20(CO2)
https://earth.org/how-does-food-waste-affect-the-environment/
https://www.avristech.com/food-waste-impacts-on-environment/

'''
Table(food_details,[title_4, wordings_4])
# Table(food_details,[items.table_schema[1],wordings_4])

title_5 = 'Processing waste'
wordings_5 = '''
In 2021, Australia exported 4.36 million tonnes of waste and repurposed goods, as this totals roughly $3.1 billion. Even though the amount of exported goods is almost exactly the same as the previous year, the stated value is 10% higher. The 4.0 million tonnes of waste is reported to be in shipments. 

Despite a little increase in exports of abandoned plastic, the proportion of mixed plastics fell. In January, the raw exported waste has been banned in Australia, shipments of scrap glass dropped from a low level to almost none.

Over 1.2 million tonnes of exports were made in codes in 2021 that would be impacted by Australia's envisioned export limitations. This makes about 40% of all exports of trash and recovered materials.

1. Human impact

When you consider all the sicknesses and climate change that produced waste produces, it is easy to see how this affects everyone and animals. Eliminating any behaviours that increase waste would help save our economy while also conserving the ecosystem in the country. Improper waste management is a contributing cause to the environment's deterioration.

For many people, maintaining a commitment to effective waste management and trash reduction can be challenging. Some people even refuse to do it because they do not believe that processed waste is killing our ecosystem. Even if only a few individuals are impacted, any effort made to properly dispose of waste will aid in averting future catastrophes and suffering. Also, there are people who have done considerable adjustment, thereby resolving the issue. 

2. Air pollution

Given that air pollution is a major issue everywhere, it is crucial to comprehend how processed waste disposal affects the ecosystem through air pollution. A basic idea in air pollution holds that gashouse gases build up in the atmosphere and dramatically change the country’s climate. Therefore processed waste disposal contributes to the issue of too many gases entering the environment. Gases like methane, a major global contributor to climate change, are released when the waste decomposes.

3. Water pollution

The majority of rubbish that is not disposed of in landfills or other facilities ends up in the ocean or rivers. When the water decays into the ocean, it becomes contaminated and gradually loses its capacity to support life, slowly erasing our marine species life. By this process, the water becomes more poisonous, making it unsafe to swim in any body of water which renders freshwater unfit for human consumption. Pollutants can contaminate other water sources because water is a great solution and circulates, and therefore they are challenging to remove from the area.

References:
https://www.agriculture.gov.au/
https://www.dcceew.gov.au/environment/protection/waste/exports/plastic

'''
Table(food_details,[title_5, wordings_5])
# Table(food_details,[items.table_schema[1],wordings_5])

title_6 = 'Transportation and distribution waste'
wordings_6 = '''
Almost 80% of Australians who are 18 years of age and older typically used a private motor vehicle to get to work or to school in 2012, while 20% of people made use of public transit. Particularly Queensland had the greatest percentages of people using public transit with 20% of these people.

Approximately 8 million people who commuted by private motor car to their place of employment or full-time study do so often. The majority of Australian state capitals had residents who were willing to use the public transport. In almost 1.8 million people have claimed that their primary mode of mobility was their personal vehicals to and from work or full-time school. 

The absence of any service was one of the main reasons why people in Australia didn't use public transit. Other justifications included a preference for the comfort, convenience, and privacy of a private motor vehicle and the availability of a public transportation service at an appropriate or adequate time. 

1. Waste of fuel

To grow, transport, store, and prepare food, we use fossil fuels such as oil, diesel, and coal. For instance, fuel is extensively used by equipment that sorts, cleans, packages, or prepares food as well as equipment that moves food from the farm to the warehouse. Several of these pieces of machinery need fuels like oil, diesel, and other types. This will result in landfills always found outside of urban areas. Moreover, it is transported over great distances using trucks like garbage trucks that are driven by diesel. Gashouse gases that harm the environment are emitted into the atmosphere when these fuels are used. As food waste wastes fuel or oil both up front and at the back end, it has a considerable negative impact on the environment.

2. Greenhouse gas emissions

Methane and nitrous oxide are slightly more common in transportation emissions than carbon dioxide. Compared to other gases, nitrous oxide emissions have increased rather slowly, from 3.7% of transportation emissions in late 1990s to 5.0% in early 2000s. The increase in the number of automobiles with catalytic converters can be used to explain this. Three-way catalytic converters reduce emissions as compared to vehicles with two-way converters or those without pollution control systems, but they also emit 10% more methane and almost 120% more nitrous oxide per kilometre.

Since transportation uses a lot of energy and burns the majority of the country’s diesel, it has a significant influence on the environment. Carbon dioxide generation results in air pollution, including nitrous oxides and particulates, which considerably accelerates global warming.

References:
https://www.abs.gov.au/ausstats/abs@.nsf/Previousproducts/1301.0Feature%20Article312003?opendocument&tabname=Summary&prodno=1301.0&issue=2003&num=&view=
'''
Table(food_details,[title_6, wordings_6])
# Table(food_details,[items.table_schema[1],wordings_6])