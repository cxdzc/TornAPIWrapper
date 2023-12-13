from TornAPIWrapper import TornApiWrapper

taw = TornApiWrapper(api_key="1aBcDeFgH2iJkLmN") #Insert your API key

data = taw.get_company(77455, selections=["lookup"]) #Get Torn City company data.

print(data["selections"])