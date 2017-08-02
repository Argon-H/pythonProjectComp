# -*- coding: utf-8 -*-
# 导出69码重复的sku
from collections import OrderedDict

from mysql_helper import query_all
from pyexcel_xlsx import get_data
from pyexcel_xlsx import save_data


def export_same_69code_sku():
    """导出69码重复的商品sku到xd.xlsx """
    sql = "SELECT sku_code,product_code,jd_sku_code,sync_date,create_date,update_date FROM t_invoicing_product_sku " \
          "WHERE product_code IN (" \
          "SELECT temp.product_code FROM (SELECT product_code FROM t_invoicing_product_sku " \
          "GROUP BY product_code HAVING count(product_code) > 1) temp) ORDER BY product_code"
    result = query_all(sql, None)

    # 打开预定义的文件表头文件
    xh = get_data("d:/商品表表头.xlsx")
    # 拼接整表数据
    xd = OrderedDict()
    xd.update({"Sheet1": xh['Sheet1'] + list(result)})

    # 保存到另外一个文件中
    save_data("d:/重复69码的sku.xlsx", xd)


def export_69not_equal_sku():
    """导出69码京东和进销存不一致的商品sku到xd.xlsx """
    data = get_data("需要删除商品条码清单.xlsx")
    # 第二行开始读取数据
    sheet_data = data['京东 (2)'][1:]
    print("excel数据{}".format(sheet_data))
    emgs = [x[0] for x in sheet_data]
    print("emgs is :{}".format(emgs))


if __name__ == "__main__":
    export_same_69code_sku()
    # export_69not_equal_sku()
