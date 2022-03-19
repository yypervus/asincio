import sqlalchemy
import aiohttp
import asyncio


async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
    return data


async def get_count():
    data = await make_request('https://swapi.dev/api/people')
    return data['count']


async def get_character(id):
    data = await make_request(f'https://swapi.dev/api/people/{id}')
    [data.pop(key, None) for key in ["created", "edited", "url"]]
    data['id'] = id
    list_key = ['films', 'species', 'starships', 'vehicles']
    for key in list_key:
        if key in data:
            data[key] = (",".join(data[key]))
    return data


engine = sqlalchemy.create_engine(f'sqlite:///asincbd.db')
connection = engine.connect()

async def save_database(profile_character):
    connection.execute('''INSERT INTO stat_character(id, birth_year, eye_color, films, gender, hair_color, height, homeworld, mass, name, skin_color, species, starships, vehicles) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (profile_character["id"], profile_character["birth_year"], profile_character["eye_color"], profile_character["films"], profile_character["gender"], profile_character["hair_color"], profile_character["height"], profile_character["homeworld"], profile_character["mass"], profile_character["name"], profile_character["skin_color"], profile_character["species"], profile_character["starships"], profile_character["vehicles"]))


async def main():
    count = await get_count()
    character_tasks = [asyncio.create_task(get_character(id_character)) for id_character in range(1, count+1)]
    characters = await asyncio.gather(*character_tasks)
    save_character_tasks = [asyncio.create_task(save_database(character)) for character in characters if 'name' in character]
    await asyncio.gather(*save_character_tasks)


asyncio.run(main())
