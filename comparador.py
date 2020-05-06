import numpy as np

followers = []
following = []

with open('followers.txt', 'r') as file:
    for line in file:
        followers.append(line)

with open('following.txt', 'r') as file:
    for line in file:
        following.append(line)

print(len(followers))
print(len(following))

dont_follow_back = np.setdiff1d(following, followers)

print(dont_follow_back)
print(len(dont_follow_back))

with open('dont follow back.txt', 'w') as file:
    for item in dont_follow_back:
        file.write(item)