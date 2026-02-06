import asyncio
from TornAPIWrapper import TornAPIWrapperAsync

async def main():
    torn = TornAPIWrapperAsync(api_key="1aBcDeFgH2iJkLmN")  #Insert your API key.
    data = await torn.user.get_profile(user_id=2561334)  #Get Torn City user profile data.
    print(data)
    await torn.close()

if __name__ == "__main__":
    asyncio.run(main())