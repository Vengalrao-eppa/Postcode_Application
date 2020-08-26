# Postcode_Application

Build a Django application to help our franchise acquisition team understand the value of postcode districts in Greater Manchester. 
A postcode district (also known as an outcode) is the first part of the postcode e.g. M11. 
Build an api that exposes following endpoints:

GET /api/outcode/{outcode}
Return the following XML data structure: 
<outcode
listing-count="{{ number of listings within outcode }}" 
average-daily-rate="{{ average daily rate of all listings within outcode }}" 
>{{ outcode }}</outcode>

If no data is available, return an empty 404 response.

GET /api/nexus/{outcode}

Returns a list of neighbouring postcode districts (outcodes) for the given nexus outcode. NB you should include the nexus outcode within the list.

Use the following data structure: 

<outcodes
nexus="{{ nexus outcode }}"
listing-count="{{ sum of listings }}"
average-daily-rate="{{ average daily rate across all listings }}"> <!-- repeat for each neighbouring outcode -->
<outcode 
listing-count="{{number of listings within outcode}} “ average-daily-rate="{{ average daily rate of all listings within outcode }}" distance=”{{ distance from nexus }}” 
>{{ outcode }}</outcode> </outcodes> 


If no data is available, return an empty 404 response. 


Notes 
Use the dataset available here for airbnb listing data: http://insideairbnb.com/get-the-data.html 
Use the api available here for postcode lookups: http://postcodes.io
Write the code as-if for production - showcase anything you think is relevant. 
