import requests, zipfile, os, json, sqlite3

def get_manifest():

    manifest_url = 'http://www.bungie.net/Platform/Destiny2/Manifest/'
    print("Downloading Manifest from http://www.bungie.net/Platform/Destiny2/Manifest/...")
    r = requests.get(manifest_url)
    manifest = r.json()
    mani_url = 'http://www.bungie.net'+manifest['Response']['mobileWorldContentPaths']['en']

    #Download the file, write it to 'MANZIP'
    r = requests.get(mani_url)
    with open("MANZIP", "wb") as zip:
        zip.write(r.content)
    print("Download Complete!")

    print("Unzipping contents...")
    #Extract the file contents, rename the extracted file to 'Manifest.content'
    with zipfile.ZipFile('MANZIP') as zip:
        name = zip.namelist()
        zip.extractall()
    os.rename(name[0], 'Manifest.content')
    os.remove('MANZIP')
    print('Unzipped!')

def build_dict():
    con = sqlite3.connect('manifest.content')
    print('Connected to sqlite db')
    cur = con.cursor()

    cur.execute('SELECT json from DestinyInventoryItemDefinition')
    print('Generating DestinyInventoryItemDefinition dictionary....')

    items = cur.fetchall()
    item_jsons = [json.loads(item[0]) for item in items]
    item_dict = {}

    for item in item_jsons:
       if ( item['displayProperties']['name'] != "Classified" ):
           if ( item['itemTypeDisplayName'] != None):
               if ( item['itemTypeAndTierDisplayName'] ):
                   if ( "Exotic" in item['itemTypeAndTierDisplayName'] and "Intrinsic" not in item['itemTypeAndTierDisplayName']):
                       if ( item['displayProperties']['name'] ):
                           item_dict[item['displayProperties']['name']] = item['displayProperties']
                           item_dict[item['displayProperties']['name']]['type'] = item['itemTypeDisplayName']
                           item_dict[item['displayProperties']['name']]['tier'] = item['itemTypeAndTierDisplayName']
                           item_dict[item['displayProperties']['name']]['image'] = "https://www.bungie.net" + item['displayProperties']['icon']
                           item_dict[item['displayProperties']['name']]['active'] = "false"
                           try:
                               item_dict[item['displayProperties']['name']]['class'] = item['quality']['infusionCategoryName']
                           except:
                               item_dict[item['displayProperties']['name']]['class'] = "null"

    print('Dictionary Generated!')

    return item_dict

def saveToJs(data):
    weapons = []
    armor = []
    warlock = []
    hunter = []
    titan = []
    weapon_ornaments = []
    ships = []
    emotes = []
    vehicles = []
    for item in list(data):
        del(data[item]['icon'])
        del(data[item]['hasIcon'])

        if (data[item]['type'] == "Weapon Ornament"):
            weapon_ornaments.append(data[item])
        elif (data[item]['type'] == "Ship"):
            ships.append(data[item])
        elif (data[item]['type'] == "Emote"):
            emotes.append(data[item])
        elif (data[item]['type'] == "Vehicle"):
            vehicles.append(data[item])
        elif (data[item]['type'] == "Trait"):
            del(data[item])
        elif (data[item]['type'] == "Helmet"):
            armor.append(data[item])
        elif (data[item]['type'] == "Chest Armor"):
            armor.append(data[item])
        elif (data[item]['type'] == "Leg Armor"):
            armor.append(data[item])
        elif (data[item]['type'] == "Gauntlets"):
            armor.append(data[item])
        elif (data[item]['type'] == "Engram"):
            del(data[item])
        else:
            weapons.append(data[item])
        
        
    for piece in armor:
        if ("warlock" in piece['class']):
            warlock.append(piece)
        elif ("titan" in piece['class']):
            titan.append(piece)
        elif ("hunter" in piece['class']):
            hunter.append(piece)
        else:
            print("This armor piece has an issue", end="")
            print(piece)
            
    with open("ExampleData.js", "w") as text_file:
        print("\nvar exoticHunterArmorList = ", file=text_file, end="")
        print(hunter, file=text_file)
        print("\nvar exoticTitanArmorList = ", file=text_file, end="")
        print(titan, file=text_file)
        print("\nvar exoticWarlockArmorList = ", file=text_file, end="")
        print(warlock, file=text_file)
        print("\nvar exoticWeaponList = ", file=text_file, end="")
        print(weapons, file=text_file)
        print("\nvar exoticVehicleList = ", file=text_file, end="")
        print(vehicles, file=text_file)
        print("\nvar exoticShipList = ", file=text_file, end="")
        print(ships, file=text_file)
        print("\nvar exoticEmoteList = ", file=text_file, end="")
        print(emotes, file=text_file)
    #print(len(data))
    #print(data["Rat King"])
    #from collections import Counter
print("Starting...")

if (os.path.isfile('ExampleData.js')):
    print("Found existing data, overwriting...")
    os.remove('ExampleData.js')
get_manifest()
all_data = build_dict()
os.remove('Manifest.content')
print("Formatting and saving to JavaScript file...")
saveToJs(all_data)
print("Done")

#print(len(all_data))
#print(all_data['Coldheart']['tier'])
#print("Exotic" in all_data['Coldheart']['tier'])
#print(not all_data['Raven Shard']['tier'])

