# Save_the_air with the Ardurino-Navigation-Service

Safe_the_air is a project to provide cities of polution through particulate matter. 
When getting in the car and activating the Ardurino-Naviagation-Service we built, the car will automatically provide a traveling path that avoids overpolluted areas. 
This way, these areas can depollute and get a rest. 

The navigation service works like this:
Ardurino connects to the web and downloads the current pollution map from. 
Based on that map, areas with high pollution are avoided if possible and an environmental friendly route is suggested. 
First the shortest path is created, then it is optimized in the 

The Demo Case:
7 am mid London a person wants to go to work. Currently the city center district is polluted to strongly. Thus the car is routed around that area and 
the alternativ path is chosen.

What still needs to be done for the Ardurino-Naviagation-Service to work autonomiousely, but hasn't as the material does not provide this: 
- storage: storing the map and code inside Ardurino. - No SD-Card
- moving calculation: The claculation of the map should be run on the Ardurino without need of a computer. - No SD-Card as well
- connecting to WIFI: then the map can be downloaded to the device without a computer. - No Wifi-Module.