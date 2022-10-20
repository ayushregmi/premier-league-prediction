from pstats import Stats
from statistics import mean
import numpy as np
from test import get_ratings
import tensorflow as tf

file = open("result(2017 onwards).csv", "rb")

'''
{"team name": {
                    season:[average goals scored in home games, average goals conceeded in home games, 
                        average goals scored in away games, average goals conceeded in away games]
                    
                }
}
'''

goals = []
team_dict = {}

count = 0

for row in file:

    col = row.decode().split(",")
    
    if col[0] == "Season":
        continue
    
    season = col[0]
    home_team = col[1].lower()
    away_team = col[2].lower()
    home_goal = int(col[3])
    away_goal = int(col[4])

    if home_team == "man city" and season == "2017-18":
        count += away_goal

    if home_team not in team_dict:
        team_dict[home_team] = {}

    if away_team not in team_dict:
        team_dict[away_team] = {}
    
    home_stats_season = team_dict[home_team]
    away_stats_season = team_dict[away_team]

    if season not in home_stats_season:
        home_stats_season[season] = [[], [], [], []]
    
    if season not in away_stats_season:
        away_stats_season[season] = [[], [], [], []]
    
    home_stats_season[season][0].append(home_goal)
    home_stats_season[season][1].append(away_goal)

    away_stats_season[season][2].append(away_goal)
    away_stats_season[season][3].append(home_goal)

file.close()
# print(count)

# for season, stats in team_dict["man city"].items():
#     print(season)
#     for stat in stats:
#         print(sum(stat))


'''
mean_scores = {"team_name":{
    "season": [gw1, gw2, ... gw38] => (gw1 = [av. home scored, av. home conceeded, av. away scored, av. away conceeded])
}}
'''

mean_scores = {}

for team in team_dict:
    # print(team)
    home_games = 0
    away_games = 0
    home_scored = 0
    home_conceeded = 0
    away_scored = 0
    away_conceeded = 0

    file = open("result(2017 onwards).csv", "rb")
    for row in file:
        col = row.decode().split(",")

        if col[0] == "Season":
            continue

        season = col[0]
        home_team = col[1].lower()
        away_team = col[2].lower()
        home_goal = int(col[3])
        away_goal = int(col[4])

        if team == home_team or team == away_team:

            if team not in mean_scores:
                mean_scores[team] = {}
            
            if season not in mean_scores[team]:
                mean_scores[team][season] = []

                # print(home_games)
                home_games = 0
                away_games = 0
                home_scored = 0
                home_conceeded = 0
                away_scored = 0
                away_conceeded = 0
                

            if team == home_team:
                home_games += 1
                home_scored += home_goal
                home_conceeded += away_goal
            
            elif team == away_team:
                away_games += 1
                away_scored += away_goal
                away_conceeded += home_goal
            
            lst = [
                home_scored / (home_games if home_games != 0 else 1), 
                home_conceeded / (home_games if home_games != 0 else 1), 
                away_scored / (away_games if away_games != 0 else 1), 
                away_conceeded / (away_games if away_games != 0 else 1)
                ]
            
            mean_scores[team][season].append(lst)

    file.close()


fifa_ratings = get_ratings() #[season, att, mid ,def, ovr, team_id, team]

input_data = np.zeros((1829, 16))
'''
[home ovr, home att, home mid, home def, home av goal in home, home av conceeded in home, home av goal scored away,
 home av goal conceeded away, 
 away ovr, away att, away mid, away def, away av goal in home, away av conceeded in home, away av goal scored in away, 
 away av goal conceeded away]
'''

fifa_ratings_dict = {} #{team: {season:[att, mid, def, ovr]}}

games_count = {}

for [season, att, mid, defend, ovr, id, team] in fifa_ratings:
    if team not in fifa_ratings_dict:
        fifa_ratings_dict[team] = {}
        games_count[team] = {}
    
    if season not in fifa_ratings_dict[team]:
        fifa_ratings_dict[team][season] = [att, mid, defend, ovr]
        games_count[team][season] = 0

# data are in fifa_ratings_dict and mean_scores

'''
fifa_ratings_dict = {"team":
                            {
                            "season":
                                    [att, mid, def, ovr]
                            }
                    }

mean_scores = {"team": 
                        {
                        "season":
                                [gw1, gw2, gw3... gw38] => gw1 = [av. home goal, av. home con., av. away goal, av. away con.]
                        }
                }

games_count = {"team" : {"season" :games_count}}

'''

file = open("result(2017 onwards).csv", "rb")

output_data = np.zeros((input_data.shape[0], 3))

for index, row in enumerate(file):
    col = row.decode().split(',')
    if col[0] == "Season":
            continue

    season = col[0]
    home_team = col[1].lower()
    away_team = col[2].lower()
    home_game = games_count[home_team][season]
    away_game = games_count[away_team][season]
    result = col[5].lower()
    
    index = index - 1

    home_att = fifa_ratings_dict[home_team][season][0]
    home_def = fifa_ratings_dict[home_team][season][1]
    home_mid = fifa_ratings_dict[home_team][season][2]
    home_ovr = fifa_ratings_dict[home_team][season][3]
    
    if home_game == 0:
        home_goal_home = 0
        home_conceed_home = 0
        home_goal_away = 0
        home_conceed_away = 0
    else:    
        home_goal_home = mean_scores[home_team][season][home_game - 1][0]
        home_conceed_home = mean_scores[home_team][season][home_game - 1][1]
        home_goal_away = mean_scores[home_team][season][home_game - 1][2]
        home_conceed_away = mean_scores[home_team][season][home_game - 1][3]

    away_att = fifa_ratings_dict[away_team][season][0]
    away_def = fifa_ratings_dict[away_team][season][1]
    away_mid = fifa_ratings_dict[away_team][season][2]
    away_ovr = fifa_ratings_dict[away_team][season][3]
    
    if away_game == 0:
        away_goal_home = 0
        away_conceed_home = 0
        away_goal_away = 0
        away_conceed_away = 0
    else:
        away_goal_home = mean_scores[away_team][season][away_game - 1][0]
        away_conceed_home = mean_scores[away_team][season][away_game - 1][1]
        away_goal_away = mean_scores[away_team][season][away_game - 1][2]
        away_conceed_away = mean_scores[away_team][season][away_game - 1][3]

    input_data[index][0] = home_att
    input_data[index][1] = home_def
    input_data[index][2] = home_mid
    input_data[index][3] = home_ovr
    input_data[index][4] = home_goal_home
    input_data[index][5] = home_conceed_home
    input_data[index][6] = home_goal_away
    input_data[index][7] = home_conceed_away
    input_data[index][8] = away_att
    input_data[index][9] = away_def
    input_data[index][10] = away_mid
    input_data[index][11] = away_ovr
    input_data[index][12] = away_goal_home
    input_data[index][13] = away_conceed_home
    input_data[index][14] = away_goal_away
    input_data[index][15] = away_conceed_away
    
    if result == "h":
        output_data[index][0] = 1
    elif result == "d":
        output_data[index][1] = 1
    elif result == "a":
        output_data[index][2] = 1
    

    games_count[home_team][season] += 1
    games_count[away_team][season] += 1


i = 7
print(input_data[i], output_data[i])

test_size = 1600

model = tf.keras.models.Sequential(
    [
        tf.keras.Input(shape=(16,)),
        tf.keras.layers.Dense(units=24, activation="relu"),
        tf.keras.layers.Dense(units=3, activation="linear")
    ]
)

model.compile(loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.Adam(learning_rate=5e-3))

training_X = input_data[:test_size, :]
training_y = output_data[:test_size, :]

testing_X = input_data[test_size:, :]
testing_y = output_data[test_size:, :]

model.fit(training_X, training_y, epochs=100)

pred = model.predict_on_batch(training_X)
print(pred)
pred = np.argmax((pred == pred.max(axis=1)[:,None]).astype(int), axis = 1)

y = np.argmax(training_y, axis = 1)

count = 0
pred = pred.T
y = y.T

for i in range(pred.shape[0]):
    if pred[i] == y[i]:
        count += 1

print("training accuracy: ", count / pred.shape[0])

#testing

pred = model.predict_on_batch(testing_X)
# print(pred)
pred = np.argmax((pred == pred.max(axis=1)[:,None]).astype(int), axis = 1)

y = np.argmax(testing_y, axis = 1)

count = 0
pred = pred.T
y = y.T

for i in range(pred.shape[0]):
    if pred[i] == y[i]:
        count += 1

print("testing accuracy: ", count / pred.shape[0])