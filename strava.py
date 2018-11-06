from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AthletesApi()
id = 56 # Integer | The identifier of the athlete. Must match the authenticated athlete.
page = 56 # Integer | Page number. (optional)
perPage = 56 # Integer | Number of items per page. Defaults to 30. (optional) (default to 30)

try: 
    # Get Athlete Stats
    api_response = api_instance.getStats(id, page=page, perPage=perPage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->getStats: %s\n" % e)
