#!/usr/bin/env python
import settings
from datetime import datetime
from bottle import route, run, post, request, template, static_file
import database as q


@route('/')
def index():
    return template("templates/index.tpl")


@route('/static/:path#.+#', name='templates')
def static(path):
    return static_file(path, root='templates')


@post('/')
def controller():
    action = request.forms.get('action')
    if action == 'UPDATE & SEARCH ARTISTS':
        year_range = q.get_artist_range_year()
        if year_range[1] == None:
            min = year_range[0][1][0]
            max = year_range[0][1][1]
        else:
            min = 0
            max = 0
        return template("templates/presentation_of_artists.tpl", min=min, max=max, response='', error=year_range[1])
    elif action == 'SEARCH SONGS':
        return template("templates/presentation_of_songs.tpl")
    elif action == 'view_songs_results':
        return view_songs_results()
    elif action == 'INSERT ARTIST':
        return template("templates/insert_artist.tpl", affected=0, response='', max=datetime.now().year)
    elif action == 'insert_artist_submit':
        return insert_artist()
    elif action == 'INSERT SONG':
        return template("templates/insert_song.tpl", artists=q.get_artists_list()[0][1:],
                        productions=q.get_productions_list()[0][1:], affected=0, response='', max=datetime.now().year)
    elif action == 'insert_song_submit':
        return insert_song()
    elif action == 'view_artists_results_submit':
        return view_artist_results()
    elif action == 'edit_artist_information_submit':
        return edit_artist_information()
    elif action == 'Update' or action == 'Delete':
        return update_artist_information()
    else:
        return template("templates/index.tpl")


def view_artist_results():
    year_from = request.forms.get('year_from')
    year_to = request.forms.get('year_to')
    result = q.get_artists(
        request.forms.get('name'),
        request.forms.get('surname'),
        request.forms.get('option'),
        (0 if year_from == '' else year_from),
        (datetime.now().year if year_to == '' else year_to))
    records = len(result[0])-1
    output = template("templates/view_artist_results.tpl",
                      result=result[0],
                      response=str(records) + ' record' + ('s' if records != 1 else '') + ' found.',
                      error=result[1])
    return output


def edit_artist_information():
    id = request.forms.get('National_ID')
    name = request.forms.get('Name')
    name = '' if name == '(Null)' else name
    surname = request.forms.get('Surname')
    year = request.forms.get('Birth_Year')
    return template("templates/update_artist_information.tpl", id=id, name=name, surname=surname, year=year,
                    records=0, response='')


def update_artist_information():
    id = str(request.forms.get('id'))
    name = str(request.forms.get('name'))
    name = '' if name == '(Null)' else name
    surname = str(request.forms.get('surname'))
    year = str(request.forms.get('year'))
    if request.forms.get('action') == 'Update':
        result = q.update_artist(id, name, surname, year)
        response = 'Artist: \'' + id + ('\' has successfully updated!' if result[0] > 0 else '\' no information changed!')
        return template("templates/update_artist_information.tpl", id=id, name=name, surname=surname, year=year,
                    records=result[0], response=response, error=result[1], max=datetime.now().year)
    else:
        result = q.delete_artist(id)
        response = 'Artist: \'' + id + ('\' has successfully deleted!' if result[0] > 0 else '\'  doesn\'t exists!')
        if result[0] > 0:
            id = ''
            name = ''
            surname = ''
            year = ''
        return template("templates/update_artist_information.tpl", id=id, name=name, surname=surname, year=year,
                        records=result[0], response=response, error=result[1], max=datetime.now().year)


def insert_artist():
    id = request.forms.get('id')
    name = request.forms.get('name')
    surname = request.forms.get('surname')
    year = request.forms.get('year')
    result = q.insert_artist(id, name, surname, year) if id != '' and surname != '' else 0
    response = 'Artist: \'' + id + ('\' has successfully imported!' if result[0] > 0 else '\' import failure! ')
    return template("templates/insert_artist.tpl", id=id, name=name, surname=surname, year=year,
                    records=result[0], response=response, error=result[1], max=datetime.now().year)


def view_songs_results():
    result = q.get_songs(request.forms.get('title'), request.forms.get('year'), request.forms.get('company'))
    records = len(result[0]) - 1
    output = template("templates/view_songs_results.tpl",
                      result=result[0],
                      response=str(records) + ' record' + ('s' if records != 1 else '') + ' found.',
                      error=result[1])
    return output


def insert_song():
    title = request.forms.get('title')
    result = q.insert_song(title,
                           request.forms.get('year'),
                           request.forms.get('cd'),
                           request.forms.get('singer'),
                           request.forms.get('composer'),
                           request.forms.get('songwriter'))
    response = 'Song: \'' + title + \
               ('\' has successfully imported!' if result[0][0] and result[1][0] > 0 else '\' import failure! ')
    output = template("templates/insert_song.tpl",
                      artists=q.get_artists_list()[0][1:],
                      productions=q.get_productions_list()[0][1:],
                      records=(result[0][0], result[1][0]),
                      response=response,
                      error=(result[0][1], result[1][1]),
                      max=datetime.now().year)
    return output


run(host='localhost', port=settings.web_port)
