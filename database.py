import pymysql
from settings import config


def fetch(sql, params):
    print(sql)
    print(params)
    try:
        conn = pymysql.connect(**config)
        cur = conn.cursor()
        try:
            cur.execute(sql, params)
            desc = cur.description
            rows = cur.fetchall()
            fields = []
            for f in desc:
                fields.append(f[0])
            data = [tuple(fields), ]
            for d in rows:
                data.append(d)
            result = (tuple(data), None)
        except pymysql.Error as e:
            print(e)
            result = (((),), e)
        cur.close()
        conn.close()
    except pymysql.Error as e:
        print(e)
        result = (((),), e)
    return result


def affect(sql, params):
    print(sql)
    print(params)
    try:
        db = pymysql.connect(**config)
        cur = db.cursor()
        try:
            cur.execute(sql, params)
            db.commit()
            result = (cur.rowcount, '')
        except pymysql.Error as e:
            print(e)
            result = (cur.rowcount, e)
            db.rollback()
        cur.close()
        db.close()
    except pymysql.Error as e:
        print(e)
        result = (0, e)
    return result


def get_artists(name, surname, option, year_from, year_to):
    if option == 'singer':
        x = ' JOIN singer_prod ON ar_taut = tragoudistis '
    elif option == 'songwriter':
        x = ' JOIN tragoudi ON ar_taut = sinthetis '
    elif option == 'composer':
        x = ' JOIN tragoudi ON ar_taut = stixourgos '
    else:
        x = ' '

    sql = "SELECT distinct ar_taut AS 'National_ID', " \
          "onoma AS 'Name', epitheto AS 'Surname', " \
          "etos_gen AS 'Birth_Year' " \
          "FROM kalitexnis" + x + \
          "WHERE etos_gen " \
          "BETWEEN %s AND %s " \
          "AND (onoma LIKE %s OR onoma IS NULL) " \
          "AND epitheto LIKE %s " \
          "ORDER BY kalitexnis.onoma ASC, kalitexnis.epitheto ASC"
    return fetch(sql, [year_from, year_to, '%' + name + '%', '%' + surname + '%'])


def update_artist(id, name, surname, year):
    name = name if name != '' else None
    sql = """UPDATE `kalitexnis` SET `onoma`= %s , `epitheto`= %s, `etos_gen`= %s WHERE (`ar_taut`= %s)"""
    return affect(sql, [name, surname, year, id])


def delete_artist(id):
    sql = """DELETE FROM `kalitexnis` WHERE (`ar_taut`= %s)"""
    return affect(sql, [id, ])


def insert_artist(id, name, surname, year):
    sql = """INSERT INTO `kalitexnis` (`ar_taut`, `onoma`, `epitheto`, `etos_gen`) VALUES (%s, %s, %s, %s)"""
    return affect(sql, [id, name, surname, year])


def get_songs(title, year, company):
    params = ['%' + title + '%']
    if company != '':
        sp1 = " ,cp.etos AS `CD PRODUCTION`, cp.etaireia AS `CD COMPANY` "
        sp2 = " LEFT JOIN singer_prod sp ON sp.title = t.titlos LEFT JOIN cd_production cp ON sp.cd = cp.code_cd "
        sp3 = " AND cp.etaireia LIKE %s"
        params.append('%' + company + '%')
    else:
        sp1 = " "
        sp2 = " "
        sp3 = " "

    if year != '':
        y = " AND t.etos_par = %s"
        params.append(year)
    else:
        y = " "

    sql = "SELECT t.titlos AS TITLE, k1.onoma AS `COMPOSER NAME`, k1.epitheto AS `COMPOSER SURNAME`, " \
          "t.etos_par AS `SONG PRODUCTION`, k2.onoma AS `WRITER NAME`, k2.epitheto AS `WRITER SURNAME`" + sp1 + \
          "FROM tragoudi t LEFT JOIN kalitexnis k1 ON k1.ar_taut = t.sinthetis LEFT JOIN kalitexnis k2 " \
          "ON k2.ar_taut = t.stixourgos" + sp2 + "WHERE t.titlos LIKE %s " + sp3 + y
    return fetch(sql, params)


def insert_song(title, year, cd, singer, composer, songwriter):
    sql1 = """INSERT INTO `tragoudi` (`titlos`, `sinthetis`, `etos_par`, `stixourgos`) VALUES (%s, %s, %s, %s)"""
    sql2 = """INSERT INTO `singer_prod` (`cd`, `tragoudistis`, `title`) VALUES (%s, %s, %s)"""
    return affect(sql1, [title, composer, year, songwriter]), affect(sql2, [cd, singer, title])


def get_artists_list():
    sql = """SELECT * FROM `kalitexnis` ORDER BY kalitexnis.onoma ASC, kalitexnis.epitheto ASC"""
    return fetch(sql, [])


def get_productions_list():
    sql = """SELECT * FROM cd_production ORDER BY cd_production.etaireia ASC"""
    return fetch(sql, [])


def get_artist_range_year():
    sql = """SELECT MIN(etos_gen) AS Min, MAX(etos_gen) AS Max FROM kalitexnis"""
    return fetch(sql, [])
