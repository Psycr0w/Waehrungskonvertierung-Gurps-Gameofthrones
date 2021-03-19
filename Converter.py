import argparse
from math import floor

parser = argparse.ArgumentParser()

parser.add_argument("num", help="Number of Gurpsdollars to convert.", type=float)
parser.add_argument("md",nargs='?', help="Switch for Moons.", type=bool)

args = parser.parse_args()

md = False
gurpsdollar = args.num * 4
md = args.md

drachendiv = 23520
mondediv = 784
hirschendiv = 112
sternediv = 16
groschendiv = 8
halbgroschendiv = 4
penniesdiv = 2

monde = 0
monddolar = 0

drachen = floor(gurpsdollar / drachendiv)
drachendollar = drachen * drachendiv


if md == True:
    monde = floor((gurpsdollar - drachendollar) / mondediv)
    monddolar = monde * mondediv


hirschen = floor((gurpsdollar - drachendollar - monddolar) / hirschendiv)
hirschdollar = hirschen * hirschendiv
sterne = floor((gurpsdollar - drachendollar - monddolar - hirschdollar) / sternediv)
sterndollar = sterne * sternediv
groschen = floor((gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar) / groschendiv)
groschendollar = groschen * groschendiv
halbgroschen = floor((gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar - groschendollar) / halbgroschendiv)
halbgroschendollar = halbgroschen * halbgroschendiv
pennies = floor((gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar - groschendollar - halbgroschendollar) / penniesdiv)
penniesdollar = pennies * penniesdiv
halbpennies = gurpsdollar - drachendollar  - monddolar - hirschdollar - sterndollar - groschendollar - halbgroschendollar - penniesdollar

currency =["Drachen", "Monde", "Hirschen", "Sterne", "Groschen", "Halbgroschen", "Pennies", "Halbpennies"]

value = [drachen,monde,hirschen,sterne,groschen,halbgroschen,pennies,halbpennies]

array = []

for i in range(0,len(currency)):
    if value[i] != 0:
    
        val = value[i]
        cur = currency[i]
        array.append(f"{val} {cur}")
    

stringer = " , ".join(array)

print(stringer)