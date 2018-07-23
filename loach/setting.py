# -*- coding: utf-8 -*-
from kombu import Queue, Exchange, binding


def create_task_queues(binding_list):
    binding_map = {}
    exchange = Exchange('DouYin', type='topic')

    _queues = [
        Queue(
            'ocean:debug',
            [binding(exchange, routing_key='douyin.debug.#')],
            queue_arguments={'x-queue-mode': 'lazy'}
        )
    ]

    for routing_key, queue_name in binding_list:
        binding_map.setdefault(queue_name, [])
        binding_map[queue_name].append(routing_key)

    for queue_name, routing_keys in binding_map.items():
        _queues.append(
            Queue(
                'douyin:' + queue_name,
                [binding(exchange, routing_key=routing_key)
                 for routing_key in routing_keys],
                queue_arguments={'x-queue-mode': 'lazy'}
            )
        )
    return _queues


bindings = [
    ('douyin.author.#', 'douyin.author'),
    ('douyin.music.#', 'douyin.music'),
]
queues = create_task_queues(bindings)


def route_task(name, args, kwargs, options, task=None, **kw):
    return {
        'exchange': 'DouYin',
        'exchange_type': 'topic',
        'routing_key': name
    }

class ProductConfig(object):
    CACHE_REDIS_URL = 'redis://'

    # SQLALCHEMY_DATABASE_URI = 'postgresql://'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///douyin'
    # 公网地址: 'amqp:///'
    RABBITMQ_URL = 'amqp:///'

    CELERY = {
        'broker_url': RABBITMQ_URL,
        'broker_connection_timeout': 10.0,
        'broker_transport_options': {},
        'result_backend': CACHE_REDIS_URL,

        # 默认任务配置
        'task_default_queue': 'douyin:default',
        'task_default_exchange': 'DouYin',
        'task_default_exchange_type': 'topic',
        'task_default_routing_key': 'default',
        'task_default_delivery_mode': 'persistent',
        'task_track_started': True,

        # 发送端路由
        'task_queues': queues,
        'task_routes': (route_task, ),

        # 日志
        'worker_task_log_format': "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s",
        'worker_log_format': "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s",
    }


def obj2dict(obj):
    return {key: getattr(obj, key) for key in dir(obj) if key.isupper()}


config = obj2dict(ProductConfig)
