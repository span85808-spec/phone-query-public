#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
留学生信息查询系统 - International Student Information Query System
手机号查询 - Phone Number Query
"""

from flask import Flask, render_template, request, jsonify, session
import os
from data.database import StudentDatabase
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-' + str(random.randint(10000, 99999))  # 随机密钥

# 初始化数据库
db = StudentDatabase()


@app.route('/')
def index():
    """显示查询页面"""
    # 从URL参数获取语言，默认为中文
    lang = request.args.get('lang', 'zh')
    return render_template('index.html', lang=lang)


@app.route('/api/query', methods=['POST'])
def query_student():
    """处理查询请求"""
    try:
        # 获取手机号
        phone = request.form.get('phone', '').strip()

        # 验证手机号
        if not phone:
            return jsonify({
                'success': False,
                'message': '请填写手机号 / Please enter phone number',
                'message_zh': '请填写手机号',
                'message_en': 'Please enter phone number'
            })

        if not phone.isdigit():
            return jsonify({
                'success': False,
                'message': '手机号只能包含数字 / Phone number must contain only digits',
                'message_zh': '手机号只能包含数字',
                'message_en': 'Phone number must contain only digits'
            })

        # 查询学生信息
        student = db.query_by_phone(phone)

        if student:
            # 对手机号进行脱敏处理
            if len(student['phone_number']) == 11:
                masked_phone = student['phone_number'][:3] + '****' + student['phone_number'][-4:]
                student['phone_masked'] = masked_phone
            else:
                student['phone_masked'] = student['phone_number']

            # 对邮箱进行脱敏处理
            if '@' in student['email']:
                parts = student['email'].split('@')
                if len(parts[0]) > 2:
                    masked_email = parts[0][0] + '*' * (len(parts[0]) - 2) + parts[0][-1] + '@' + parts[1]
                    student['email_masked'] = masked_email
                else:
                    student['email_masked'] = student['email']
            else:
                student['email_masked'] = student['email']

            # 对微信ID进行脱敏处理（如果有的话）
            if student['wechat_id']:
                wechat = student['wechat_id']
                if len(wechat) > 4:
                    student['wechat_masked'] = wechat[:2] + '*' * (len(wechat) - 4) + wechat[-2:]
                else:
                    student['wechat_masked'] = wechat
            else:
                student['wechat_masked'] = ''

            return jsonify({
                'success': True,
                'message': '查询成功 / Query successful',
                'message_zh': '查询成功',
                'message_en': 'Query successful',
                'student': student
            })
        else:
            return jsonify({
                'success': False,
                'message': '抱歉，未找到您的信息 / Sorry, your information was not found',
                'message_zh': '抱歉，未找到您的信息',
                'message_en': 'Sorry, your information was not found'
            })

    except Exception as e:
        print(f"查询错误: {e}")
        return jsonify({
            'success': False,
            'message': '系统错误，请稍后再试 / System error, please try again later',
            'message_zh': '系统错误，请稍后再试',
            'message_en': 'System error, please try again later'
        })


@app.route('/health')
def health_check():
    """健康检查端点"""
    return jsonify({'status': 'healthy', 'count': db.get_count()})


if __name__ == '__main__':
    # 打印一些统计信息
    print("=" * 60)
    print("留学生信息查询系统启动")
    print("=" * 60)
    print(f"系统中总共有 {db.get_count()} 条记录")
    print("查询字段：手机号 (Phone Number)")
    print("=" * 60)
    print("\n访问地址：")
    print("1. 本地访问: http://localhost:5000")
    print("2. 网络访问: http://[你的IP地址]:5000")
    print("\n语言切换：")
    print("- 中文: http://localhost:5000?lang=zh")
    print("- 英文: http://localhost:5000?lang=en")
    print("=" * 60)

    # 启动服务器
    # host='0.0.0.0' 允许其他设备访问
    # port=5000 默认端口

    if __name__ == '__main__':
    # 开发环境运行（本地测试用）
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
