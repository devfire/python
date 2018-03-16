#!flask/bin/python
from flask import Flask, jsonify, request
from statsd import StatsClient

app = Flask(__name__)

'''
using all statsd defaults here:
STATSD_HOST = 'localhost'
STATSD_PORT = 8125
STATSD_PREFIX = None
STATSD_MAXUDPSIZE = 512
'''

'''set the app prefix so we can differentiate between multiple applications'''
statsdClient = StatsClient(prefix='epic.service')

'''create a custom error handler'''
def bad_request(message):
    response = jsonify({'ERROR': message})
    response.status_code = 400
    return response

def submit_statsd(jsonObject, counter):
	'''
	This function accepts a JSON object and a numeric value.
	It serializes the JSON object into a dot separated statsd metric.
	Then, it publishes the metric and the value via UDP to the statsd daemon

	NOTE: this function assumes 'geo' as the root json node.
	Safe assumption to make for now since traversing a json object
	of arbitrary depth requires far more code
	'''

	'''always initialize the metric list'''
	statsdMetric = []

	'''build up the metric dynamically, in case the json schema changes and a new field is added'''
	'''Note the mandatory geo prefix'''
	for value in jsonObject['geo'].itervalues():
		statsdMetric.append(value)

	'''join the fields with a dot separator'''
	statsdMetric = '.'.join(statsdMetric)

	'''submit to statsd'''
	statsdClient.incr(statsdMetric, counter)

'''default / path'''
@app.route('/', methods=['POST'])
def default_path():
	'''ensure we have a valid json request, error otherwise'''
	try:
		jsonPayload = request.json
	except:
     		return bad_request('Invalid JSON payload')

	'''convert the parameters to an immutable dict object'''
	parameters = request.args.to_dict()

	'''ensure count is present, error otherwise'''
	try: 
		statsdValue = parameters['count']
	except:
		return bad_request('Required count parameter is missing')

	'''ensure geo node is the head node, error otherwise'''
	try:
		geoAttributes = jsonPayload['geo']
	except:
		return bad_request('Required root node geo is missing')

	'''
	OK, now send data to statsd. We will accept non-integer count inputs
	since statsd accepts those and simply sets the value to 0.
	There maybe valid reasons why counter is passed as a non-integer?
	NOTE: because our statsd server listens for UDP traffic, 
	we won't know whether our request was successful or not
	'''
	submit_statsd(jsonPayload, statsdValue)

	'''return back to the client what we got'''
	return jsonify({'value': statsdValue}), 200

'''a very basic healthcheck endpoint'''
@app.route('/healthcheck', methods=['GET'])
def get_health():
    return jsonify({'health': 'OK'})

if __name__ == '__main__':
	'''change the default port 5000 to 80.
	Make sure to run with sudo because port 80 is a privileged port'''
        try:
    	    app.run(debug=False, port=80) 
        except:
            app.logger.error('Unable to bind to port, exiting')
