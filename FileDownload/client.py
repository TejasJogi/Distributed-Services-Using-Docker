import requestes

url = 'http://localhost:5050/download/'
filename = input("Enter file name: ")
path = './Download/'

file = open(path + filename, mode='wb').write(response.content)
print(response.headers)
