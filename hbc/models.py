# -*- coding: utf-8 -*-
import arrow

from hbc import db


class Users(db.Model):
    """用户"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True)
    password = db.Column(db.String(128))
    scope = db.Column(db.String(128), default='')
    date_created = db.Column(db.DateTime, default=arrow.now().datetime)
    date_modified = db.Column(db.DateTime, default=arrow.now().datetime)
    banned = db.Column(db.Integer, default=0)

    def __init__(self, username, password, scope='', banned=0,
                 date_created=None, date_modified=None):
        self.username = username
        self.password = password
        self.scope = scope
        now = arrow.now().datetime
        if not date_created:
            self.date_created = now
        if not date_modified:
            self.date_modified = now
        self.banned = banned

    def __repr__(self):
        return '<Users %r>' % self.id


class Scope(db.Model):
    """权限范围"""
    __tablename__ = 'scope'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Scope %r>' % self.id


class Hbc(db.Model):
    """黄标车信息"""
    __tablename__ = 'hbc'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    jgsj = db.Column(db.DateTime)
    hphm = db.Column(db.String(12), default='-')
    kkdd_id = db.Column(db.String(9))
    hpys_code = db.Column(db.String(2))
    fxbh_code = db.Column(db.String(2))
    cdbh = db.Column(db.Integer)
    imgurl = db.Column(db.String(256))
    imgpath = db.Column(db.String(256))
    banned = db.Column(db.Integer, default=0)

    def __init__(self, date, jgsj, hphm='-', kkdd_id='441301001', hpys_code='QT',
                 fxbh_code='QT', cdbh=1, imgurl='', imgpath='', banned=0):
        self.date = date
        self.jgsj = jgsj
        self.hphm = hphm
        self.kkdd_id = kkdd_id
        self.hpys_code = hpys_code
        self.fxbh_code = fxbh_code
        self.cdbh = cdbh
        self.imgurl = imgurl
        self.imgpath = imgpath
        banned = banned

    def __repr__(self):
        return '<Hbc %r>' % self.id


class Kkdd(db.Model):
    """卡口地点"""
    __tablename__ = 'kkdd'
    kkdd_id = db.Column(db.String(9), primary_key=True)
    kkdd_name = db.Column(db.String(64))
    cf_id = db.Column(db.String(3))
    sbdh = db.Column(db.String(128))
    banned = db.Column(db.Integer, default=0)

    def __init__(self, kkdd_id, kkdd_name, cf_id, sbdh, banned=0):
        self.kkdd_id = kkdd_id
        self.kkdd_name = kkdd_name
        self.cf_id = cf_id
        self.sbdh = sbdh
        self.banned = banned

    def __repr__(self):
        return '<Kkdd %r>' % self.kkdd_id


class WZImg(db.Model):
    """黄标车违章标志图片"""
    __tablename__ = 'hbc_img'
    id = db.Column(db.Integer, primary_key=True)
    kkdd_id = db.Column(db.String(9))
    fxbh_code = db.Column(db.String(2))
    img_path = db.Column(db.String(128))

    def __init__(self, kkdd_id, fxbh_code, img_path):
        self.kkdd_id = kkdd_id
        self.fxbh_code = fxbh_code
        self.img_path = img_path

    def __repr__(self):
        return '<WZImg %r>' % self.id


class WhiteList(db.Model):
    __tablename__ = 'white_list'
    id = db.Column(db.Integer, primary_key=True)
    hphm = db.Column(db.String(16))
    banned = db.Column(db.Integer, default=0)

    def __init__(self, hphm, banned=0):
        self.hphm = hphm
        self.banned = banned

    def __repr__(self):
        return '<WhiteList %r>' % self.id
    
