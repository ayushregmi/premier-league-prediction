import requests
from bs4 import BeautifulSoup
import pandas as pd

html_list = [
        requests.get("https://www.fifaindex.com/teams/fifa18_278/?league=13&order=desc").text, # fifa 18
        requests.get("https://www.fifaindex.com/teams/fifa19_353/?league=13&order=desc").text, #fifa 19
        requests.get("https://www.fifaindex.com/teams/fifa20_419/?league=13&order=desc").text, #fifa 20
        requests.get("https://www.fifaindex.com/teams/fifa21_486/?league=13&order=desc").text, #fifa 21
        requests.get("https://www.fifaindex.com/teams/fifa22_555/?league=13&order=desc").text #fifa 22
        
]

lst = [["season", "team", "ATT", "MID", "DEF", "OVR"]]

year = ["2017-18", "2018-19", "2019-20", "2020-21", "2021-22"]

name = []

def get_ratings():
    for j, html in enumerate(html_list):


        soup = BeautifulSoup(html, "html.parser")

        table = soup.find("table")


        for i, row in enumerate(table.find_all("tr")[3:]):
            col = row.find_all("td")
            temp = []
            if len(col) == 8:
                name_ = col[1].find("a").text.lower()

                if name_ == "afc bournemouth":
                    name_ = "bournemouth"

                if name_ not in name:
                    name.append(name_)

                lst.append([
                    year[j],
                    name_, 
                    int(col[3].text), 
                    int(col[4].text),
                    int(col[5].text),
                    int(col[6].text)
                    ])

    fifa_ratings = pd.DataFrame(columns=lst[0])

    fifa_ratings_list = []
    for row in lst[1:]:
        temp = {"season":[row[0]], "team":[row[1]], "ATT":[row[2]],"MID":[row[3]],"DEF":[row[4]],"OVR":[row[5]]}
        # df.loc[len(df.index)] = row
        fifa_ratings = pd.concat([fifa_ratings, pd.DataFrame(temp)], ignore_index=True)

        fifa_ratings_list.append([row[0],row[1],row[2],row[3],row[4],row[5]])

    # pd.set_option('display.max_rows', fifa_ratings.shape[0]+1)
    # print(fifa_ratings)
    name.sort()

    team_names = pd.DataFrame({"club":name, "team_key":range(len(name))})

    fifa_ratings = fifa_ratings.merge(team_names, left_on="team", right_on="club")

    team_names = team_names.set_index(["team_key"])
    # print(team_names)

    fifa_ratings = fifa_ratings.drop("club", axis=1).drop("team", axis = 1)

    team_names.loc[4] = "brighton"
    team_names.loc[6] = "cardiff"
    team_names.loc[11] = "huddersfield"
    team_names.loc[12] = "leeds"
    team_names.loc[13] = "leicester"
    team_names.loc[15] = "man city"
    team_names.loc[16] = "man united"
    team_names.loc[17] = "newcastle"
    team_names.loc[18] = "norwich"
    team_names.loc[19] = "sheffield united"
    team_names.loc[21] = "stoke"
    team_names.loc[22] = "swansea"
    team_names.loc[23] = "tottenham"
    team_names.loc[25] = "west brom"
    team_names.loc[26] = "west ham"
    team_names.loc[27] = "wolves"

    # print(fifa_ratings_list)
    return fifa_ratings.merge(team_names, left_on="team_key", right_on="team_key").head(n=100).to_numpy()

