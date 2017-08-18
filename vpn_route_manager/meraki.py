import requests, json

class Meraki(object):
    ## Settable object parameters
    def __init__(self, apikey, networkid, apiurl="https://dashboard.meraki.com/api/v0"):
        self.apikey = apikey
        self.apiurl = apiurl
        self.networkid = networkid
        self.headers = {'Content-type': 'application/json', 'X-Cisco-Meraki-API-Key': apikey}

    # Method 'getroutes'
    def getroutes(self):
        apikey = self.apikey
        apiurl = self.apiurl
        networkid = self.networkid

        ## get static routes from API
        try:
            apicall = requests.get('{0}/networks/{1}/staticRoutes'.format(apiurl, networkid), headers=self.headers)
            apicall.raise_for_status()
            # The below call returns a List of Dictionaries...
            ## eg: [{"rule": "1", "subnet": "10.0.0.0/8"}, {"rule": 2, "subnet": "127.0.0.1/32"}, {...} ]
            ## Will need to iterate through the list to process each KV; We want:
            #   * Ignore any routes not starting with "VPNMan-" (so we don't cause issues with other routes from other sources)
            #   * To document the sR ID incase we want to delete it later
            #   * Document the Subnet
            routesjson = apicall.json()
        except requests.exceptions.HTTPError as e:
            print("API Request for GET staticRoutes failed with Error: ")
            print(str(e))
            return False

        # Convert JSON to Pythonic List of Lists.
        return routesjson

#    # Method 'addroute'
#    def addroute(self, route):
#        ## Add a missing route to the static routes list
#        return result

#    # Method 'delroute'
#    def delroute(self, route):
