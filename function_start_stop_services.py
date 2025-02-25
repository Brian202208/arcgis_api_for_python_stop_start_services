#!/usr/bin/env python
# coding: utf-8

"""
ArcGIS Server Service Management Script

This script allows starting or stopping ArcGIS server services using the ArcGIS API for Python.
It can be executed with a command-line argument ("start" or "stop") to control the services accordingly.

Author: Michael Preko Nkum
"""

# Import necessary modules
from arcgis.gis import GIS
import arcgis.gis.admin
import sys

def function_start_stop_services(action):
    """
    Starts or stops services on all servers for the configured GIS instance.

    Args:
        action (str): Either "start" or "stop" to perform the respective action on services.
    """
    if action not in ["start", "stop"]:
        print("Invalid action. Please specify 'start' or 'stop'.")
        sys.exit(1)
        
    # Initialize connection to GIS (Replace with actual credentials)
    gis = GIS("", "", "")

    try:
        # Retrieve a list of ArcGIS servers
        gis_servers = gis.admin.servers.list()

        # Print confirmation of connection
        for server in gis_servers:
            print("Connected to ArcGIS API for Python:", server)

        # Loop through each server and perform the requested action (start/stop)
        for server in gis_servers:
            for service in server.services.list():
                try:
                    if action == "start":
                        service.start()
                        print("Service started:", service)
                    elif action == "stop":
                        service.stop()
                        print("Service stopped:", service)
                except Exception as e:
                    print("Failed to start/stop service:", service)
                    print("Error:", str(e))

        # Retrieve updated list of GIS servers
        gis_servers1 = gis.admin.servers.list()

        # Identify and extract folders from the GIS server structure
        for folder in gis_servers1:
            for server in folder.services:
                try:
                    if server[0] == 'folders':  # Check if the tuple represents folder structure
                        list_folders = server[1]  # Extract folder names
                        print("Folders Identified:", list_folders)
                        print("Total Folders:", len(list_folders))
                except Exception as e:
                    print("Error while processing folders:", str(e))

        # Iterate through each folder and start/stop hosted services
        for folder in gis_servers1:
            for server in folder.services:
                try:
                    if server[0] == 'folders':  # Ensure it's a folder structure
                        for folder_name in list_folders:
                            hosted_services = folder.services.list(folder=folder_name)
                            for service in hosted_services:
                                try:
                                    if action == "start":
                                        service.start()
                                        print("Service started in folder:", service)
                                    elif action == "stop":
                                        service.stop()
                                        print("Service stopped in folder:", service)
                                except Exception as e:
                                    print("Failed to start/stop service in folder:", service)
                                    print("Error:", str(e))
                except Exception as e:
                    print("Error while processing hosted services:", str(e))

    except Exception as e:
        print("Failed to execute script:", str(e))
        sys.exit(1)  # Exit with an error code

if __name__ == "__main__":
    # Check if the user provided a valid command-line argument
    if len(sys.argv) < 2:
        print("Usage: python function_start_stop_services.py <start|stop>")
        sys.exit(1)

    # Retrieve the action argument from the command line and convert it to lowercase
    action = sys.argv[1].lower()
    function_start_stop_services(action)
