from Server.__init__ import api_key

import flask
from flask import request
import Server.database as db
import subprocess
import sys

app = flask.Flask(__name__)

tickers = {}


@app.route('/api/v1/price', methods=['GET'])
def api_price():
    """
    Queries server for latest price available as of the time specified.
    The time query is expected to be in UTC time.
    Example output:
    AAPL    332.50
    MSFT    180.30
    FB      No Data
    """
    queries = ['year', 'month', 'day', 'hour', 'minute']
    data = {}
    for query in queries:
        data[query] = request.args.get(query)
    # TODO: make sql to database and format result
    return data


@app.route('/api/v1/delete/<ticker>', methods=['DELETE'])
def api_del_ticker(ticker):
    """
    Instruct server to delete a ticker from the server database
    Returns:
        0=success
        1=server error
        2=ticker not found
    """
    # TODO: Delete data from database, and stop process for ticket
    # stop process
    tickers[ticker].kill()
    # delete data from database
    db.execute(db.delete())


@app.route('/api/v1/add/<ticker>/<interval>', methods=['POST'])
def api_add_ticker(ticker, interval):
    """
    Instruct server to add a ticker to the server database. Server will
    download historical data for said ticket, and start appending
    on the next pull
    Returns:
        0=success
        1=server error
        2=ticker not found
    """

    # TODO: Run subprocess
    p = subprocess.Popen(["python3", "./server/collect.py", ticker, interval])
    tickers[ticker] = p


@app.route('/api/v1/reset', methods=['DELETE'])
def api_reset(ticker):
    """
    Delete all information on server.
    Client exits with return code
    0=success
    1=failure
    """
    db.delete()
    # return 0 for success and 1 for failure

def command_line(args):
    if len(args) > 0:
        cmd = args[0]
        if cmd == '--tickers':
            pass
        elif cmd == '--port':
            pass
        elif cmd == '--reload':
            pass
        elif cmd == '--minutes':
            pass
        else:
            print("Illegal argument")


if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 8000
    # TODO: CLI arguments for server app
    args = sys.argv[1:]
    command_line(args)

    app.run(host=ip, port=port, debug=True)
