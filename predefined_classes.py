"""predefined classes"""
import pandas as pd

# Use the dir(list) command to display all attributes and methods of the list class.
print(dir(list))

# Utiliser la commande help(list) pour afficher la documentation de la classe list.
print(help(list))


# Instantiate an empty DataFrame using the constructor contained in the pandas package. This DataFrame will be named df.

df = pd.DataFrame()


liste_4 = [1, 5, 45, 42, None, 123, 4213, None, 213]


df1 = pd.DataFrame(data=liste_4)
df1.head()


def divise2(result):
    return result / 2


df3 = df2.apply(divise2)
df3
