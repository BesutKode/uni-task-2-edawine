# Repo explanation

This task is designed to teach us how to extract data from existing open data sources.

Steps that I use:

1. Find a suitable island that is:
    
    a. is not a relation object in OpenStreetMap,
    
    b. is not connected to Wikimedia,
    
    c. is more than 10 kms in length, or is 10 kms away from another island,
    
    d. has more than 1,000 residents

    in http://www.openstreetmap.org.

2. Find the datasets needed in https://overpass-turbo.eu/ using queries you can find in query folder. The query is generated using the wizard button, then typing the data you want in your map (example: 'peak in "Pulau Kisar'). For the node and way, I follow the guide in https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide.
    
    After the query has been generated, click on the run button. To save the result in geojson, click on the export button, and then click on 'as geojson'.

3. Visualizing the data into a map using folium module (https://github.com/python-visualization/folium).

    I have created a example script ('map.py') that takes all the data in data folder to generate a html page ('index.html'). After the page has been generated, you can open the map in a browser without having to run the script again. In the map, you can select the data to be shown on the map or not in the upper right corner, then tick/untick the data.

If you would like to try the script, first do `pip3 install folium`, then run the script `python3 map.py`
