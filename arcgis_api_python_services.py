#!/usr/bin/env python
# coding: utf-8

"""
ArcGIS Server Service Management Script

This script is designed to start or stop ArcGIS server services as part of the "State Zero" script.
It can be scheduled to run at predefined intervals.

Author: Michael Preko Nkum
"""

# Import required modules
from arcgis.gis import GIS
import arcgis.gis.admin

# Establish a connection to the ArcGIS server
# Replace empty strings with actual values: GIS(server_url, username, password)
gis = GIS("", "", "")

# Retrieve a list of all configured GIS servers
gis_servers = gis.admin.servers.list()

# Iterate through each server and start all services
for server in gis_servers:
    for service in server.services.list():
        # Uncomment the following line to stop services instead of starting them
        # service.stop()
        service.start()
        print("Service Started:", service)

# Retrieve the updated list of GIS servers
gis_servers1 = gis.admin.servers.list()

# Identify and list all available folders in the GIS server structure
for folder in gis_servers1:
    for server in folder.services:
        try:
            if server[0] == 'folders':  # Checking if the tuple contains folder information
                list_folders = server[1]  # Extract the list of folders
                print("Folders Found:", server[1])
                print("Total Folders:", len(server[1]))
        except Exception as e:
            print(f"Error while retrieving folders: {e}")

# Iterate through each folder and start services within them
for folder in gis_servers1:
    for server in folder.services:  # Iterate through the list of tuples
        try:
            if server[0] == 'folders':  # Check if it is a folder structure
                # Iterate through each folder and retrieve hosted services
                for i in list_folders:
                    hosted_services = folder.services.list(folder=i)
                    for service in hosted_services:
                        # Uncomment the following line to stop services instead of starting them
                        # service.stop()
                        service.start()
                        print("Service Started in Folder:", hosted_services[0])
        except Exception as e:
            print(f"Error while starting services in folders: {e}")
