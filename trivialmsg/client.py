import requests

if __name__ == '__main__':
    host = input('connection point: ')
    sess = requests.session()
    while True:
        cmd = input()
        if len(cmd.split()) < 2:
            print('invalid command')
            continue

        data = {}
        if cmd.split()[0] == 'put':
            data['type'] = 'put'
            data['id'] = cmd.split()[1]
            data['msg'] = ' '.join(cmd.split()[2:])
        if cmd.split()[0] == 'get':
            data['type'] = 'get'
            data['id'] = cmd.split()[1]
        got = sess.post(url=host, json=data)
        print(got.json())
