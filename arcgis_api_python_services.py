#!/usr/bin/env python
# coding: utf-8

# In[60]:
# this script basically stops/start services as part of the state zero script.

from arcgis.gis import GIS


import arcgis.gis.admin

gis = GIS("", "", "")

gis_servers = gis.admin.servers.list()


for server in gis_servers:
    print("Hello from ArcGIS API for Python!",server)


for server in gis_servers:
    for service in server.services.list():
        #service.stop()
        service.start()
        print("service1",service)


gis_servers1 = gis.admin.servers.list()


for folder in gis_servers1:
    for server in folder.services:
        try:
            if (server[0] == 'folders'):
                list_folders = server[1]
                print (server[1])
                print('length_list',len(server[1]))
        except:
            pass
           

for folder in gis_servers1:
    #for server in folder.services:
    for server in folder.services: # array of tuples
        try:
            #print(server[1])
            if (server[0] == 'folders'): # data structure is in tuple (obtaining the first element of the tuple) ('folders',['folder1','folder2','folder3'])
                #hosted_services = server[1].services.list(folder='All_Work_Orders')
                for i in list_folders:
                    hosted_services = folder.services.list(folder=i)
                    for service in hosted_services: #added
                        #service.stop() #added
                        service.start() #added
                        print('service2',hosted_services[0])
        except:
            pass





