import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort, jsonify

from travel_iq import app
from travel_iq.engine.RequestHandler import RequestHandler

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

    #req = RequestHandler()
    #print req.locationConverter(location)

    response = {
        'result': [{'venueName': 'Brooklyn Museum', 'venueImage': 'None', 'venueDesc': 'No description for this place from Foursquare, visit url for more detail', 'venueURL': 'http://www.brooklynmuseum.org'}, {'venueName': 'High Line', 'venueImage': 'None', 'venueDesc': 'The High Line is an elevated freight rail line transformed into a public park on Manhattan\xe2\x80\x99s West Side. It is owned by the City of New York, and maintained and operated by Friends of the High Line.', 'venueURL': 'http://www.thehighline.org'}, {'venueName': 'Museum of Modern Art (MoMA)', 'venueImage': 'https://irs3.4sqi.net/img/general/original/QVSZOXC4I2SC2WRVFEQZITGNSTH4EAVF3MULRR4UKJBJD3ZA.jpg', 'venueDesc': "The Museum of Modern Art is a place that fuels creativity, ignites minds, and provides inspiration. Follow us on Foursquare to get tips on what's cool and new at MoMA\xe2\x80\x94and leave some yourself. Share tips on your visit to MoMA, whether it\xe2\x80\x99s checking out great art in our exhibitions, films, and lectures, or just enjoying time with friends. And a badge could be considered an artwork too\xe2\x80\xa6", 'venueURL': 'http://www.moma.org'}, {'venueName': 'Bryant Park', 'venueImage': 'None', 'venueDesc': 'Located in Midtown Manhattan, Bryant Park is visited by over 6 million people each year and is one of the busiest public spaces in the world.', 'venueURL': 'http://www.facebook.com/bryantparknyc'}, {'venueName': 'Citi Field', 'venueImage': 'https://irs2.4sqi.net/img/general/original/376887_WtceDnE_N5PvWH-XIhIdGy6E6KjFxTxLjtkHwr3ksqI.jpg', 'venueDesc': 'Welcome to the Official MLB Foursquare Page!', 'venueURL': 'http://www.mets.com'}, {'venueName': 'Gramercy Theatre', 'venueImage': 'None', 'venueDesc': 'No description for this place from Foursquare, visit url for more detail', 'venueURL': 'http://thegramercytheatre.com'}, {'venueName': 'The Metropolitan Museum of Art', 'venueImage': 'None', 'venueDesc': 'No description for this place from Foursquare, visit url for more detail', 'venueURL': 'http://www.metmuseum.org'}, {'venueName': 'Madison Square Park', 'venueImage': 'None', 'venueDesc': "New York City Department of Parks & Recreation is the steward of 5,000 of New York City\xe2\x80\x99s parks and park properties\xe2\x80\x94that\xe2\x80\x99s 14 percent of the city! You can follow NYC Parks for expert tips in every corner of the city. Be sure to check in at New York City\xe2\x80\x99s parks, playgrounds, recreation centers, monuments, food carts, and facilities to become a true New York explorer! Please read the City of New York's Social Media Customer Use Policy at nyc.gov/socialmediapolicy for information on communicating with Parks through social media. All service requests should be submitted through nyc.gov/311.", 'venueURL': 'http://nyc.gov/parks'}, {'venueName': 'Soho House', 'venueImage': 'None', 'venueDesc': 'No description for this place from Foursquare, visit url for more detail', 'venueURL': 'http://www.sohohouseny.com'}] 
    }

    return jsonify(response), 201


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



