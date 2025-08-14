import os
import pandas as pd

class DataManager:
    def __init__(self, base_directory : str, second_directory : str):
        self.all_data = pd.DataFrame()
        self.base_directory = base_directory
        self.second_directory_path = os.path.join(self.base_directory, second_directory)
        self.all_data_path = os.path.join(self.second_directory_path, "all_data.csv")
        
    def concating(self):
        data_frames = []
        for file_name in os.listdir(self.second_directory_path):
            file = os.path.join(self.second_directory_path, file_name)
            if file.endswith(".csv"):
                datas = pd.read_csv(file)
            data_frames.append(datas)
        try:
            self.all_data = pd.concat(data_frames, ignore_index=True)
        except Exception as error:
            print(f"we have a problem : {error}")
            
    def is_exist(self):
        if os.path.exists(self.all_data_path):
            return True
        
    def to_csv(self):
        self.all_data.to_csv(self.all_data_path,index=True)
        
        
    
        
        
        
        
        
