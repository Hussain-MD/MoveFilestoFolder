# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:40:52 2020

@author: Hussain Dhorajiwala
"""

import csv , json,sys,glob,os
import configparser as cp
from datetime import datetime

arr = []
#read the csv and add the arr to a arrayn

class Move():
    def __init__(self,config_file="Movefolder.properties"):
        try:
            config = cp.RawConfigParser()
            config.read(config_file)
            self.source_path =config.get('APPSETTINGS', 'source_path')
            
            self.dest_path =config.get('APPSETTINGS', 'dest_path')
            self.error_file =config.get('APPSETTINGS', 'error_file')
            
        except Exception as ex:
            exc_type,exc_obj,exc_tb=sys.exc_info()
            print("Error in __init__ method at {}, Error Message---- {} ".format(exc_tb.tb_lineno,ex))
    
    
   
    def MoveFolders(self):
         try:
            import logging
            self.writeoutput("Logger","{}^{}\n".format("Script Start time",str(datetime.now())))
            logging.basicConfig(filename="logfile.log", level=logging.INFO)
            config = cp.RawConfigParser()
            config.read("MoveFolders.properties")

            import os
            import shutil
            fields=[]
            
            with open(self.error_file) as csvfile:
                csvReader = csv.reader(csvfile)
                fields = next(csvReader) 
                for csvRow in csvReader:
                    print(str(csvRow))
                    file=str(csvRow)
                    source=self.source_path+file[2:-2]
                    print(source)
                        
                    dest=self.dest_path+file[2:-2]
                    try:
                        shutil.move(source,self.dest_path)
                        logging.info(file)
                        print("done")
                    except Exception as ex:
                        #self.writeoutput("Error","{}^{}^{}^{}^{}\n".format("output_folder_path",self.dest_path,"filename: ",file))
                        print(ex)
                     
         except Exception as ex:
            exc_type,exc_obj,exc_tb=sys.exc_info()
            print(ex)
                
obj=Move("MoveFolders.properties")
obj.MoveFolders()   
