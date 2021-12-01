from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./static"

from pymongo import MongoClient

from datetime import datetime

client = MongoClient('13.125.137.38', 27017, username="test", password="test")
db = client.dbsparta_Hidden_track


@app.route('/')
def main():
    # DB에서 저장된 정보를 찾아서 HTML에 나타내기
    # file_receive = request.files.get('file_give')
    # name_receive = request.args.get('name_give')
    # station_receive = request.args.get('station_give')

    info = list(db.cafe.find({}, {"_id": False}))
    return render_template("index.html", info=info,)

# info=info, name=name_receive, station=station_receive, file=file_receive

# @app.route('/cafe', methods=['GET'])
# def view_cafe():
#     cafes = list(db.cafe.find({}, {'_id': False}))
#     return jsonify({'all_cafe': cafes})

# 클라이언트한테서 카페값 받아와서 DB 저장하기
@app.route('/cafe', methods=['POST'])
def save_cafe():
    name_receive = request.form['name_give']
    station_receive = request.form['station_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]

    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{mytime}'

    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'name': name_receive,
        'station': station_receive,
        'file': f'{filename}.{extension}'
    }
    db.cafe.insert_one(doc)

    return jsonify({'msg': '카페정보 업로드 완료!'})

# 클라이언트한테서 라이크값 받아와서 DB 저장하기
# @app.route('/cafe', methods=['POST'])
# def save_like():
#     like_receive = request.form['like_give']
#
#     doc = {
#         'like' : like_receive
#     }
#     db.cafe.insert_one(doc)
#
#     return jsonify({'msg': '카페 좋아요 POST 요청 완료!'})
#
#---------------------------------------------------------------------
@app.route('/detail', methods=['GET'])
def view_detail():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': 'GET 연결 완료!'})


# 클라이언트한테서 코멘트입력값 받아오기 DB 저장하기
@app.route('/detail', methods=['POST'])
def save_comment():
    id_receive = request.form['id_give']
    title_receive = request.form['title_give']
    artist_receive = request.form['artist_give']
    comment_receive = request.form['comment_give']

    doc = {
        'id' : id_receive,
        'title' : title_receive,
        'artist' : artist_receive,
        'comment' : comment_receive
    }
    db.detail.insert_one(doc)

    return jsonify({'msg': '디테일 POST 요청 완료!'})


@app.route('/like', methods=['GET'])
def view_like():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': 'GET 연결 완료!'})

# 클라이언트한테서 언라이크값 받아오기 DB 저장하기
@app.route('/like', methods=['POST'])
def save_unlike():
    unlike_receive = request.form['unlike_give']

    doc = {
        'unlike' : unlike_receive
    }
    db.cafe.insert_one(doc)

    return jsonify({'msg': '언라이크 POST 요청 완료!'})





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
















# from flask import Flask, render_template, jsonify, request
#
# app = Flask(__name__)
#
# from pymongo import MongoClient
#
# client = MongoClient('localhost', 27017)
# db = client.dbsparta
#
#
# ## HTML 화면 보여주기
# @app.route('/')
# def homework():
#     return render_template('index.html')
#
#
# # 주문하기(POST) API
# @app.route('/search', methods=['POST'])
# def save_cafe():
#     name_receive = request.form['name_give']
#
#     doc = {
#         'name': name_receive,
#     }
#
#     db.cafelist.insert_one(doc)
#
#     return jsonify({'msg': '카페 추가 요청 완료되었습니다!!'})
#
# # 주문 목록보기(Read) API
# @app.route('/search', methods=['GET'])
# def view_cafe():
#     searches = list(db.cafelist.find({}, {'_id': False}))
#
#     return jsonify({'all_searches': searches})
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)