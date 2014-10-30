from flask import Flask, request
import sh
from config import *

app = Flask(__name__)


class Repository(object):

    def __init__(self, j):
        self.__dict__ = j


@app.route('/pull', methods=['POST'])
def pull():
    repo = Repository(request.json["repository"])
    repo_dir = '%s/%s' % (WEB_APP_DIR, repo.name)
    git = sh.git.bake(_cwd=repo_dir)
    git.pull()
    return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
