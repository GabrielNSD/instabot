'''
list_xpath = []

for i in range(1,10):
    num = i
    new_x = '/html/body/div[4]/div/div[2]/ul/div/li[' + str(num) + ']/div/div[2]/div[1]/div/div/a'
    list_xpath.append(new_x)

print(type(list_xpath[0]))


with open('xpaths.txt', 'w') as file:
    for item in list_xpath:
        file.write("%s\n" % item)
'''

a ='1.428'
new_a = a.replace('.', '')

print(new_a)