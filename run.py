print("Welcome to Insta-Assitant\n")

print("Where we help your business reach more followers and create a buget for you.\n")

name = input("Please enter your name:")

print(f"\n Hello {name} ")

print("Instgram industry \n 1.Healthcare \n 2.Media \n 3.Education \n 4.Nonprofit \n 5.Restaurants \n 6.Tech \n 7.Travel & Tourism \n 8.Finance \n 9.Hospitality ")

social_media_industry = input("\n Please enter which  number represents your industry:")

def industry_indetifier():
    global user_industry
    user_industry = ""

    if int(social_media_industry) == 1:
        user_industry = "Healthcare"
    elif int(social_media_industry) == 2:
        user_industry = "Media"
    elif int(social_media_industry) == 3:
        user_industry = "Education"
    elif int(social_media_industry) == 4:
        user_industry = "Nonprofit"
    elif int(social_media_industry) == 5:
        user_industry = "Restaurants"
    elif int(social_media_industry) == 6:
        user_industry = "Tech"
    elif int(social_media_industry) == 7:
        user_industry = "Travel & Tourism"
    elif int(social_media_industry) == 8:
        user_industry = "Finance"
    elif int(social_media_industry) == 9:
        user_industry = "Hospitality"
    else:
        print("stupid")
    
    return user_industry

industry_indetifier()

print(f"\nYou are in the {user_industry}")