# -*- coding: utf-8 -*-

# from celery import Celery
# from loach.setting import config
# celery = Celery()
# celery.config_from_object(config['CELERY'])
#
# @celery.task(
#     name='weibo.articles.crawl.one',
#     autoretry_for=(requests.ConnectionError, requests.Timeout),
#     retry_kwargs={
#         'max_retries': 1,
#         'countdown': 0.5
#     },
#     ignore_result=True
# )
# def fuck_it(){
#
# }
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + "\\..\\..\\")
import pika
import sys
import json
import datetime
from sqlalchemy import create_engine
from loach.model.douyinaccount import DouYinAccount
from loach.model.douyinfollowrelation import DouYinFollowRelation
from loach.model.douyinlikerelation import DouYinLikeRelation
from loach.model.douyinvideo import DouYinVideo
from loach.model.douyincomment import DouComment
from json.decoder import JSONDecodeError

con = pika.BlockingConnection(pika.ConnectionParameters(host='...', port=5672, virtual_host='/', credentials=pika.PlainCredentials('', '')))
channel = con.channel()

engine = create_engine("p")
engine.connect()


binding_keys = [
    # routing_key       queue_name
    'douyin.author.#', 'douyin.author'
]


def douyin_author_post(body):
    data = json.loads(body.decode('utf-8'))
    videos = data['aweme_list']
    for video in videos:
        video_cleared = {
            'user_id': str(video['author_user_id']),
            'short_id': video['author']['short_id'],
            'video_id': video['aweme_id'],
            'cover': video['video']['cover']['url_list'][0],
            'description': video['desc'],
            'comment_count': video['statistics']['comment_count'],
            'share_count': video['statistics']['share_count'],
            'like_count': video['statistics']['digg_count'],
            'play_count': video['statistics']['play_count'],
            'share_url': video['share_info']['share_url'],
            # 'age':
            'status': 0,
            'video_create_time': datetime.datetime.fromtimestamp(video['create_time'])
        }
        for play_url in video['video']['play_addr']['url_list']:
            if play_url.find('aweme.snssdk') > 0:
                video_cleared['play_url'] = play_url
                break
        DouYinVideo.upsert(**video_cleared)
    return 'OK'


def douyin_author_feed(body):
    data = json.loads(body.decode('utf-8'))
    videos = data['aweme_list']
    for video in videos:
        video_cleared = {
            'user_id': str(video['author_user_id']),
            'short_id': video['author']['short_id'],
            'video_id': video['aweme_id'],
            'cover': video['video']['cover']['url_list'][0],
            'description': video['desc'],
            'comment_count': video['statistics']['comment_count'],
            'share_count': video['statistics']['share_count'],
            'like_count': video['statistics']['digg_count'],
            'play_count': video['statistics']['play_count'],
            'share_url': video['share_info']['share_url'],
            # 'age':
            'status': 0,
            'video_create_time': datetime.datetime.fromtimestamp(video['create_time'])
        }
        for play_url in video['video']['play_addr']['url_list']:
            if play_url.find('aweme.snssdk') > 0:
                video_cleared['play_url'] = play_url
                break
        DouYinVideo.upsert(**video_cleared)
    return 'OK'


def douyin_author_following(body):
    response = json.loads(body.decode('utf-8'))
    authors_info = response['followings']
    uid = response['uid']
    for author_info in authors_info:
        author_info_cleared = {
            'user_id': str(author_info.get('uid')),
            'description': author_info.get('signature'),
            'nickname': author_info.get('nickname'),
            'short_id': author_info.get('short_id'),
            # 'douyin_id': author_info.get('unique_id'),
            'avatar': author_info['avatar_thumb']['url_list'][0],
            'verification_type': author_info.get('verification_type'),
            'birthday': author_info.get('birthday'),
            # 'age':
            'sex': author_info.get('gender'),
            'region': author_info.get('region'),
            'account_create_time': datetime.datetime.fromtimestamp(author_info.get('create_time', 0))
        }
        if 2 == author_info_cleared['verification_type']:
            author_info_cleared['verification'] = '抖音音乐人'
        DouYinAccount.upsert(**author_info_cleared)
        if not DouYinFollowRelation.exists(user_id=author_info_cleared['user_id'], follower_id=uid):
            DouYinFollowRelation.add(user_id=author_info_cleared['user_id'], follower_id=uid)
    return "OK"


def douyin_author_info(body):
    author_info = json.loads(body.decode('utf-8'))['user']
    author_info_cleared = {
        'user_id': str(author_info.get('uid')),
        'description': author_info.get('signature'),
        'nickname': author_info.get('nickname'),
        'short_id': author_info.get('short_id'),
        # 'douyin_id': author_info.get('unique_id'),
        'avatar': author_info['avatar_thumb']['url_list'][0],
        'verification': author_info.get('custom_verify'),
        'birthday': author_info.get('birthday'),
        # 'age':
        'sex': author_info.get('gender'),
        'region': author_info.get('location'),
        'like_count': author_info.get('favoriting_count'),
        'video_count': author_info.get('aweme_count'),
        'liked_count': author_info.get('total_favorited'),
        'music_count': author_info['original_musician']['music_count'],
        'music_like_count': author_info['original_musician']['digg_count'],
        'music_used_count': author_info['original_musician']['music_used_count'],
        'following_num': author_info.get('following_count'),
        'follower_num': author_info.get('follower_count'),
    }
    if author_info_cleared['verification'].find("音乐人") >= 0:
        author_info_cleared['verification_type'] = 2
    DouYinAccount.upsert(**author_info_cleared)
    return "OK"


def douyin_author_favorite(body):
    data = json.loads(body.decode('utf-8'))
    videos = data['aweme_list']
    uid = data['uid']
    for video in videos:
        video_cleared = {
            'user_id': str(video['author_user_id']),
            'short_id': video['author']['short_id'],
            'video_id': video['aweme_id'],
            'cover': video['video']['cover']['url_list'][0],
            'description': video['desc'],
            'comment_count': video['statistics']['comment_count'],
            'share_count': video['statistics']['share_count'],
            'like_count': video['statistics']['digg_count'],
            'play_count': video['statistics']['play_count'],
            'share_url': video['share_info']['share_url'],
            # 'age':
            'status': 0,
            'video_create_time': datetime.datetime.fromtimestamp(video['create_time'])
        }
        for play_url in video['video']['play_addr']['url_list']:
            if play_url.find('aweme.snssdk') > 0:
                video_cleared['play_url'] = play_url
                break

        DouYinVideo.upsert(**video_cleared)
        if not DouYinLikeRelation.exists(user_id=uid, video_id=video_cleared['video_id']):
            DouYinLikeRelation.add(user_id=uid, video_id=video_cleared['video_id'])
    return 'OK'


def douyin_author_follower(body):
    response = json.loads(body.decode('utf-8'))
    authors_info = response['followings']
    uid = response['uid']
    for author_info in authors_info:
        author_info_cleared = {
            'user_id': str(author_info.get('uid')),
            'description': author_info.get('signature'),
            'nickname': author_info.get('nickname'),
            'short_id': author_info.get('short_id'),
            # 'douyin_id': author_info.get('unique_id'),
            'avatar': author_info['avatar_thumb']['url_list'][0],
            'verification_type': author_info.get('verification_type'),
            'birthday': author_info.get('birthday'),
            # 'age':
            'sex': author_info.get('gender'),
            'region': author_info.get('region'),
            'account_create_time': datetime.datetime.fromtimestamp(author_info.get('create_time', 0))
        }
        if 2 == author_info_cleared['verification_type']:
            author_info_cleared['verification'] = '抖音音乐人'

        DouYinAccount.upsert(**author_info_cleared)
        if not DouYinFollowRelation.exists(user_id=uid, follower_id=author_info_cleared['user_id']):
            DouYinFollowRelation.add(user_id=uid, follower_id=author_info_cleared['user_id'])
    return "OK"


def douyin_author_comment(body):
    response = json.loads(body.decode('utf-8'))
    comments_info = response['comments']
    for comment_info in comments_info:
        comment_info_cleared = {
            'user_id': str(comment_info['user']['uid']),
            'text': comment_info['text'],
            'nickname': comment_info['user']['nickname'],
            'short_id': comment_info['user']['short_id'],
            'video_id': comment_info['aweme_id'],
            'reply_id': comment_info['reply_id'],
            'comment_id': comment_info['cid'],
            'like_count': comment_info['digg_count'],
            'status': comment_info['status'],
            'comment_create_time': datetime.datetime.fromtimestamp(comment_info['create_time'])
        }

        if not DouComment.exists(comment_info_cleared['comment_id']):
            DouComment.add(**comment_info_cleared)
    return "OK"


routing_tasks = {
    'douyin.author.post': douyin_author_post,
    'douyin.author.feed': douyin_author_feed,
    'douyin.author.following': douyin_author_following,
    'douyin.author.follower': douyin_author_follower,
    'douyin.author.info': douyin_author_info,
    'douyin.author.favorite': douyin_author_favorite,
    'douyin.author.comment': douyin_author_comment
}

# channel.queue_bind(exchange="DouYin", queue="douyin.author", routing_key='douyin.author.#',)


def cb(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    task = routing_tasks.get(method.routing_key, None)
    if task and callable(task):
        try:
            r = task(body)
        except (KeyError, IndexError, JSONDecodeError):
            # 这些报错说明都因返回的数据格式不对，可以直接抛弃
            r = "OK"
        if r == 'OK':
            print("13123123", method.routing_key)
            ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=10)
channel.basic_consume(cb, queue="douyin.author")

channel.start_consuming()
