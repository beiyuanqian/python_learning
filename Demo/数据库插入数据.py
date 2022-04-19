# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/1/6}

import pymysql

db = pymysql.connect(host="10.2.22.51", port=30311, user="skynet", password="skynet!23",
                     database="supplier_detection_platform")
cursor = db.cursor()
# 统计sample_inspection的数据总量
sql_1 = 'select count(*) from sample_inspection;'
cursor.execute(sql_1)
print(cursor.fetchall())

# sql_2 = 'delete from sample_inspection where customer_material_code="ceshi_number_0";'
# cursor.execute(sql_2)
# db.commit()
# print(cursor.fetchall())

# 插入数据
for i in range(0, 500000):
    id_1 = 'd64aebbde3354e348dc3fabe8a' + str(i).zfill(6)
    DD = 'DD_ceshi_number_' + str(i).zfill(6)
    nbDD = 'nbDD_ceshi_number_' + str(i).zfill(6)
    DD_id = '1fd5507f11a9401b831577242b' + str(i).zfill(6)
    print(id_1)
    sql = """INSERT INTO sample_inspection(
        id,
         sampling_ratio,
         qualified_ratio,
         customer_order_num,
         inner_order_num,
         detect_type,
         repair_times,
         customer_material_code,
         inner_material_code,
         material_name,
         customer_name,
         customer_code,
         order_quantity,
         old_invalid_number,
         image_number,
         version,
         detect_number,
         material_group_name,
         material_type_name,
         product_line_id,
         product_line_name,
         has_barcode,
         device_name,
         inspection_result,
         unqualified_reason_type,
         inspector_user_name,
         detect_used_time,
         detect_start_time,
         detect_end_time,
         company_code,
         send_to,
         update_time,
         update_by,
         create_time,
         create_by,
         is_delete,
         order_id,
         material_id,
         material_standard_id,
         manual_order_quantity,
         small_batch_num,
         inner_image_number,
         product_model,
         sampling_num,
         material_group_code,
         material_type_code,
         currency_flag,
         currency_material_id,
         currency_material_code,
         uid
    ) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
             '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
             '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s)""" % (
        id_1,
        '6.000',
        '90.000',
        DD,
        nbDD,
        '0',
        '0',
        'ceshi_number_0',
        'ceshi_number_0',
        '测试物料',
        '珠海格力电器股份有限公司',
        '400',
        '50',
        '0',
        'TUZHIWENJIANHAO',
        'bz-1',
        '3',
        'NULL',
        'NULL',
        '73',
        'K4',
        '0',
        'NULL',
        '0',
        'NULL',
        'admin(格力)',
        '16119',
        '1622188283010',
        '1622188299129',
        '760113',
        'NULL',
        '1622188299529',
        'admin(格力)',
        '1622188299529',
        'admin(格力)',
        '0',
        DD_id,
        '7008ab6b1c79476082dabc30995af939',
        'ecbcfb10c27a42e3b91dafc71e456b94',
        '50',
        '1',
        'TUZHIWENJIANHAO',
        'NULL',
        '0',
        'NULL',
        'NULL',
        '0',
        'NULL',
        'NULL',
        'NULL'
    )
    cursor.execute(sql)
    db.commit()
# try:
#
# except:
#     db.rollback()

# 统计sample_inspection的数据总量
sql_3 = 'select count(*) from sample_inspection;'
cursor.execute(sql_3)
print(cursor.fetchall())
db.close()