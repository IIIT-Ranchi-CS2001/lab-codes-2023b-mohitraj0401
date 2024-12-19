singers = { "rohan", "sohan", "arpit", "gaurav"}
dancers = { "rohan" ,"akash", "shobhit", "naman"}

artists = singers.union(dancers)
print("all artists are: ", artists)
allrounders = singers.intersection(dancers)
print("allrounders are: ", allrounders)

dancersButNotSingers = (dancers.difference(singers))
print("dancersButNotSingers are: ", dancersButNotSingers)
singersButNotDancers =  (singers.difference(dancers))
print("singersButNotDancers are: ", singersButNotDancers)
dancersButNotSingersCumSingersButNotDancers = dancersButNotSingers.union(singersButNotDancers)
print("dancersButNotSingersCumSingersButNotDancers are: ", dancersButNotSingersCumSingersButNotDancers )