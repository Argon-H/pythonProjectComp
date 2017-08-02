# -*- coding: utf-8 -*-

from mysql_helper import query_all, del_many

if __name__ == '__main__':
    sql = "SELECT * FROM t_invoicing_product_sku WHERE product_code IN (SELECT temp.product_code FROM (" \
          "SELECT product_code FROM t_invoicing_product_sku GROUP BY product_code " \
          "HAVING count(product_code) > 1) temp) AND sku_code !='A01924'  ORDER BY product_code"
    skus = query_all(sql, None)

    # skuCode 列表
    sku_codes = tuple([x[2] for x in skus])
    print("skuCodes:" + str(sku_codes))
    # product_id 列表
    pids = tuple([x[1] for x in skus])
    print("pids:" + str(pids))

    format_strings = ','.join(['%s'] * len(sku_codes))
    print("格式化字符串:" + format_strings)

    sql_del_ref = "DELETE FROM  t_invoicing_supplier_sku_ref WHERE sku_code IN ({})".format(format_strings)
    del_ref_count = del_many(sql_del_ref, sku_codes)
    print("删除了{}条供应商sku关系记录".format(del_ref_count))

    sql_del_prod = "DELETE FROM  t_invoicing_product WHERE product_id IN ({})".format(format_strings)
    del_prod_count = del_many(sql_del_prod, pids)
    print("删除了{}条商品记录".format(del_prod_count))

    sql_del_sku = "DELETE FROM  t_invoicing_product_sku WHERE sku_code IN ({})".format(format_strings)
    del_sku_count = del_many(sql_del_sku, sku_codes)
    print("删除了{}条sku记录".format(del_sku_count))
