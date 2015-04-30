import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort, jsonify

from travel_iq import app
from travel_iq.engine.RequestHandler import getResults

@app.route('/')
def index(**kwargs):
    return make_response(open('travel_iq/templates/index.html').read())


@app.route('/search', methods=['POST'])
def search(**kwargs):
    if not request.json:
        abort(400)

    data = request.json
    location = data['q']
    filters = data['filters']

    if filters:
        filterValues = filters.values()
    else:
        filterValues = []

    results = getResults(location, filterValues)

    response = {
        'result': results
    }

    return jsonify(response), 201


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



