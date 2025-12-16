#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学生数据库模块
包含从Excel读取的数据
"""


class StudentDatabase:
    def __init__(self):
        """初始化数据库，硬编码Excel中的数据"""
        self.students = [
            {
                '序号': '1',
                'name': 'Bilal Zia',
                'uestc_id': '202424140107',
                'phone_number': '18740807216',
                'email': 'bilal.zia@uestc.edu.cn',
                'wechat_id': 'BilalZia786'
            },
            {
                '序号': '2',
                'name': 'Muhammad Jhan Zeb',
                'uestc_id': '202514040103',
                'phone_number': '19938010754',
                'email': 'muhammadjehanzaib@gmail.com',
                'wechat_id': 'iamjehanxaib'
            },
            {
                '序号': '3',
                'name': 'Ismayilzada Bukrat',
                'uestc_id': '2025080146006',
                'phone_number': '19828108397',
                'email': 'ismayilzadabukrat@gmail.com',
                'wechat_id': 'Bukrat'
            },
            {
                '序号': '4',
                'name': 'Arshad Aakash',
                'uestc_id': '202524040122',
                'phone_number': '19828108379',
                'email': 'aakasharshad7285@gmail.com',
                'wechat_id': 'AakashArshad'
            },
            {
                '序号': '5',
                'name': 'Ali Jahanzaib',
                'uestc_id': '202514020109',
                'phone_number': '17882219691',
                'email': 'jahanzaib.phy@outlook.com',
                'wechat_id': 'Jazzyb1122'
            },
            {
                '序号': '6',
                'name': 'Khan Muhammad Umar',
                'uestc_id': '202524040106',
                'phone_number': '19828108379',
                'email': 'aakasharshad584@gmail.com',
                'wechat_id': 'UmarKhan'
            },
            {
                '序号': '7',
                'name': 'Zahra',
                'uestc_id': '202514150116',
                'phone_number': '18109013072',
                'email': 'Zahrashehzadi777@gmail.com',
                'wechat_id': 'Xara7773'
            },
            {
                '序号': '8',
                'name': 'Akram Arfa',
                'uestc_id': '202524140105',
                'phone_number': '19828108603',
                'email': 'arfaakram75@gmail.com',
                'wechat_id': 'Meeluarfa'
            },
            {
                '序号': '9',
                'name': 'SHAH AIZAZ ALI',
                'uestc_id': '202424010108',
                'phone_number': '19150049475',
                'email': 'Feedback.aizaz@gmail.com',
                'wechat_id': 'Mr_Aizaz'
            },
            {
                '序号': '10',
                'name': 'maryam Iqbal',
                'uestc_id': '202524040101',
                'phone_number': '19828108335',
                'email': 'engrmaryam7685@gmail.com',
                'wechat_id': 'wxid_ctwoc9n8tvv222'
            },
            {
                '序号': '11',
                'name': 'Awan fahmee Maqsood',
                'uestc_id': '202414040105',
                'phone_number': '19181972470',
                'email': 'Fahmeemaqsood93@gmail.com',
                'wechat_id': 'wxid_3j16mt4o3c1w12'
            },
            {
                '序号': '12',
                'name': 'Iram Nasif',
                'uestc_id': '202424160101',
                'phone_number': '19915563216',
                'email': 'nasifiram@gmail.com',
                'wechat_id': '_Irm23'
            },
            {
                '序号': '13',
                'name': 'iqtidar ali',
                'uestc_id': '202414080101',
                'phone_number': '18111244154',
                'email': 'iqtidar.perviz@gmail.com',
                'wechat_id': 'Iqtidar_Ali_2024'
            },
            {
                '序号': '14',
                'name': 'Bayarkhuu Odgarig',
                'uestc_id': '2023080146018',
                'phone_number': '18884801091',
                'email': 'Godgarig0913@gmail.com',
                'wechat_id': 'Xingxing20010913'
            },
            {
                '序号': '15',
                'name': 'Yahya Abdurrazaq',
                'uestc_id': '202524080129',
                'phone_number': '19938324570',
                'email': 'yahyarimi02@gmail.com',
                'wechat_id': 'Abbayahayya'
            },
            {
                '序号': '16',
                'name': 'Sufyan Aslam',
                'uestc_id': '202314210108',
                'phone_number': '19160361374',
                'email': 'sufyanaslam@163.com',
                'wechat_id': 'Sufyan-21'
            },
            {
                '序号': '17',
                'name': 'Imane amouhou',
                'uestc_id': '2023080146019',
                'phone_number': '19308025246',
                'email': 'amouhouamouhou@gmail.com',
                'wechat_id': 'YangLadyy'
            },
            {
                '序号': '18',
                'name': 'Khan Farhad',
                'uestc_id': '202414080108',
                'phone_number': '18848236140',
                'email': 'farhadmohmand22@gmail.com',
                'wechat_id': 'princeFarhad'
            },
            {
                '序号': '19',
                'name': 'Aun Raza',
                'uestc_id': '202524010115',
                'phone_number': '19982030626',
                'email': 'aunraza2003@gamil.com',
                'wechat_id': 'UESTC_1214'
            },
            {
                '序号': '20',
                'name': 'Burhan',
                'uestc_id': '202314040102',
                'phone_number': '15776220683',
                'email': 'burhanali859@outlook.com',
                'wechat_id': 'belisns'
            }
        ]

        # 创建手机号索引
        self.phone_index = {}
        for student in self.students:
            phone = student['phone_number'].strip()
            self.phone_index[phone] = student

    def query_by_phone(self, phone):
        """根据手机号查询学生信息"""
        # 清理手机号
        phone = phone.strip()

        # 直接查找
        if phone in self.phone_index:
            return self.phone_index[phone].copy()

        # 如果找不到，尝试去掉可能的国际区号前缀
        if phone.startswith('+86'):
            phone = phone[3:].lstrip()
            if phone in self.phone_index:
                return self.phone_index[phone].copy()

        return None

    def get_count(self):
        """获取总记录数"""
        return len(self.students)


if __name__ == '__main__':
    # 测试数据库
    db = StudentDatabase()
    print(f"数据库中有 {db.get_count()} 条记录")

    # 测试查询
    test_phone = '18740807216'  # Bilal Zia 的手机号
    result = db.query_by_phone(test_phone)
    if result:
        print(f"找到记录: {result['name']}")
    else:
        print("未找到记录")