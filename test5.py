from __future__ import division

__author__ = 'phil'

# exercises from Data Science from Scrath
# code may or may not mirror the text examples

# data set being analyzed is a list of users and connections

users = [
    {"id": 0, "name": "hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5.7), (6.8), (7.8), (8, 9)]


# now add list of friends/connections for each user

for user in users:
    user["friends"] = []

# for i,j in range(friendships):  this generated an error because range wanted integers, not a list
for i, j in friendships:
    users[i]["friends"].append(users[j])  # add i as a friend of j
    users[j]["friends"].append(users[i])
