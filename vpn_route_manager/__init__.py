# import iplookup
import iplookup

# Local modules
import meraki, taskRunner

# Load my local secrets for apikey + networkid until I get the config files sorted.
import secrets
apikey = secrets.get_apikey()
networkid = secrets.get_networkid()

# Create a Meraki API Object instance
api = meraki.Meraki(apikey, networkid)

# Call the Meraki Object's getroutes method to get the routes (List of Dictionaries)
routes = api.getroutes()
if routes == False:
    print("The API Call to Meraki returned a non-OK Error")
    sys.exit(1)

# Strip list to routes which start with 'keyword' in their names (allows us to only handle our own routes without touching others)
keyword = "IPT"
route_list = [ route for route in routes if route["name"].startswith("IPT")]
print(str(route_list))

# Filter this list to only the IP (strip CIDR)
subnets = []
for dict in route_list:
    subnets.append(dict.get('subnet').split('/')[0])

print(subnets)

# For each IP from DomainsList, ensure route on localhost via VPN GW -- method YTBD
## Once we have polled the domainslist the first time, schedule a periodic re-check

# For each IP from DomainsList; find missing from MerakiList, and add.
# For each IP in MerakiList missing from DomainList, Delete it



# Code layout should be:
- Imports
- API Endpoints for Flask
- Initialise vars as __main__ (Read from config?)
- Next; poll Domains list, and run initial on-load comparisons and settings
- When initial run complete, start Periodic
#rt = taskRunner.Periodic(300, pollDomains)
- Start Flask Server