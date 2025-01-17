#!/usr/bin/env python
# coding: utf-8

# In[60]:


from arcgis.gis import GIS


# In[61]:


import arcgis.gis.admin


# In[62]:


gis = GIS("https://arcgisportal.tohowater.com/arcgis/home/", "portaladmin", "getmein2myPM")


# In[63]:


gis_servers = gis.admin.servers.list()


# In[ ]:





# In[64]:


for server in gis_servers:
    print("Hello from ArcGIS API for Python!",server)


# In[ ]:





# In[65]:


for server in gis_servers:
    for service in server.services.list():
        #service.stop()
        #service.start()
        print("service1",service)


# In[66]:


#servers = gis.admin.servers.list()


# In[67]:


gis_servers1 = gis.admin.servers.list()


# In[68]:


"""
for folder in gis_servers1:
    #for server in folder.services:
    for server in folder.services:
        try:
            #print(server[1])
            if (server[0] == 'folders'):
                list_folders = server[1]
                print (server[1])
                print('length_list',len(server[1]))
            #print(type(server))
        except:
            pass
            """


# In[73]:


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
                        #print('service',hosted_services[0])
                        #print('typeofservice',type(hosted_services[0]))
                        #service.stop()
                        #service.start()
                        #list_folders = server[1]
                        #for i in server[1]
                        #print (server[1])
                        #print('length_list',len(server[1]))
                        #print(type(server))
        except:
            pass


# In[ ]:





# In[ ]:




