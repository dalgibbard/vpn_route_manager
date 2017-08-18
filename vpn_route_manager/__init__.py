# import iplookup
import iplookup

# Local modules
import meraki

# Load my local secrets for apikey + networkid until I get the config files sorted.
import secrets
apikey = secrets.get_apikey()
networkid = secrets.get_networkid()

# Create a Meraki API Object instance
api = meraki.Meraki(apikey, networkid)

# Call the Meraki Object's getroutes method to get the routes
routes = api.getroutes()

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

# For each IP from DomainsList; find missing from MerakiList, and add.
# For each IP in MerakiList missing from DomainList, Delete it
