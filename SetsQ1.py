s1 = {'Math', 'Physics', 'Chemistry'}
s2 = {'Physics', 'Biology', 'Math'}
print("The subjects common between both students are ", s1&s2)
print("The subjects taken by only student 1 are ", s1-s2)
print("The subjects taken by only student 2 are ", s2-s1)
print("Uniquely, the subjects are ", s1|s2)
