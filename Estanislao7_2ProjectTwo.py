#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 04:37:32 2024

@author: tomasestanisl_snhu
"""
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # USER = 'aacuser'
        # PASS = 'TestPass1'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31878
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connection Successful")

# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary 
            return result.acknowledged # true or false
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Read method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            result = list(self.database.animals.find(data))  # list of data from find query
            return result # empty list if unsuccessful
        else:
            raise Exception("Nothing to retrieve, because data parameter is empty")
            
# Update method to implement the U in CRUD.
    def update(self, data, new):
        if data is not None or new is not None:
            result = self.database.animals.update_many(data, new)  # data should be filter query and new is the action to perform.
            return result.modified_count # number of modified objects
        else:
            raise Exception("Nothing to update, because data or new parameter is empty")
            
# Delete method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)  # data should be filter query
            return result.deleted_count # number of deleted objects
        else:
            raise Exception("Nothing to delete, because data parameter is empty")