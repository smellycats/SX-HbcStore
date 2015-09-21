from hbc import app, views
from ini_conf import MyIni

if __name__ == '__main__':
    my_ini = MyIni('my_ini.conf')
    s_ini = my_ini.get_sys()
    h_ini = my_ini.get_hzhbc()
    app.config['SECRET_KEY'] = s_ini['secret_key']
    app.config['EXPIRES'] = s_ini['expires']
    app.config['WHITE_LIST_OPEN'] = s_ini['white_list_open']
    app.config['WHITE_LIST'] = set(s_ini['white_list'].split(','))
    app.config['SQLALCHEMY_BINDS'] = {
        'hz_hbc': 'mysql://%s:%s@%s:%s/%s' % (h_ini['username'],
                                              h_ini['password'],
                                              h_ini['host'], h_ini['port'],
                                              h_ini['db'])
    }
    app.run(port=8098, threaded=True)
