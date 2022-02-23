import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json
import datetime

d = datetime.datetime.now()
current_date = d.strftime("%Y-%m-%d")

html = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index")
bs = BeautifulSoup(html.text, "html.parser")

table_class = "wikitable sortable jquery-tablesorter"

table = bs.find("table",{"class":"wikitable"})

df = pd.read_html(str(table))
df = pd.DataFrame(df[0])

df.columns = ["Rank", "Change", "Nation", "Index", "Growth"]

df = df[["Nation","Index"]]
unordered_df = df.sort_values("Nation")
sorted_df = unordered_df.reset_index(drop=True)

response = requests.get("https://restcountries.com/v3.1/all")
responseJason = json.loads(response.text)

normal = pd.json_normalize(responseJason)
normal[["name.common", "population","gini.2016", "gini.2017","gini.2018", "gini.2019"]]
separate_gini = normal[["gini.2016", "gini.2017","gini.2018", "gini.2019"]]
normal["gini"] = separate_gini.sum(axis=1, numeric_only=True)

gini_mean = normal.mean()["gini"]
api_frame = normal.replace(0,gini_mean)
api_frame = api_frame.rename(columns={"name.common":"Nations", "population":"Population", "gini":"Gini", "area":"Area"})
hdi_countries = api_frame[(api_frame.unMember == True) | (api_frame.Nations =="Palestine") | (api_frame.Nations =="Hong Kong")]
new_api_frame = hdi_countries[["Nations", "Population","Gini","Area"]]

#display(new_api_frame.loc[(new_api_frame["Nation"]=="Nauru")]
#new_api_frame.loc[new_api_frame["Nation"]!="Nauru" "Monaco"]
#new_api_frame[(new_api_frame["Nations"]=="Nauru") | (new_api_frame["Nations"]=="Monaco") |(new_api_frame["Nations"]=="North Korea")|(new_api_frame["Nations"]=="San Marino") |(new_api_frame["Nations"]=="Somalia")| (new_api_frame["Nations"]=="Tuvalu")].index

new_api_frame = new_api_frame.drop([1,21,171,206,228,235])

unordered_api_frame = new_api_frame.sort_values("Nations")
sorted_api_frame = unordered_api_frame.reset_index(drop=True)

joined = sorted_df.join(sorted_api_frame)
country_data = joined[["Nation", "Index","Population","Gini","Area"]]

population_correlation = country_data["Index"].corr(country_data["Population"])
gini_correlation = country_data["Index"].corr(country_data["Gini"])
area_correlation = country_data["Index"].corr(country_data["Area"])

round_pop_corr = round(population_correlation,3)
round_gini_corr = round(gini_correlation,3)
round_area_corr = round(area_correlation, 3)

correlation = {"":["Population", "Area", "Gini"],
               "HDI score": [round_pop_corr, round_area_corr, round_gini_corr]}

report = pd.DataFrame(correlation)

array = report.to_numpy()
print(country_data)
print("Correlation report generated!")
np.savetxt(current_date+".txt", array, fmt="%s", header="Correlation report")

