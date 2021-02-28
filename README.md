# instabot
:warning:FAILED
Python script for automating Instagram interactions(follow, unfollow and like) using InpstPy.\
The main objective is to gain followers.

## Requirements
In order to run the script you need to clone the repo, and run:
```shell
pip3 install -r requirements.txt
```
After that, you need to set your Instagram username and password as `INSTA_USERNAME` and `INSTA_PASSWORD` environment variables. You also can set them in config.env file inside the config folder.
```shell
python3 instabot.py
```
Optionally you can set a list of `ignoreAccounts`, `favoriteAccounts`, `dontLikeAccounts` and `keywordBlacklist`
in the data.json file in config folder to customize the script. 

