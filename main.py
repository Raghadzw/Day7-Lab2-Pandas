import pandas as pd

x = pd.read_csv("C:/Users/ragha/Desktop/instagram_users.csv")


print("Number of rows:" , len(x))

print("Number of columns:" , len(x.columns))

print("Size of dataset:" , x.size )

print("Type of columns:" , x.dtypes )

print(x)

print(x.head())
print(x.tail())

print("Null values=" , x.isna().sum().sum())

print(x[x.duplicated()])
print(x.drop_duplicates(inplace = True))


print("Number of rows after remove duplicate values:" , len(x))

print("Number of columns after remove duplicate values:" , len(x.columns))


x.columns = ["Num_posts" , "Num_following" ,"Num_followers" ,"Biography_length" ,"Picture_availability" ,
             "Link_avability" ,"Average_caption_length" ,"Caption_zero" , "Non_image_percentage" ,"Engagement_rate_like" ,
                   "Enagement_rate_comment" , "Loction_tag_percntage" ,"Average_hashtag_count", "Promotional_keywords" ,
             "Followers keywords" , "Cosine similarity" ,"Post interval", "real_fake"]

x["real_fake"] = x["real_fake"].replace(["f"] ,"fake")
x["real_fake"] = x["real_fake"].replace(["r"],"real")


print("Total number of fake accounts=" , x["real_fake"].value_counts()["fake"])
print("Total number of real accounts=" , x["real_fake"].value_counts()["real"])

print(x.describe())