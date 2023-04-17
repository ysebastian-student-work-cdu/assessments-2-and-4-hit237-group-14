class Item:
    
    items=[]
    
    def __init__(self,item):
        Item.items.append(item)
        
    def show_records():
        return Item.items
    
item_1 = Item({'type': 'Household waste',
            'description': 'This is the food waste that occurs in our homes, including food that is left uneaten on plates, expired or spoiled food, and food that is thrown away because it is no longer wanted.',
            'id': '1'})
item_2 = Item({
            'type': 'Retail waste',
            'description': 'This includes food that is thrown away by supermarkets, grocery stores, and other food retailers due to overstocking, expiration, or damage.',
            'id': '2'
        })
item_3 = Item( {
            'type': 'Restaurant waste',
            'description': 'This is the food waste that occurs in restaurants, cafes, and other food service establishments, including food that is left uneaten by customers, overproduction, and spoilage.',
            'id': '3'
        })
item_4 = Item(   {
            'type': 'Agricultural waste',
            'description': 'This includes food that is lost during the production and harvesting of crops, such as fruits and vegetables that are left in the field due to overproduction or damage.',
            'id': '4'
        })
item_5 = Item(  {
            'type': 'Processing waste',
            'description': 'This is the food waste that occurs during the processing and manufacturing of food products, including scraps, trimmings, and packaging waste.',
            'id': '5'
        })
item_6 = Item( {
            'type': 'Transportation and distribution waste',
            'description': 'This includes food that is lost during transportation and distribution, such as spoilage and damage during transit.',
            'id': '6'
        })