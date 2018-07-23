# -*- coding: utf-8 -*-
from flask import Blueprint


douyin = Blueprint('douyin', __name__, url_prefix='/douyin')

from loach.api import douyinview