print("............................................................")

print("Welcome to Insta-Assitant\n")

print("Your instagram campaign assistant.\n")

print("............................................................")

name = input("Please enter your name:")

health_care = {
    "industry": "Healthcare",
    "best time to post": ["Tuesday: 8 a.m.–noon", " Tuesday: 5–8 p.m."],
    "Best day": "Monday and Tuesday",
    "hashtags": "#HealthCare",
}

media = {
    "industry": "Media",
    "best time to post": ["Tuesday: 1–5 p.m.", "Wednesday: 11 a.m"],
    "Best day": "Tuesday and  Wednesday",
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
    "best time to post": ["Monday: 10–11 a.m.", "Tuesday: 10 a.m.–1 p.m"],
    "Best day": "Monday",
    "hashtags": "#Tech",
    }

travel_and_tourism = {
    "industry": "Travel & Tourism",
    "best time to post": ["Monday: 11 a.m–3 p.m.", "Thursday: 9 a.m.–1 p.m."],
    "Best day": "Thursday",
    "hashtags": "#education",
    }

finance = {
    "industry": "Finance",
    "best time to post": ["Monday: 5 p.m.", "Wednesday: 9 a.m.–1 p.m."],
    "Best day": "Wednesday",
    "hashtags": "#education",
    }

hospitality = {
    "industry": "Hospitality",
    "best time to post": ["Wednesday: noon", "Friday: 8 a.m.–noon"],
    "Best day": "Friday",
    "hashtags": "#education",
    }

print(f"\n Hello {name} ")

print("Instgram industry \n 1.Healthcare \n 2.Media\
    \n 3.Education \n 4.Nonprofit \n 5.Restaurants \n 6.Tech\
    \n 7.Travel & Tourism \n 8.Finance \n 9.Hospitality ")


def get_user_industry():
    """
    This function takes the input for the user
    to so select which industry they belong to
    """
    global social_media_industry
    global user_industry_selected

    while True:
        social_media_industry = input(
            "\n Please enter which  number represents your industry:\n"
            )
        try:
            user_industry_selected = int(social_media_industry)
            if type(user_industry_selected) != int:
                raise ValueError(
                    "Enter a number from the list, you provided"
                    f"- '{user_industry_selected}'"
                    )
            elif user_industry_selected > 9:
                raise ValueError(
                    "Enter only a number that is from the list, you provided"
                    f"- '{user_industry_selected}'"
                    )
            elif user_industry_selected < 1:
                raise ValueError(
                    "Enter a number between 1 and 9, you provided"
                    f"-'{user_industry_selected}'"
                    )
            else:
                break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

    return user_industry_selected


def industry_indetifier():
    """
    This function  matches the input of the users industry,
    to which object/industry it is in
    """
    global user_industry
    user_industry = "Empty str"

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

    return user_industry


def get_users_followers():
    """
    This takes an input for how man followers the user has,
    it also has a validator to ensure an integer is entered and that
    the user enters amount no less that zero and no higher than
    the highest instagram profile
    """
    global user_followers

    while True:
        user_followers = input("\nEnter how many followers you have:\n")

        try:
            user_follower_entry = int(user_followers)

            if type(user_follower_entry) != int:
                raise ValueError(
                    "Please enter a number, you provided"
                    f"-'{user_follower_entry}'"
                    )
            elif user_follower_entry < 0:
                raise ValueError(
                    "You can't have negative followers, you provided"
                    f"-'{user_follower_entry}'"
                    )
            elif user_follower_entry > 388000000:
                raise ValueError(
                    "Exceeded highest followers, you provided"
                    f"-'{user_follower_entry}'"
                    )
            else:
                break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

    return user_follower_entry


def get_users_sales_goals():
    """
    This takes aninput for how man sales
    the user wants to make from their campaign.
    It also has a validator to ensure an integer is entered and that
    the user enters amount no less that zero and no higher than
    the highest instagram profile
    """
    global campaign_reach

    while True:
        campaign_reach = input("\nEnter sales target:\n")

        try:
            users_sales_entery = int(campaign_reach)

            if type(users_sales_entery) != int:
                raise ValueError(
                    "Please enter a number, you provided"
                    f"-'{users_sales_entery}'"
                    )
            elif users_sales_entery < 133:
                raise ValueError(
                    "A minimum requirement of 133 is required, you provided"
                    f"-'{users_sales_entery}'"
                    )
            else:
                break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

    return users_sales_entery


def ad_duration():
    """
    This takes a validated input for how long the campaign will last.
    It also has a validator to ensure an integer is entered and that
    the user enters amount no less that zero.
    """
    global duration

    while True:
        duration = input("\nEnter number of days the campaign will last:\n")

        try:
            users_duration_entery = int(duration)

            if type(users_duration_entery) != int:
                raise ValueError(
                    "Please enter a number, you provided"
                    f"-'{user_industry_selected}'"
                    )
            elif users_duration_entery <= 0:
                raise ValueError(
                    "Please enter a number from 1 or higher, you provided"
                    f"-'{user_industry_selected}'"
                    )
            else:
                break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

    return users_duration_entery


def cost_calculation():
    """
    Calculates how much the user will need to spend in order to
    meet their sales target. It multiplies the sales target of the user
    by 1.25 as it is projected that only 25% of ads are successful.
    """
    global total_cost
    campaign_reach_needed = int(campaign_reach) * 1.25
    total_cost = campaign_reach_needed * 1.33

    return total_cost


def average_cost():
    """
    Calculates how much the user will need to spend on average per day on ad
    """
    global average_cost_per_day
    average_cost_per_day = total_cost / int(duration)

    return average_cost_per_day


def type_of_hashtag_to_use():
    global hashtags
    hashtags = ""
    if int(user_followers) <= 10000:
        hashtags = "Use niche has tags that are not so popular"
    elif int(user_followers) <= 100000:
        hashtags = "Use tags that are semi-popular"
    elif int(user_followers) <= 1000000:
        hashtags = "Use popular tags"

    return hashtags


def main():
    """
    This is the storage for all the functions
    """
    get_user_industry()
    industry_indetifier()
    get_users_followers()
    get_users_sales_goals()
    type_of_hashtag_to_use()
    cost_calculation()
    ad_duration()
    average_cost()


main()

best_day = user_industry["Best day"]

best_time = user_industry["best time to post"]

example_hashtags = user_industry["hashtags"]

user_industry = user_industry["industry"]

print(f"\nYour profile is in this industry: {user_industry}")

print(f"\nYou currently have:{user_followers} followers")

print(f"\nThese hashtags will give you the best exposure: {hashtags}")

print(f"\nAn example of a hashtag to use: {example_hashtags }")

print(f"\nThe best day to run youd is: {best_day}")

print(f"\nThe best times to run your is: {best_time}")

print(f"\nYour campaign will last {duration } days")

print(f"\nYour average per day cost will be: {average_cost_per_day} Dollars")

print(f"\nYour Total cost: {total_cost} Dollars in total")

print(f"We look forward to your success {name}")
