print("Welcome to Insta-Assitant\n")

print("Where we help your business reach more followers and create a buget for you.\n")

name = input("Please enter your name:")

print(f"\n Hello {name} ")

print("Instgram industry \n 1.Healthcare \n 2.Media \n 3.Education \n 4.Nonprofit \n 5.Restaurants \n 6.Tech \n 7.Travel & Tourism \n 8.Finance \n 9.Hospitality ")


def get_user_industry():
    global social_media_industry
    
    global user_industry_selected

    while True:
        social_media_industry = input("\n Please enter which  number represents your industry:")
        try:          
            user_industry_selected = int(social_media_industry)
            
            if type(user_industry_selected) != int:
                raise ValueError(
                    f"Exactly 6 values required, you provided {user_industry_selected}"
                    )
                    
            elif user_industry_selected > 9:
                raise ValueError(
                    f"Exactly 6 values required, you provided {user_industry_selected}"
                    )
            elif user_industry_selected < 1:
                raise ValueError(
                    f"Exactly 6 values required, you provided {user_industry_selected}"
                    )
            else:
                break                    
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

    return user_industry_selected


health_care = {
    "industry": "Healthcare",
    "best time to post": ["Sunday: 8–9 a.m.", "Tuesday: 8 a.m.–noon", " Tuesday: 5–8 p.m."],
    "Best day": "Monday, Tuesday",
    "hashtags": "#HealthCare",
}

media = {
    "industry": "Media",
    "best time to post": ["Tuesday: 1–5 p.m.", "Wednesday: 11 a.m", "Thursday: 8–9 a.m."],
    "Best day": "Tuesday, Wednesday, Thursday",
    "hashtags": "#media",
}

education = {
    "industry": "Education",
    "best time to post": ["Friday: 4–5 a.m.", "Thursday: 2 p.m."],
    "Best day": "Friday",
    "hashtags": "#education",
    }

nonprofit = {
    "industry": "Nonprofit",
    "best time to post": ["Wednesday: 10 a.m.–6 p.m."],
    "Best day": "Wednesday",
    "hashtags": "#nonprofit",
    }

restaurants = {
    "industry": "Restaurants",
    "best time to post": ["Monday: 9 a.m.–1 p.m."],
    "Best day": "Monday",
    "hashtags": "#restaurants",
    }

tech = {
    "industry": "Tech",
    "best time to post": ["Monday: 10–11 a.m.", "Monday: 2–5 p.m.", "Monday: 8 p.m.", "Tuesday: 10 a.m.–1 p.m", "Thursday: noon", "Friday: 11 a.m"],
    "Best day": "Monday",
    "hashtags": "#Tech",
    }

travel_and_tourism = {
    "industry": "Travel & Tourism",
    "best time to post": ["Monday: 11 a.m–3 p.m.", "Thursday: 9 a.m.–1 p.m.", " Friday: 10 a.m.–noon"],
    "Best day": "Thursday",
    "hashtags": "#education",
    }

finance = {
    "industry": "Finance",
    "best time to post": ["Monday: 5 p.m.", "Wednesday: 9 a.m.–1 p.m.", " Friday: 11 a.m."],
    "Best day": "Wednesday",
    "hashtags": "#education",
    }

hospitality = {
    "industry": "Hospitality",
    "best time to post": ["Wednesday: noon", "Thursday : 3–4 p.m.", "Friday: 8 a.m.–noon"],
    "Best day": "Friday",
    "hashtags": "#education",
    }


def industry_indetifier():
    global user_industry
    user_industry = ""

    if user_industry_selected == 1:
        user_industry = health_care
    elif user_industry_selected == 2:
        user_industry = media
    elif user_industry_selected == 3:
        user_industry = education
    elif user_industry_selected == 4:
        user_industry = nonprofit
    elif social_media_industry == 5:
        user_industry = restaurants
    elif social_media_industry == 6:
        user_industry = tech
    elif social_media_industry == 7:
        user_industry = travel_and_tourism
    elif social_media_industry == 8:
        user_industry = finance
    elif social_media_industry == 9:
        user_industry = hospitality
    else:
        print("stupid")
    
    return user_industry


def get_users_followers():
    global user_followers
    user_followers = input("\nEnter how many followers you have:\n")


def get_users_sales_goals():
    campaign_reach = input("\nEnter number of sales you would like to make from this campaign:")


def type_of_hashtag_to_use():
    global hashtags
    hashtags = ""
    if int(user_followers) <= 10000:
        hashtags = "niche"
    elif int(user_followers) <= 100000:
        hashtags = "big time"
    elif int(user_followers) <= 1000000:
        hashtags = "superstar"
    elif int(user_followers) <= 10000000:
        hashtags = "cr7"
    elif int(user_followers) <= 100000000:
        hashtags = "kardashian"
    elif int(user_followers) <= 500000000:
        hashtags = "mj"
    else:
        print("wtf")
    
    return hashtags   


def main():
    get_user_industry()
    industry_indetifier()
    get_users_followers()
    get_users_sales_goals()
    type_of_hashtag_to_use()


main()

print(f"you should use these type of hashtags {hashtags}")
print(user_industry)
