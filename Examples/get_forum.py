from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = torn.forum.get_threads(category_ids=[54, 63]) #Get Torn City thread data.

print(data)