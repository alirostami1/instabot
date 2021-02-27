# imports
from instapy import InstaPy
from instapy import smart_run
import os
import random
from dotenv import load_dotenv
import json
import time

# ==================================================
# Load data:

# Load ENV from .env file
load_dotenv("config/config.env")

# Load Data from .json file
with open('config/data.json') as jsonFile:
    data = json.load(jsonFile)

# Instagram Username an Password from ENV
instaUsername = os.getenv("INSTA_USERNAME")
instaPassword = os.getenv("INSTA_PASSWORD")

# List of Accounts to ignore having interactions with compeletly - from .json file
ignoreAccounts = data["ignoreAccounts"]

# List of Accounts that we are most Interested in Interacting with - from .json file
favoriteAccounts = data["favoriteAccounts"]

# Dont like these Accounts - from .json file
dontLikeAccounts = data["dontLikeAccounts"]

# Dont interact with posts if it Contains these Keywords - from .json file
keywordBlacklist = data["keywordBlacklist"]

session = InstaPy(username=instaUsername,
                password=instaPassword)

# get an InstaPy session!
while True:
    # login

    with smart_run(session):
        """ Activity flow """
        # --- general settings ---

        # ignore these users
        session.set_ignore_users(ignoreAccounts)
        # dont like these users
        session.set_dont_like(dontLikeAccounts)
        # dont interact with if contains keyword
        session.set_ignore_if_contains(keywordBlacklist)
        # enable simulation
        session.set_simulation(enabled=True, percentage=100)
        # only interact with post and accounts with persian and english letters in them
        session.set_mandatory_language(
            enabled=True, character_set=['LATIN', 'ARABIC'])
        # set boundries on who to interact with
        session.set_relationship_bounds(enabled=True,
                                        potency_ratio=None,
                                        delimit_by_numbers=True,
                                        max_followers=7500,
                                        max_following=5000,
                                        min_followers=25,
                                        min_following=25,
                                        min_posts=1)

        # only likes posts with min and max likes >
        session.set_delimit_liking(
            enabled=True, max_likes=3000, min_likes=None)
        # set delays between each action - to make it more human-like
        session.set_action_delays(
            enabled=True,
            like=30,
            comment=45,
            follow=45,
            unfollow=45,
            randomize=True,
            random_range_from=100,
            random_range_to=300)
        # set limit qouta
        session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                                     peak_likes_hourly=30,
                                     peak_likes_daily=200,
                                     peak_comments_hourly=0,
                                     peak_comments_daily=0,
                                     peak_follows_hourly=15,
                                     peak_follows_daily=200,
                                     peak_unfollows_hourly=15,
                                     peak_unfollows_daily=200,
                                     peak_server_calls_hourly=200,
                                     peak_server_calls_daily=None)
        # Interaction's law
        session.set_user_interact(amount=3, randomize=True, percentage=80,
                                  media='Photo')
        # Enalbe liking
        session.set_do_like(enabled=True, percentage=20)
        # Enable Following
        session.set_do_follow(enabled=True, percentage=30, times=1)

        # ===============================================================
        # --- Actions ---

        # Choosing a random account from favoriteAccount list
        number = random.randint(3, 5)
        random_targets = favoriteAccounts

        if len(favoriteAccounts) <= number:
            random_targets = favoriteAccounts
        else:
            random_targets = random.sample(favoriteAccounts, number)

        """ Interact with the chosen targets...
        """
        # Follow the randomly selected user from favoriteAccounts commenters
        session.follow_commenters(random_targets, amount=50,
                                  daysold=365, max_pic=100, sleep_delay=600, interact=True)

        time.sleep(3600)
        """ Unfollow nonfollowers after one day...
        """
        session.unfollow_users(amount=random.randint(75, 100),
                               nonFollowers=True,
                               style="FIFO",
                               unfollow_after=24 * 60 * 60, sleep_delay=600)
        time.sleep(1800)

        # Follow the randomly selected user from favoriteAccounts likers
        session.follow_likers(random_targets,
                              follow_likers_per_photo=100,
                              randomize=True, sleep_delay=600,
                              interact=True)
        time.sleep(1800)

        """ Unfollow all users followed by InstaPy after one week to keep the 
        following-level clean...
        """
        session.unfollow_users(amount=random.randint(75, 100),
                               allFollowing=True,
                               style="FIFO",
                               unfollow_after=96 * 60 * 60, sleep_delay=600)
        time.sleep(1800)

        """ Joining Engagement Pods...
        """
        session.join_pods()
