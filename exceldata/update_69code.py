# -*- coding: utf-8 -*-
# 更新69码,两种方式1,数据量大从excel里读取,2,数据量小,直接写在代码里
#     skus = [('00382', '6926032333371'), ('00381', '6926032329329'), ('00383', '6926032333357'),
#            ('A01691', '6918730033844'), ('A04223', '6918730033806'), ('00380', '6926032333364')]
from mysql_helper import update_many_by_params

from pyexcel_xlsx import get_data


def update_many_data():
    excel_data = get_data("69码更新144个---201704201958.xlsx")
    sheet_data = excel_data['Sheet1'][1:]  # 获取Sheet1的第二行之后的数据
    print("excel数据:{}".format(sheet_data))
    sql_data = [tuple(x[::-1]) for x in sheet_data]
    print("sql_data:{}".format(sql_data))
    return sql_data


def exceute_update(skus):
    sql_update69code = """UPDATE t_invoicing_product_sku sku, t_invoicing_product prod
              SET sku.product_code = %s,prod.product_name = %s
              WHERE sku.product_id = prod.product_id
              AND sku.sku_code = %s"""

    result = update_many_by_params(sql_update69code, skus)
    print("一共更新{}条数据".format(result))


if __name__ == "__main__":
    update_skus = update_many_data()
    exceute_update(update_skus)
