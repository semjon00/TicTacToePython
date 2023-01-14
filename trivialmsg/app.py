import json
from flask import Flask, request, make_response

messages = {}

app = Flask(__name__)


@app.route("/", methods=["POST"])
def message():
    content = request.json
    resp = ''
    if content['type'] == 'put':
        messages[content['id']] = content['msg']
        resp = make_response(json.dumps(
            {'status': 'ok'}
        ))
    elif content['type'] == 'get':
        if content['id'] in messages:
            resp = make_response(json.dumps(
                {'status': 'ok',
                 'msg': messages[content['id']]}
            ))
        else:
            resp = make_response(json.dumps(
                {'status': 'invalid_id'}
            ))
    else:
        resp = make_response(json.dumps(
            {'status': 'unknown_command'}
        ))
    return resp


if __name__ == '__main__':
    app.run()
