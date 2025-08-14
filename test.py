
import os
from DataBase.data_manager import DataManager 
from data_analysis import CountryCrimeAnalyser as analyser


data_manager = DataManager("DataBase", "data_set")
while_break = False
while True:
    if while_break :
        break
    else:
        if data_manager.is_exist():
            data_analiser = analyser(data_manager.all_data_path)
            data_analiser.load_data()
            data_analiser.analysing()
            while True:
                if os.path.exists("global_murder_map.csv"):
                    data_analiser.make_chart()
                    while_break = True
                    break
                else:
                    data_analiser.to_csv()
        else:
            data_manager.concating()
            data_manager.to_csv()            
        
        
    
