from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = torn.racing.get_cars() #Get Torn City car data.

print(data)