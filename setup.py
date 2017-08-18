from distutils.core import setup
version = "1.0.0"
setup(
    name = 'vpn_route_manager',
    packages = ['vpn_route_manager'], # this must be the same as the name above
    version = version,
    download_url = 'https://github.com/dalgibbard/vpn_route_manager/archive/{}.tar.gz'.format(version),
    description = 'Module for looking up IPs from Domain Names',
    long_description='''
VPN Route Manager
========
A bespoke utility to manage routes locally on a server, to route via VPN, and additionally configure
a Meraki security device (via Meraki API) to forward these routes to the local server for routing through
the VPN

Desired Behaviour:
* Allow for configuring a list of Domains via a simple WebUI
* Convert the domain list to IPs
* Compare this list of IPs to routes currently configured on the host, and on the Meraki MX
* Add/Delete routes as required to satisfy the routing of configured domains
* Interval-based polling, and/or action based triggering of a re-check of routes. 

''',
  author = 'Darren Gibbard',
  author_email = 'dalgibbard@gmail.com',
  url = 'https://github.com/dalgibbard/vpn_route_manager', # use the URL to the github repo
  keywords = "vpn routing meraki api flask", # arbitrary keywords
  install_requires = [
      "flask",
      "iplookup"
  ],
  classifiers = [
    'Development Status :: 3 - Alpha',
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
  ],
  license='BSD',
)
