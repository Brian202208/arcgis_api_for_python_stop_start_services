#!/usr/bin/env python
# coding: utf-8
"""
This script is designed to start or stop all services on a standalone ArcGIS Server. 
It does not support ArcGIS Servers that are federated with a portal.

Usage:
    python function_start_stop_services.py <start|stop>

Arguments:
    start: Initiates all services on the ArcGIS Server.
    stop: Stops all services on the ArcGIS Server.

Requirements:
    - ArcGIS API for Python
    - Standalone ArcGIS Server
    - Valid credentials for authentication

Author:
    Michael Nkum
"""

import sys
from arcgis.gis.server import Server

def function_start_stop_services_external(action):
    """
    Starts or stops all services on the configured standalone ArcGIS Server.

    Args:
        action (str): Specifies the action to perform, either "start" or "stop".

    Raises:
        SystemExit: If an invalid action is provided or if an error occurs during execution.
    """
    if action not in ["start", "stop"]:
        print("Invalid action. Please specify 'start' or 'stop'.")
        sys.exit(1)
    
    # Define server connection parameters (Replace with actual credentials)
    server_base_url = "https://arcgis02.intra.tohowater.com"
    
    try:
        # Establish connection to the ArcGIS Server
        server = Server(
            url=f"{server_base_url}:6443/arcgis/admin",
            tokenurl=f"{server_base_url}:6443/arcgis/rest/generateToken",
            username="",  # Provide username
            password=""   # Provide password
        )
    except Exception as e:
        print("Failed to connect to ArcGIS Server:", str(e))
        sys.exit(1)
    
    try:
        # Process root directory services
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
        
        # Process services within folders
        for service in server.services:
            try:
                if service[0] == 'folders':
                    list_folders = service[1]
                    print("Processing folders:", list_folders)
                    
                    for folder_name in list_folders:
                        hosted_services = server.services.list(folder=folder_name)
                        print("Hosted services in folder:", folder_name, hosted_services)
                        
                        for hosted_service in hosted_services:
                            try:
                                if action == "start":
                                    hosted_service.start()
                                    print("Service started:", hosted_service)
                                elif action == "stop":
                                    hosted_service.stop()
                                    print("Service stopped:", hosted_service)
                            except Exception as e:
                                print("Failed to start/stop service in folder:", hosted_service)
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
    function_start_stop_services_external(action)
