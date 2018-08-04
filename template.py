#import argparse
#import os
#import sys
#import pandas as pd
#this is fork
import time
from instabot import Bot
#from instabot.bot.bot_like import limits

hashtags = ['music', 'song', 'permormance', 'inspiration', 'cover', 'live', 'guitar', 'piano', 'acapella']

bot = Bot(#whitelist_file=False,
          #blacklist_file=False,
          #comments_file=False,
          proxy=None,
          max_likes_per_day=2000,
          max_unlikes_per_day=10,
          max_follows_per_day=500,
          max_unfollows_per_day=1000,
          max_comments_per_day=0,
          max_blocks_per_day=0,
          max_unblocks_per_day=0,
          max_likes_to_like=100,
          filter_users=True,
          max_followers_to_follow=1000,
          min_followers_to_follow=100,
          max_following_to_follow=10000,
          min_following_to_follow=100,
          max_followers_to_following_ratio=10,
          max_following_to_followers_ratio=2,
          min_media_count_to_follow=3,
          max_following_to_block=500,
          like_delay=30,
          unlike_delay=30,
          follow_delay=30,
          unfollow_delay=30,
          comment_delay=30,
          block_delay=30,
          unblock_delay=30,
          stop_words=('shop', 'store', 'free'),
          verbosity=True
         )
bot.login(username='your_account',
          password='your_password',
          proxy=None)

#set variable to 1 for follow
go_follow = 1
wait_for_follow = 0
user_id = bot.get_user_id_from_username('your_account')
following = len(bot.get_user_following(user_id=user_id))
if following>7000:
    go_follow = 0
for i in range(1, 10000001):
    try:
        #if we have less than 7k following go ahead and follow more
        if go_follow==1:
            print('GOING TO FOLLOW')
            for h in hashtags:
                users = bot.get_hashtag_users(h)
                bot.follow_users(users)
            following = len(bot.get_user_following(user_id=user_id))
            if following>7000:
                go_follow = 0
                wait_for_follow = 0
            #print('SLEEPING 2 HOURS')
            #time.sleep(2*60*60)
        #else we unfollow
        else:
            #we wait for 7 days minimum before unfollow
            wait_for_follow = wait_for_follow+1
            if wait_for_follow>-1:
                print('GOING TO UNFOLLOW')
                bot.unfollow_everyone()
                #print('SLEEPING 2 HOURS')
                #time.sleep(2*60*60)
                following = len(bot.get_user_following(user_id=user_id))
                if following<100:
                    go_follow = 1
                    wait_for_follow = 0
        for h in hashtags:
            bot.like_hashtag(h)
        #print('SLEEPING 2 HOURS')
        print('UNFOLLOW ITERATIONS IS', wait_for_follow)
        #time.sleep(2*60*60)
    except Exception as e:
        print(e)
    finally:
        #limits.reset_counters(bot)
        bot.print_counters()