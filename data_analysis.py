import pandas as pd
import re
from managers import MessagesManager
import matplotlib.pyplot as plt


class AbstractAnalyser:
    def load_data(self):
        pass
    
    def analysing(self):
        pass
    
    
class CountryCrimeAnalyser(AbstractAnalyser):    
    def __init__(self, all_data):
        self.countrys_df = pd.DataFrame()
        self.killers_number = None
        self.all_data = all_data
        
    def load_data(self):
        self.countries_df = pd.read_csv(self.all_data, usecols=["Country"])
    
    def analysing(self):
        splited_countries = self.countries_df["Country"].str.split("\n")      
        exploded_df = self.countries_df.assign(Country=(splited_countries).explode("Country"))  
        self.killers_number = exploded_df["Country"].value_counts()
        self.killers_number = pd.DataFrame({
            "Country" : self.killers_number.index,
            "Killers"  : self.killers_number.values},
            )
        self.killers_number["Country"] = self.killers_number["Country"].str.replace("(suspected)", "")
        most_dangerous = self.killers_number.head(1).to_numpy()
        safest = self.killers_number.tail(1).to_numpy()
        MessagesManager.country_crime_result(most_dangerous, safest)
        
    def to_csv(self):
        self.killers_number.to_csv("global_murder_map.csv")
    
    def make_chart(self):
        top_ten_dangerous = self.killers_number.head(10)
        top_ten_safest = self.killers_number.tail(10)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        ax1.bar(top_ten_dangerous["Country"], top_ten_dangerous["Killers"], color='red')
        ax1.set_title("Top 10 Dangerous Countries")
        ax1.set_xlabel("Country", loc="center", labelpad=20)
        ax1.set_ylabel("Killers", loc="center", labelpad=20)
        ax1.tick_params(axis='x', rotation=90)  
        ax2.bar(top_ten_safest["Country"], top_ten_safest["Killers"], color='green')
        ax2.set_title("Top 10 Safest Countries")
        ax2.set_xlabel("Country", loc="center", labelpad=-20)
        ax2.set_ylabel("Killers", loc="center", labelpad =20)
        ax2.tick_params(axis='x', rotation=90)
        plt.tight_layout(h_pad=1) 
        plt.show()



class MurderMethodAnaliser(AbstractAnalyser):
    def analysing(self):
        print("murder method analysing")
    
    def to_csv(self):
        print("murder method csv")
    
    def make_chart(self):
         print("murder method chart")
         
         
class KillerActivityAnalyzer(AbstractAnalyser):
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None  # DataFrame

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        self.df = self.df[["Years active", "Proven victims"]]
        self.df["Years active (duration)"] = self.df["Years active"].apply(
            self.years_to_duration)
        self.df["Proven victims (num)"] = self.df["Proven victims"].apply(
            self.victims_to_number)
        #print(self.df.head())

    @staticmethod
    def years_to_duration(years_str):
        numbers = re.findall(r"\d{4}", years_str)
        start = int(numbers[0])
        if len(numbers) > 1:
            end = int(numbers[1])
        else:
            end = start
            return 1
        return (end - start) + 1

    @staticmethod
    def victims_to_number(victims_str):
        numbers = re.findall(r"\d+", str(victims_str))
        if len(numbers) > 1:
            return (int(numbers[0]) + int(numbers[1])) / 2
        return int(numbers[0])

    def analising(self):
        corr = self.df["Years active (duration)"].corr(
            self.df["Proven victims (num)"])
        print(MessagesManager.show_corr(), corr)

        if corr > 0:
            print(MessagesManager.positive_corr())
        elif corr < 0:
            print(MessagesManager.negative_corr())
        else:
            print(MessagesManager.no_corr())


