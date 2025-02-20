#Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.
'''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
'''
import json 
data = json.load(open('sample-data.json', 'r'))
print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
i = data[["imdata"][0]["11PhysIf"]["attributes"]["dn"]]
for i in range(len(data["imdata"])):
    dn = data["imdata"][i]["11PhysIf"]["attributes"]["dn"]
    speed = data["imdata"][i]["11PhysIf"]["attributes"]["speed"]
    mtu = data["imdata"][i]["11PhysIf"]["attributes"]["mtu"]
    print(f'{f"{dn}":<72}{f"{speed}":<11}{f"{mtu}":<10}')