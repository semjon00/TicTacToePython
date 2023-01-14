import requests

if __name__ == '__main__':
    host = input('Where to connect?: ').strip()
    while True:
        sess = requests.session()
        # room_nr = input('Room number: ')
        got = sess.post(url=host, json={'reset': 1})
        while True:
            print(got.json()['msg'])
            print(got.json()['board'])
            print()

            command = input('Enter command: ') + ' '
            data = {}
            if command.split(' ')[0] == 'stop':
                break
            elif command.split(' ')[0] == 'choice':
                data['choice'] = command.split(' ')[1]
            else:
                data['reset'] = 1
            got = sess.post(url=host, json=data)
