from TornAPIWrapper import TornAPIWrapper

torn = TornAPIWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = torn.faction.get_search(filters=["respectLessOrEqual20000", "membersGreater10"], limit=5) #Get Torn City faction data.

print(data)