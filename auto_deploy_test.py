from flask import Flask, request, abort,json,jsonify
from subprocess import call
import os

app = Flask(__name__)


@app.route('/payload', methods=['POST'])
def payload():
    if request.method == 'POST':
        # os.system('cd  d:/Pythontest/test && git pull origin master')
        print('---------------------begin----------------------')
        print(request.get_json())
        print('---------------------end----------------------')
        push_info = request.get_json()
        commit_info = push_info['commits']
        if push_info['ref'] == 'refs/heads/master':
            print('master分支有提交')
            print(push_info['commits'])
            os.system('git pull origin master')

        if push_info['commits'][0]['committer']['email'] == 'xingxiaobo@yijia.ai':
            print('确认是自己提交的')

        data = {
            'hello': 'world',
        }
        js = json.dumps(data)
        resp = jsonify(data)
        resp.status_code = 200
        os.system('git pull origin master')
        return resp
    else:
        abort(400)


if __name__ == '__main__':
        app.run(port=4567,debug=True)

