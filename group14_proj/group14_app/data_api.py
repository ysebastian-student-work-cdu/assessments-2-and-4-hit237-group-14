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
wordings_1 = '''
Every year, Australians generate 540 kilogrammes of domestic garbage per person. Each person would have to lose more than 10 kg each week. Only 37 of the 67 million tonnes of rubbish that Australians produced in 2017 were recycled, leaving 21.7 to be dumped in landfills. Over 130,000 tonnes of Australian plastic have been entering the ocean annually, causing contamination and affecting economic species.

Domestic waste was thrown in landfills at a rate of 1.77 million tonnes per year in 2007. This includes the typical 1.23 million tonnes collected through kerbside bin services.

Household garbage delivery to landfills increased by 4% during the previous three years compared to the long-term average.

So what are the examples of Household Waste?

• Plastic Bags and Bin Liners
• Foam Cups and Food Trays
• Clothing and Fabrics
• Nappies

But how does Household Waste affect the environment?

It affects the environment by contributing to climate change, air pollution and water contamination. Piles of trash that are thrown into the ocean affects almost all the species as they cannot distinguish between what is edible and what is not edible. This results in death as aquatic animals are not able to process trash into their systems.

1. Effects on animals

Increasingly, improper waste management practises and inadequate solid waste collection lead to several diseases and even the death of animals, particularly cows, birds, and stray dogs which feed among the trash while scavenging erratically. These wastes come in a variety of forms and contain hazardous substances. Cows and buffalos regularly consume plastics with their food, which causes the animals to die. The consumption of this meal has an impact on both the quantity and quality of animal milk products.

2. Water contamination

Poor management and improper disposal of household waste results in environmental contamination. The water bodies are impacted. Moreover, it modifies the biological, chemical, and physical properties of water bodies. Trash that hasn't been picked up is dispersed throughout the ecosystem, where it seeps into the ground and gets carried by runoff to aquatic areas. The poisonous nature of the garbage contaminates the water. Moreover, it reduces agricultural output and renders the soil sterile.
'''

Table(food_details,[items.table_schema[1],wordings_1])

wordings_2='''
A further 31,665 tonnes of plastic and 35,937 tonnes of paper may be recycled yearly by NSW shops. 2.3 million shopping carts full of plastic and 1.5 million carts full of paper would arise from this each year.
Packing materials including paper, cardboard, and plastic make up over 60% of the trash at a typical retail store.

All of these materials can be easily recycled.

By avoiding, minimising, reusing, and recycling packaging materials, businesses are able to save money and keep the environment clean.

There are some retail businesses that contain chemicals such as makeup stores and pharmacies. These can impact greenhouse gasses and environment such as:
• Water and energy used in production
• Natural Resource extraction
• Pollution
• Transportation
• Use of Product
• Disposal
•Waste management

1. Energy

The environment may be severely impacted by how much energy businesses consume. They have direct effects on how much energy is used, as well as indirect affects on how the glasshouse gases produced during the energy producing process. Switching from fluorescent to LED lighting can have a significant impact because lighting is one of the largest direct energy consumers.

2. Chemicals

Many retail products contain chemicals as a result of the production process. Yet, these substances typically pose little threat. As the majority of retailers do not make the goods they sell, they must collaborate with producers and suppliers to ensure that all environmental requirements are met with regard to the chemicals used and emissions generated during production.

3. Waste management

One aspect of waste management is the handling of solid waste. Solid waste is generated through the destruction of end-of-product trash, the disposal of shipment packing, and the use of shopping bags. In order to achieve zero waste, many retailers must recycle all solid waste 100 percent of the time.
'''
Table(food_details,[items.table_schema[1],wordings_2])

wordings_3='''
A further 140,529 tonnes of food waste could be recovered by businesses in NSW, or 281 million meals could be kept out of the trash. Food waste often occupies more than 60% of the garbage can in a café or restaurant, with paper and cardboard taking up the remaining 18%. That means that somewhere between 80% and 90% of the garbage can's contents could be recycled or salvaged rather than thrown away.

75% of cafes, restaurants, and lodging facilities agree that reducing waste and increasing recycling are essential components of operating a sustainable and moral business.

1. Greenhouse gas emission

Throwing out food causes it to decompose in landfills, where it releases methane, a glasshouse gas with a 28-times greater potential to cause global warming than carbon dioxide. If we shift food waste from landfills and into an innovative food waste treatment system, we can reduce glasshouse gas emissions by about 11%. Methane is released as food waste breaks down, and it stays in the atmosphere for 12 years, absorbing the majority of solar heat. Despite having a short lifespan, methane contributes 20% of glasshouse gas emissions.

Food waste reduction results in a reduction in methane emissions into the atmosphere.

2. Meat production

13–18% of the global glasshouse gas (GHG) emissions and 11% of the GHG emissions in Australia are produced by livestock agriculture. Yet not all livestock has the same effect on global warming.

Lamb and beef are the meats that emit the most emissions. However compared to the next-closest food types, lamb and mutton, beef produces 60 kg (or nearly 2.5 times as much) GHG emissions per kilogramme (kg). By far, the highest source of GHGs is beef. Actually, in Australia, it takes 515 litres to produce just 1 kg of beef fit for a restaurant.
'''
Table(food_details,[items.table_schema[1],wordings_3])

wordings_4='''
In 2016–17, over 30 million tonnes of organic waste were generated in Australia, of which 6.7 million tonnes were sent to landfills.

Examples of organic waste include food, garden waste, wood, agricultural trash, and hazardous organic waste (i.e. sludge from grease traps and abattoir waste).

Organic garbage in Australian landfills accounts for about 3% of the country's glasshouse gas emissions.

Almost 75% of all organic garbage, including food and garden waste, is sent to the landfill.

So how does Agricultural Waste contribute poorly to the economy?

1. Waste of Natural Resources

When restaurants waste food, they are wasting the resources that are used in producing the food. The main aspects of this are energy, fuel and water.

Water is a natural process in food production as this includes irrigation and spraying of crops. Wasting food also means wasting fresh water that is used for producing the crop.

With the growth of plants and animals, a sizable amount of fresh water is lost. Fruits and vegetables, which have a high water content, require a lot of water to flourish. Also, different plant species have different water needs. Water is also essential for the nourishment and growth of animals. Despite the fact that growing meat uses more water, it is the food that is thrown out the most.

2. Degradation of Land

There are two ways as to how people waste land. That is the land for producing food and land that is used for dumping food.

The world's agricultural land area is 11.5 million hectares. Land can be divided into two categories: land that is able to support crop growth and land that cannot grow crops. Over 900 million hectares of land that cannot grow crops, cattle are raised for the production of meat and dairy products. As the demand for meat increases, more land that is able to support crop growth is being converted into pastures for animals to graze. This causes our natural land to gradually deteriorate, making it difficult for anything natural to survive there.

These numbers show that farmers are using too much area for food production, and if farmers don't take precautions, the yield will gradually decrease as the soil deteriorates. By converting land that is able to support crop growth into pastures, farmers not only endanger the biodiversity that already exists in nature but also threaten to seriously disrupt the ecosystem's food chains. As a result, the loss of animal habitat that results from this conversion to pastures threatens to seriously disrupt the food chains of the ecosystem.

3. Harm to biodiversity

The term "biodiversity" refers to the numerous species and other living things that make up an ecosystem.

Agriculture in general has a negative impact on our biodiversity. Converting wild lands into pastures and suitable agricultural terrains are common practises where there is an increase in the requirement for the production of animals.

Deforestation and converting lands that are inhabited by our ecosystems to be turned into land that are able to grow crops means obliterating the existing plants and animals, frequently to the point of extinction.

'''
Table(food_details,[items.table_schema[1],wordings_4])

wordings_5 = '''
In 2020–21, Australia exported 4.25 million tonnes (Mt) of waste and repurposed goods, totalling $3.2 billion. Even though the tonnage is almost exactly the same as the previous year, the stated value is 12% higher. The 3.9 Mt (91%) of "core waste plus ash" covered by national waste reporting was present in the shipments.

Despite a little increase in exports of abandoned plastic, the proportion of mixed plastics fell. As Australia's export ban on raw glass went into effect in January, shipments of scrap glass dropped from a low level to almost none.

Over 1.3 Mt of exports were made in codes in 2020–2021 that would be impacted by Australia's envisioned export limitations. This makes about 30% of all exports of trash and recovered materials.

1. Human impact

When you consider all the sicknesses and climate change that improper waste processing produces, it is easy to see how this affects everyone. Eliminating any behaviours that increase waste would help save many lives while also conserving the ecosystem globally. Improper waste management is a contributing cause to the environment's deterioration.

For many people, maintaining a commitment to effective waste management and trash reduction can be challenging. Even some people think there is no point because it is already too late. Even if only a few individuals are impacted, any effort made to properly dispose of waste will aid in averting future catastrophes and suffering. Also, it suggests that a considerable adjustment may be done, thereby resolving the issue

2. Air pollution

Given that air pollution is a major issue everywhere, it is crucial to comprehend how improper garbage disposal affects the ecosystem through air pollution. A basic idea in air pollution holds that glasshouse gases build up in the atmosphere and dramatically change the planet's climate. Improper waste disposal contributes to the issue of too many gases entering the environment. Gases like methane, a major global contributor to climate change, are released when the waste decomposes.

3. Water pollution

The majority of rubbish that is not disposed of in landfills or other facilities ends up in the ocean or another body of water. When the water decays into the ocean, it becomes contaminated and gradually loses its capacity to support life. By this process, the water becomes more poisonous, making it unsafe to swim in any body of water and rendering freshwater unfit for human consumption. Pollutants can contaminate other water sources because water is a great solution and circulates, and therefore they are challenging to remove from the area.
'''
Table(food_details,[items.table_schema[1],wordings_5])


wordings_6 = '''
78% of Australians who were 18 years of age and older typically used a private motor vehicle to get to work or full-time school in March 2012, while 16% made use of public transit. New South Wales and Queensland had the greatest percentages of people using public transit, with 21% and 17%, respectively.

Twenty-three percent of the eight million people who commuted by private motor car to their place of employment or full-time study do so often. The majority of Australian state capitals except Hobart (37%) had residents who were willing to receive travellers. In almost 1.7 million cases, persons claimed that their primary mode of mobility was to and from work or full-time school.

Over 69% of those surveyed claimed that this was the case because it was practical, cosy, and relaxed them.

The absence of any service (30%) was one of the main reasons why people in Australia didn't use public transit. Other justifications included a preference for the comfort, convenience, and privacy of a private motor vehicle (26%) and the availability of a public transportation service at an appropriate or adequate time (23%).

1. Waste of fuel

To grow, transport, store, and prepare food, we use fossil fuels such as oil, diesel, and coal. For instance, fuel is extensively used by equipment that sorts, cleans, packages, or prepares food as well as equipment that moves food from the farm to the warehouse. Several of these pieces of machinery need fuels like oil, diesel, and other types. Moreover, landfills are always found outside of urban areas. As a result, it is transported over great distances using trucks like garbage trucks that are driven by petroleum or diesel. Glasshouse gases that harm the environment are emitted into the atmosphere when these fuels are used. As food waste wastes fuel or oil both up front and at the back end, it has a considerable negative impact on the environment.

2. Greenhouse gas emissions

Methane and nitrous oxide are slightly more common in transportation emissions than carbon dioxide. Compared to other gases, nitrous oxide emissions have increased by a factor of two, from 2.7% of transportation emissions in 1990 to 5.4% in 2000. The increase in the number of automobiles with catalytic converters and other pollution-reduction devices can be used to explain this. Three-way catalytic converters reduce emissions as compared to vehicles with two-way converters or those without pollution control systems, but they also emit 12% more methane and 154% more nitrous oxide per kilometre.

Since transportation uses a lot of energy and burns the majority of the world's petroleum, it has a significant influence on the environment. Carbon dioxide generation results in air pollution, including nitrous oxides and particulates, which considerably accelerates global warming.
'''
Table(food_details,[items.table_schema[1],wordings_6])