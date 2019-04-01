game1 = [-1, 1, 5, 2, 7, 3, 0, 0, 0, 0]
outcome1 = -1
game2 = [1, 5, 1, 8, 3, 4, 2, 0, 0, 0]
outcome2 = -1
game3 = [-1, 1, 9, 2, 6, 8, 4, 5, 0, 0]
outcome3 = -1

situation1 = [-1, 1, 2, 3, 0, 0, 0, 0, 0, 0]
situation2 = [-1, 1, 2, 4, 0, 0, 0, 0, 0, 0]
situation3 = [-1, 1, 2, 5, 0, 0, 0, 0, 0, 0]
situation4 = [-1, 1, 2, 6, 0, 0, 0, 0, 0, 0]

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)

regressor.fit([game1, game2, game3], [outcome1, outcome2, outcome3])

pred1 = regressor.predict([situation1, situation2, situation3, situation4])

print(pred1)