from flask import Blueprint, request, jsonify, url_for, redirect, render_template
from . import db
from .ModelDB import TokenInfo

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'main'


@main.route('/add')
def add():
    username = request.args.get('username')

    adduser = TokenInfo(username=username)
    try:
        db.session.add(adduser)
        db.session.commit()
    except Exception as e:
        return jsonify({'message': str(e)})

    return redirect(url_for('main.data'))


@main.route('/api')
def api():
    showdata = TokenInfo.query.all()
    data = []
    for i in showdata:
        temp = {}
        temp['id'] = i.id
        temp['username'] = i.username
        temp['created'] = i.created
        # print(i)
        data.append(temp)
    # print('id : {}, username : {}, createtime: {}'.format(i.id, i.username, i.created))
    return jsonify(data)


@main.route('/show')
def data():
    showdata = TokenInfo.query.order_by(TokenInfo.created).all()
    return render_template('index.html', users=showdata)
