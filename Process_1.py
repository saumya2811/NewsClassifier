import pandas as pd

hindu = pd.read_csv('hindu.csv')


hindu.dropna(how='any', inplace=True)
hindu.drop(hindu[(hindu['Title']=="None") | (hindu['Tag']=="None") | (hindu['Body']=="None")].index, inplace=True)
hindu['Tag'].replace(["Cricket", "Tennis", "Football", "Hockey", "Athletics", "Races", "Motorsport", "Formula One"],"Sports", inplace=True, regex=True)
hindu['Tag'].replace(["Sci-Tech", "Science", "Technology", "Gadgets", "Internet"],"Science and Technology", inplace=True, regex=True)
hindu['Tag'].replace([ "Authors", "Review"],"Books", inplace=True, regex=True)
hindu['Tag'].replace("Bookss","Books", inplace=True, regex=True)
hindu['Tag'].replace([ "Careers", "Education", "Colleges"],"Education", inplace=True, regex=True)
hindu['Tag'].replace([ "Markets", "Business", "Industry"],"Economy", inplace=True, regex=True)
hindu['Tag'].replace("Other Sports","Sports", inplace=True, regex=True)
hindu['Tag'].replace([ "Science and Science and Technology and Science and Technology","Science and Science and Technology" ],"Science and Technology ", inplace=True, regex=True)
hindu['Tag'].replace([ "Health", "Food", "Fashion", "Fitness", "Homes and gardens", "Motoring", "Travel", "Society"],"Life & Society", inplace=True, regex=True)
hindu['Tag'].replace(["Life & Life & Society", "Life & Style", "Life & Society"],"Society", inplace=True, regex=True)
hindu['Tag'].replace("Environment", "Science and Technology", inplace=True, regex=True)
hindu['Tag'].replace("Thiruvananthapuram","Kerala", inplace=True, regex=True)
hindu['Tag'].replace(["Vijayawada", "Visakhapatnam"], "Andhra Pradesh", inplace=True, regex=True)
hindu['Tag'].replace("Puducherry", "Other States", inplace=True, regex=True)
hindu['Tag'].replace(["Chennai", "Kolkata", "Mumbai", "Bengaluru"],"Metro", inplace=True, regex=True)
hindu['Tag'].replace(["Tiruchirapalli"], "Tamil Nadu", inplace=True, regex=True)
hindu['Tag'].replace("Hyderabad", "Telangana", inplace=True, regex=True)
hindu['Tag'].replace("Kozhikode","Kerala", inplace=True, regex=True)
hindu['Tag'].replace("Mangaluru","Karnataka", inplace=True, regex=True)
hindu['Tag'].replace("Metro","Metros", inplace=True, regex=True)
hindu['Tag'].replace("Kochi","Kerala", inplace=True, regex=True)
hindu['Tag'].replace("Coimbatore","Tamil Nadu", inplace=True, regex=True)
hindu['Tag'].replace("Madurai","Tamil Nadu", inplace=True, regex=True)

hindu.drop(hindu[(hindu['Tag']=="Madurai") | (hindu['Tag']=="Coimbatore") | (hindu['Tag']=="Kochi")].index, inplace=True)
hindu = hindu.groupby('Tag').filter(lambda x: len(x) > 40)
print(hindu.head(15))
hindu.to_csv('data.csv')
data=pd.read_csv('data.csv')
print(data.head(15))
























