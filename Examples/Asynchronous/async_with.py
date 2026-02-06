import asyncio
from TornAPIWrapper import TornAPIWrapperAsync

async def main():
    async with TornAPIWrapperAsync(api_key="1aBcDeFgH2iJkLmN") as torn:  #Insert your API key.
        data = await torn.user.get_profile(user_id=2561334)  #Get Torn City user profile data.
        print(data)

if __name__ == "__main__":
    asyncio.run(main())