# -*- coding: utf-8 -*-
import arrow

from hbc import db
from hbc.models import Users, Scope, Hbc, Kkdd

def test_scope_get():
    scope = Scope.query.all()
    for i in scope:
        print i.name

def test_user_get():
    user = Users.query.filter_by(username='admin', banned=0).first()
    print user.scope

    
def test_hbc_get():
    hbc = Hbc.query.first()
    print hbc.hphm, hbc.kkdd_id

def test_hbc_add():
    datetime = '2013-05-11 21:23:58'
    t = arrow.get(datetime).replace(hours=-8)
    hbc = Hbc(date=t.format('YYYY-MM-DD'), jgsj=t.datetime, hphm='粤L12345',
              kkdd_id='441302002', hpys_code='BU', fxbh_code='IN', cdbh=5,
              imgurl='httP;//123', imgpath='c:123', banned=0)
    db.session.add(hbc)
    db.session.commit()
    print hbc.id

def test_hbcimg_get():
    hbc = Hbc.query.filter(Hbc.date=='2013-05-11 21:23:58',
                           Hbc.hphm=='粤L12345',
                           Hbc.kkdd_id.startswith('441302002'),
                           Hbc.imgpath != '').all()
    print hbc

def test_kkdd():
    kkdd = Kkdd.query.filter(Kkdd.kkdd_id.startswith('441302001')).all()
    print kkdd

if __name__ == '__main__':
    #hpys_test()
    #hbc_add()
    #test_scope_get()
    #test_user_get()
    #test_hbc_get()
    #test_hbc_add()
    #test_hbcimg_get()
    test_kkdd()



