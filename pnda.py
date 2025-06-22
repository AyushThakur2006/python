# import pandas as pd
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# my=pd.DataFrame(mydataset)
# print(my)

import pandas as pd
my = pd.read_csv("Personal_Finance_Dataset.csv")
print(my.head(10))
