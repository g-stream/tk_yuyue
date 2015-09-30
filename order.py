# -*- coding: utf-8 -*-
import requests
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
from lxml import etree
import re
import os
from io import BytesIO
import datetime
import time
class Order():
    s = requests.Session()
    sample_data = {'2': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '3': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '5': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '9': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '7': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '8': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '4': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '0': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '1': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225], '6': [225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 0, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 225, 225, 0, 0, 225, 225, 225, 0, 0, 0, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 0, 0, 0, 0, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225, 225]}
    account = '213132445'
    password = 'zcqc0073'
    phone = '15651930010'

    login_url        = "http://ids1.seu.edu.cn/amserver/UI/Login"
    login_im_url     = "http://ids1.seu.edu.cn/amserver/verify/image.jsp"
    login_check_url  = "http://ids1.seu.edu.cn/amserver/verify/check.jsp"
    main_url         = 'http://yuyue.seu.edu.cn/eduplus/order/initOrderIndex.do?sclId=1'

    yuyue_judgeorder_url = 'http://yuyue.seu.edu.cn/eduplus/order/order/judgeOrder.do?sclId=1'
    yuyue_im_url     = 'http://yuyue.seu.edu.cn/eduplus/control/validateimage'
    yuyue_judge_url  = 'http://yuyue.seu.edu.cn/eduplus/order/order/order/judgeUseUser.do?sclId=1'
    yuyue_insert_url = 'http://yuyue.seu.edu.cn/eduplus/order/order/order/insertOredr.do?sclId=1'

    my_order_url     = 'http://yuyue.seu.edu.cn/eduplus/order/fetchMyOrders.do?sclId=1'
    fresh_url        = 'http://yuyue.seu.edu.cn/eduplus/order/order/getOrderInfo.do?sclId=1'


    check_data = {'inputCode' :  ''}
    login_data = {'IDButton'  :  'Submit',
                  'IDToken0'  :  '',
                  'IDToken1'  :  account,
                  'IDToken2'  :  password,
                  'goto'      :  main_url,
                  'gx_charset':  'gb2312'}

    yuyue_judgeorder_data = {'dayInfo'  :'',
                             'itemId'   :'10',
                             'time'     :''}
    yuyue_judge_data = {'allowHalf'     : '2',
                        'ids'           : '13486,',
                        'itemId'        : '10',
                        'useTime'       : '',
                        'validateCode'  : ''}
    yuyue_insert_data = {'orderVO.itemId'   :  '10',
                         'orderVO.phone'    :  phone,
                         'orderVO.remark'   :  '',
                         'orderVO.useMode'  :  '2',
                         'orderVO.useTime'  :  '',
                         'useUserIds'       :  '13486',
                         'validateCode'     :  ''}

    accept_time = ['09:00-10:00','10:00-11:00','11:00-12:00','12:00-13:00',
                   '13:00-14:00','14:00-15:00','15:00-16:00','16:00-17:00',
                   '17:00-18:00','18:00-19:00','19:00-20:00','20:00-21:00']

    def __init__(self):
        pass
    def __processe_im(self, im):
        t = im.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(t)
        t = enhancer.enhance(8)
        t = t.convert('L')
        return t.point(lambda i:i>70 and 225)

    def __flaten_im(self, im):
        list = []
        for i in range(20):
            list.extend([im.getpixel((k,i)) for k in range(13)])
        return list
    def __im_crop_and_processing_and_flaten(self, im):
        return [self.__flaten_im(self.__processe_im(im.crop(((4+13*k),0,(17+13*k),20)))) for k in range(4)]
    def __score_of_list(self, list1, list2):
        return sum([int(list1[i]==list2[i]) for i in range(len(list1))])

    def __max_value(self, test, sample):
        m = 0
        for k,v in sample.items():
            if self.__score_of_list(v,test)>m:
                out = k
                m =self.__score_of_list(v,test)
        return out
    def __value(self, im):
        a = [self.__max_value(i,self.sample_data) for i in self.__im_crop_and_processing_and_flaten(im)]
        b = ''
        for i in a:
            b = b+i
        return b


    def validatecode_get(self, url):
        a = time.time()
        im_get = self.s.get(url)
        im = Image.open(BytesIO(im_get.content))
        print('处理图片用时',time.time()-a)
        validatecode = self.__value(im)
        self.validatecode = validatecode
        print('验证码是: '+validatecode)
        return validatecode


    def login(self):
        self.check_data['inputCode'] = self.validatecode_get(self.login_im_url)
        #验证码验证
        print(self.check_data)
        print(self.login_data)
        self.s.post(self.login_check_url,data = self.check_data)
        self.s.post(self.login_url,data = self.login_data)


    def time_gen(self,time):
        return self.accept_time[time-9]
    def date_gen(self,datedelta):
        return (datetime.datetime.today()+datetime.timedelta(days=datedelta)).strftime("%Y-%m-%d")
    def datetime_gen(self,datedelta, time):
        return self.date_gen(datedelta) + ' ' + self.time_gen(time)


    def order(self, datedelta=2, time=20):
        self.yuyue_judgeorder_data['dayInfo'] = self.date_gen(datedelta = datedelta)
        self.yuyue_judgeorder_data['order_time'] = self.time_gen(time = time)
        self.yuyue_judge_data['useTime'] = self.yuyue_insert_data['orderVO.useTime'] = self.datetime_gen(datedelta=datedelta, time=time)
        self.s.post(self.yuyue_judgeorder_url,data = self.yuyue_judgeorder_data)
        self.yuyue_judge_data['validateCode'] = self.yuyue_insert_data['validateCode'] = self.validatecode_get(self.yuyue_im_url)
        print(self.yuyue_judge_data)
        print(self.yuyue_insert_data)
        self.s.post(self.yuyue_judge_url, data = self.yuyue_judge_data)
        self.s.post(self.yuyue_insert_url, data = self.yuyue_insert_data)


    def __fresh_html_processing(self, html):
        tree = etree.fromstring(html,etree.HTMLParser())
        item = tree.xpath("//div[@class='time-item']")
        process1 = [[i.xpath("./em[@class='time']/text()")[0],i.xpath("./em[@class='time2']")[0].xpath('string(.)')] for i in item]
        d = {}
        for i in process1:
            re1 = re.search("\d{2}:\d{2}-\d{2}:\d{2}",i[0])
            re2 = re.search('(\d).*(\d)',i[1],re.S)
            d[re1.group(0)]=(str(int(re2.group(2))-int(re2.group(1)))+'/'+re2.group(2))
        return d
    def remain(self):
        fresh_data_list = [[{'dayInfo'   :(datetime.datetime.today()+datetime.timedelta(days=i)).strftime("%Y-%m-%d"),
                               'itemId'    :'10',
                               'pageNumber':str(k)} for k in [1,2]] for i in range(3)]
        fresh_html_list = [[self.s.post(self.fresh_url,i).text for i in k] for k in fresh_data_list]
        out = []
        for i in fresh_html_list:
            d1 = self.__fresh_html_processing(i[0])
            d2 = self.__fresh_html_processing(i[1])
            d = {}
            for k,v in (list(d1.items()) + list(d2.items())):
                d[k] = v
            out.append(d)
        return out
