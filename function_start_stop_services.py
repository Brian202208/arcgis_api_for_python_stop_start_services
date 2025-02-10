#!/usr/bin/env python
# coding: utf-8
# Author: Michael Preko Nkum

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
        
    # Initialize connection to GIS (Replace with your credentials)
    gis = GIS("", "", "")
    
    try:
        #  Connect to ArcGIS Enterprise/ArcGIS Online
        gis_servers = gis.admin.servers.list()

        
        for server in gis_servers:
            print("Hello from ArcGIS API for Python!", server)

        # loops through the services to stop or start the gis services
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

        
        gis_servers1 = gis.admin.servers.list()
        # loops through to obtain the folders property in a tuple
        for folder in gis_servers1:
            for server in folder.services:
                try:
                    if server[0] == 'folders':
                        list_folders = server[1]
                        print("Folders:", list_folders)
                        print('Number of folders:', len(list_folders))
                except Exception as e:
                    print("Error while processing folders:", str(e))


        
        # loops through the folder and sub-folders to start or stop services as needed
        for folder in gis_servers1:
            for server in folder.services:
                try:
                    if server[0] == 'folders':
                        for folder_name in list_folders:
                            hosted_services = folder.services.list(folder=folder_name)
                            for service in hosted_services:
                                try:
                                    if action == "start":
                                        service.start()
                                        print('Service started:', service)
                                    elif action == "stop":
                                        service.stop()
                                        print("Service stopped:", service)
                                except Exception as e:
                                    print("Failed to start/stop service in folder:", service)
                                    print("Error:", str(e))
                except Exception as e:
                    print("Error while processing hosted services:", str(e))

    except Exception as e:
        print("Failed to execute script:", str(e))
        sys.exit(1)  # Exit with an error code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python function_start_stop_services.py <start|stop>")
        sys.exit(1)

    # Retrieve the action argument from the command line
    action = sys.argv[1].lower()
    function_start_stop_services(action)
