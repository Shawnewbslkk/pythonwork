from flask import Flask,request
import requests
from flask_restful import Resource,Api
import pymysql

app = Flask(__name__)
api = Api(app)


class Student_info(Resource):
    @staticmethod
    def get():
        db = pymysql.connect(host='127.0.0.1', user='root', password='mm5201314', database='newone', port=3306,
                             charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("select * from student_info")
        data = cursor.fetchall()
        datanew = {}
        datanew["msg"] = data
        return datanew, 200, {"Access-Control-Allow-Origin": "*"}


class Exam_info(Resource):
    @staticmethod
    def get():
        db = pymysql.connect(host='127.0.0.1', user='root', password='mm5201314', database='newone', port=3306,
                             charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("select * from exam_info")
        data_exam = cursor.fetchall()
        data_examnew = {}
        data_examnew["msg"] = data_exam
        print(data_examnew)
        return data_examnew, 200, {"Access-Control-Allow-Origin": "*"}

class somemassage(Resource):
    @staticmethod
    def get():
        info = {
            "message":[
                {
                    "examType": "初级考试",
                    "msg": "一些测试信息",
                    "details":
                        "音乐考试局是乐器及音乐理论等级考试的评审机构，各音乐考试局有不同的考试级别，但大部分都包括由初级至演奏级的音乐考试。"
                },
                {
                    "examType": "中级考试",
                    "msg": "一些测试信息",
                    "details":
                        "大多数的考试局只供考生在当地应考，少数考试局亦设海外考场方便海外考生考试（如英国皇家音乐学院联合委员会 ABRSM，英国圣三一音乐学院 Trinity，维也纳音乐考试局 Vienna Music Examination Board）。英国皇家音乐学院联合委员会ABRSM为现时最多国际考生的音乐评审机构，每年有超过六十万考生应考，其中约90％考生来自香港，其余10％是来自世界各地及英国本土的考生。"
                },
                {
                    "examType": "高级考试",
                    "msg": "一些测试信息",
                    "details":
                        "世界著名的音乐考试局及音乐评审机构包括：\n" +
                        "\n" +
                        "英国皇家音乐学院联合委员会：英文官方网站 www.abrsm.org\n" +
                        "维也纳音乐考试局：德文及英文官方网站 www.vmeb.org; 中文版官方网站 www.vmeb-cn.com\n" +
                        "英国圣三一音乐学院：英文官方网站 www.trinitycollege.co.uk; 中文版官方网站 www.trinitycollege.com.hk\n" +
                        "英国伦敦音乐学院：中文版官方网站 [1]\n" +
                        "澳洲音乐考试局 www.ameb.edu.au\n" +
                        "新西兰音乐考试局 www.nzmeb.org\n" +
                        "加拿大皇家音乐学院 www.rcmexaminations.org\n" +
                        "此外，亦有一些较著名由私人机构组成的音乐评级机构（如 YAMAHA），YAMAHA 音乐试流行于日本及台湾地区。"
                }
            ]
        }
        return info, 200, {"Access-Control-Allow-Origin": "*"}


# class login():
#@app.route('/login', methods=['POST', 'GET'])
#def login():
    #if request.method == 'POST':
        #return {"msg": True}, 200, {"Access-Control-Allow-Origin": "*"}

#class login(Resource):
    #@staticmethod
    #def post():
        #return {"msg": True}, 200, {"Access-Control-Allow-Origin": "*"}


api.add_resource(Student_info, '/api/candidateinfo')
#api.add_resource(somemassage, '/message')
api.add_resource(Exam_info, '/api/examType')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
