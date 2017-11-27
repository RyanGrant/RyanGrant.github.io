#All of these imports used, if the code is broken down into several sections like it is on the wiki,
#might not make sense to include all of them at the beginning, but will save time for new devs

import requests, zipfile, os, pickle, json, sqlite3

def build_dict():
    print('Connecting to sqlite db thing')
    con = sqlite3.connect('manifest.content')
    cur = con.cursor()

    all_data = {}
    cur.execute('SELECT json from DestinyInventoryItemDefinition')

    items = cur.fetchall()

    item_jsons = [json.loads(item[0]) for item in items]

    item_dict = {}
    #'displayProperties'
    #'screenshot'
    #'itemTypeDisplayName'
    #'itemTypeAndTierDisplayName'
    
    for item in item_jsons:
        if ( item['displayProperties']['name'] != "Classified" ):
            if ( item['itemTypeDisplayName'] != None):
                if ( item['itemTypeAndTierDisplayName'] ):
                    if ( "Exotic" in item['itemTypeAndTierDisplayName'] and "Intrinsic" not in item['itemTypeAndTierDisplayName']):
                        if ( item['displayProperties']['name'] ):
                            item_dict[item['displayProperties']['name']] = item['displayProperties']
                            item_dict[item['displayProperties']['name']]['type'] = item['itemTypeDisplayName']
                            item_dict[item['displayProperties']['name']]['tier'] = item['itemTypeAndTierDisplayName']
                            item_dict[item['displayProperties']['name']]['image'] = "http://www.bungie.net" + item['displayProperties']['icon']
                            item_dict[item['displayProperties']['name']]['active'] = "false"
                            try:
                                item_dict[item['displayProperties']['name']]['class'] = item['quality']['infusionCategoryName']
                            except:
                                item_dict[item['displayProperties']['name']]['class'] = "null"

    #add that dictionary to our all_data using the name of the table
    #as a key.
    #all_data[table_name] = item_dict

    print('Dictionary Generated!')
    return item_dict


print("Starting...")
all_data = build_dict()
with open('manifest.pickle', 'wb') as data:
    pickle.dump(all_data, data)
    print("'manifest.pickle' created!\nDONE!")

#with open('manifest.pickle', 'rb') as data:
#    all_data = pickle.load(data)

print(len(all_data))
#print(all_data['Coldheart']['tier'])
#print("Exotic" in all_data['Coldheart']['tier'])
#print(not all_data['Raven Shard']['tier'])
weapons = []
armor = []
warlock = []
hunter = []
titan = []
types = []
weapon_ornaments = []
ships = []
emotes = []
vehicles = []
traits = []
for item in list(all_data):
    del(all_data[item]['icon'])
    del(all_data[item]['hasIcon'])

    if (all_data[item]['type'] == "Weapon Ornament"):
        weapon_ornaments.append(all_data[item])
    elif (all_data[item]['type'] == "Ship"):
        ships.append(all_data[item])
    elif (all_data[item]['type'] == "Emote"):
        emotes.append(all_data[item])
    elif (all_data[item]['type'] == "Vehicle"):
        vehicles.append(all_data[item])
    elif (all_data[item]['type'] == "Trait"):
        traits.append(all_data[item])
    elif (all_data[item]['type'] == "Helmet"):
        armor.append(all_data[item])
    elif (all_data[item]['type'] == "Chest Armor"):
        armor.append(all_data[item])
    elif (all_data[item]['type'] == "Leg Armor"):
        armor.append(all_data[item])
    elif (all_data[item]['type'] == "Gauntlets"):
        armor.append(all_data[item])
    elif (all_data[item]['type'] == "Engram"):
        del(all_data[item])
    else:
        weapons.append(all_data[item])

for piece in armor:
    if ("warlock" in piece['class']):
        warlock.append(piece)
    elif ("titan" in piece['class']):
        titan.append(piece)
    elif ("hunter" in piece['class']):
        hunter.append(piece)
    else:
        print(piece)
        
print(warlock)
print(len(all_data))
#print(all_data["Rat King"])
#from collections import Counter
#print(Counter(types))
