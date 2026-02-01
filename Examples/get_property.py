from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = torn.property.get_property(property_id=609) #Get Torn City property data.

print(data)