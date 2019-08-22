# -*- coding: utf-8 -*

# Solved decode issue, If your server has the right configiration, Skip it.
import json
import sys

# from importlib import reload
#
reload(sys)
#
print('sys.getdefaultencoding: ', sys.getdefaultencoding())
print('sys.getdefaultfilesystemencoding: ', sys.getfilesystemencoding())
sys.setdefaultencoding('utf8')
print('sys.getdefaultencoding: ', sys.getdefaultencoding())

from datetime import datetime

sqls = {
    'key1': {
        'oralce': """
            select to_char(bjrq) month_, t_key,ywlx, count(*)
            from (
                select bjrq, ywlx,
                        case 
                        when glbm>='410100008' and glbm<'410100009' 
                            then
                                (case 
                                 when glbm in ('410100008031','410100008030','410100008032','410100008054') then 'cgs' 
                                 else 'fwz' end)
                        when glbm in ('410122000400', '410181000400', '410182000400', '410183000400', '410184000400', '410185000400', '410106000400')
                            then 'xq' 
                        else 'qt' end t_key 
                from veh_flow 
                where lszt <> 'Q' 
                      -- and bjrq>=trunc(sysdate) 
                      -- 重写时间过滤条件
                      and bjrq >= to_date('2010-01-01', 'yyyy-mm-dd')
                      and bjrq < to_date('2019-01-01', 'yyyy-mm-dd')
                      and regexp_instr(ywlx, '[ABI]')>0
              )
            group by to_char(bjrq), t_key,ywlx
            order by month_, t_key
            """,
        'sparksql': """
             --  select year(bjrq) AS year_ , month (bjrq) AS month_, t_key, ywlx, count(*) -- ✅
            select trunc(bjrq, 'MM') month_, t_key, ywlx, count(*) -- ✅
            from (
                select bjrq, ywlx,
                        case 
                        when glbm>='410100008' and glbm<'410100009' 
                            then
                                (case 
                                 when glbm in ('410100008031','410100008030','410100008032','410100008054') then 'cgs' 
                                 else 'fwz' end)
                        when glbm in ('410122000400', '410181000400', '410182000400', '410183000400', '410184000400', '410185000400', '410106000400')
                            then 'xq' 
                        else 'qt' end t_key 
                from veh_flow_temp_view_002 
                where lszt <> 'Q'  -- ✅
                    and ywlx rlike '^(.*[ABI].*).*$' -- ✅
                   and bjrq >= timestamp('2010-01-01 00:00:00.0') -- ✅
                   and bjrq < timestamp('2019-01-01 00:00:00.0')
                   -- and bjrq >= timestamp('2019-08-08 00:00:00.0')
              )
            -- group by  year(bjrq), month (bjrq), t_key, ywlx ✅
            group by trunc(bjrq, 'MM'), t_key, ywlx -- ✅
            order by month_, t_key -- ✅
        """,
        'sparksql_count': """
           select count(*)
           from (
               select ywlx,
                       case 
                       when glbm>='410100008' and glbm<'410100009' 
                           then
                               (case 
                                when glbm in ('410100008031','410100008030','410100008032','410100008054') then 'cgs' 
                                else 'fwz' end)
                       when glbm in ('410122000400', '410181000400', '410182000400', '410183000400', '410184000400', '410185000400', '410106000400')
                           then 'xq' 
                       else 'qt' end t_key 
               from veh_flow_temp_view_002 
               where lszt <> 'Q' 
                   and ywlx rlike '^(.*[ABI].*).*$'
                   and bjrq >= timestamp('2010-01-01 00:00:00.0') -- ✅
                   and bjrq < timestamp('2019-01-01 00:00:00.0')
             )
       """,

        # 测试字符过滤，时间过滤，字符串包含
        'sparksql_select_count': """
            select *
            from veh_flow_temp_view_002

            -- 统计某段时间内的数量
            where  
                bjrq >= timestamp('2010-01-01 00:00:00.0') -- ✅
                and bjrq < timestamp('2019-01-01 00:00:00.0')
                -- bjrq>=trunc('2010-01-01', 'DAY') ❌ ， got 0

                and lszt <> 'Q'
                and ywlx rlike '^(.*[ABI].*).*$' -- ✅
                -- and  regexp_extract(ywlx, '[ABI]', 1)     
        """
    },
    'key2': {
        'oralce': """
           -- 10年的数据2.1s 三驾统计

           SELECT case
                      when wfxw1 in ('6034', '6035', '17121') or wfxw2 in ('6034','6035','17121')
                           or wfxw3 in ('6034','6035','17121') or wfxw4 in ('6034','6035','17121')
                           or wfxw5 in ('6034','6035','17121') then '酒驾'
                      when wfxw1 in ('6032','6022','6033') or wfxw2 in ('6032','6022','6033')
                           or wfxw3 in ('6032','6022','6033') or wfxw4 in ('6032','6022','6033')
                           or wfxw5 in ('6032','6022','6033') then '醉驾'
                      when wfxw2 in ('5035') or wfxw3 in ('5035') or wfxw4 in ('5035') or wfxw5 in ('5035') then '毒驾'
                      else '普通违法'
                  end AS "VIO_TYPE",
                  TRUNC(TO_DATE(wfsj), 'mm') AS timestamp,
                  COUNT(*) AS "count"
           FROM vio_force
           WHERE wfsj >= trunc(add_months(sysdate,-12), 'mm')
             AND wfsj <= trunc(sysdate,'mm')-1
             AND case
                      when wfxw1 in ('6034', '6035', '17121') or wfxw2 in ('6034','6035','17121')
                           or wfxw3 in ('6034','6035','17121') or wfxw4 in ('6034','6035','17121')
                           or wfxw5 in ('6034','6035','17121') then '酒驾'
                      when wfxw1 in ('6032','6022','6033') or wfxw2 in ('6032','6022','6033')
                           or wfxw3 in ('6032','6022','6033') or wfxw4 in ('6032','6022','6033')
                           or wfxw5 in ('6032','6022','6033') then '醉驾'
                      when wfxw2 in ('5035') or wfxw3 in ('5035') or wfxw4 in ('5035') or wfxw5 in ('5035') then '毒驾'
                      else '普通违法'
                 end != '普通违法'
             AND jllx != '3'
             AND xxly = '1'
           GROUP BY case
                         when wfxw1 in ('6034', '6035', '17121') or wfxw2 in ('6034','6035','17121')
                           or wfxw3 in ('6034','6035','17121') or wfxw4 in ('6034','6035','17121')
                           or wfxw5 in ('6034','6035','17121') then '酒驾'
                      when wfxw1 in ('6032','6022','6033') or wfxw2 in ('6032','6022','6033')
                           or wfxw3 in ('6032','6022','6033') or wfxw4 in ('6032','6022','6033')
                           or wfxw5 in ('6032','6022','6033') then '醉驾'
                      when wfxw2 in ('5035') or wfxw3 in ('5035') or wfxw4 in ('5035') or wfxw5 in ('5035') then '毒驾'
                        else '普通违法'
                    end,
                    TRUNC(TO_DATE(wfsj), 'mm')
           ORDER BY timestamp
            """,
        'sparksql': """

        """,
    },
    'key3': {
        'oracle': """
        -- 营运车辆复议
            select (case
                        when instr(SQBM,'410105')=1 then '一大队'
                        when instr(SQBM,'410102')=1 then '二大队'
                        when instr(SQBM,'410103')=1 then '三大队'
                        when instr(SQBM,'410104')=1 then '四大队'
                        when instr(SQBM,'410108')=1 then '五大队'
                        when instr(SQBM,'410199')=1 then '六大队'
                        when instr(SQBM,'410196')=1 then '九大队'
                        when instr(SQBM,'410194')=1 then '郑少大队'
                        when instr(SQBM,'410193')=1 then '西南大队'
                        when instr(SQBM,'410106')=1 then '上街大队'
                        when instr(SQBM,'410185')=1 then '登封大队'
                        when instr(SQBM,'410182')=1 then '荥阳大队'
                        when instr(SQBM,'410183')=1 then '新密大队'
                        when instr(SQBM,'410122')=1 then '中牟大队'
                        when instr(SQBM,'410188')=1 then '港区大队'
                        when instr(SQBM,'410184')=1 then '新郑大队'
                        when instr(SQBM,'410181')=1 then '巩义大队'
                        when instr(SQBM,'410198')=1 then '七大队大队'
                        when instr(SQBM,'410197')=1 then '八大队大队'
                        when instr(SQBM,'410189')=1 then '车管中心'
                        when instr(SQBM,'410100')=1 then '郑州市车辆管理所'
                        when instr(SQBM,'410187')=1 then '郑州交警支队电子警察'
                        when instr(SQBM,'410195')=1 then '十大队'
                        else '其他' end) sqbm,
              count(1),hpzl,trunc(sqsj) 
            from 
            ( 
                select sqbm,t.HPZL hpzl,t.SQSJ sqsj
                FROM vehicle c, vio_operate_check t
                WHERE t.sqbm like '4101%'
                     AND t.hpzl in ('01','02')
                     AND t.hpzl = c.hpzl
                     AND substr(t.hphm, 2, 7) = c.hphm
                     AND t.shjg = '1'
                     AND c.syxz IN ('B', 'C', 'D', 'E', 'F', 'G', 'R', 'T')
                     AND t.sqsj >= trunc(ADD_MONTHS(sysdate, -12), 'dd') and t.sqsj < trunc(sysdate, 'dd')
            ) a 
            group by sqbm,hpzl,trunc(sqsj)
        """,
        'sparksql': """
             select (case
                        when instr(SQBM,'410105')=1 then '一大队'
                        when instr(SQBM,'410102')=1 then '二大队'
                        when instr(SQBM,'410103')=1 then '三大队'
                        when instr(SQBM,'410104')=1 then '四大队'
                        when instr(SQBM,'410108')=1 then '五大队'
                        when instr(SQBM,'410199')=1 then '六大队'
                        when instr(SQBM,'410196')=1 then '九大队'
                        when instr(SQBM,'410194')=1 then '郑少大队'
                        when instr(SQBM,'410193')=1 then '西南大队'
                        when instr(SQBM,'410106')=1 then '上街大队'
                        when instr(SQBM,'410185')=1 then '登封大队'
                        when instr(SQBM,'410182')=1 then '荥阳大队'
                        when instr(SQBM,'410183')=1 then '新密大队'
                        when instr(SQBM,'410122')=1 then '中牟大队'
                        when instr(SQBM,'410188')=1 then '港区大队'
                        when instr(SQBM,'410184')=1 then '新郑大队'
                        when instr(SQBM,'410181')=1 then '巩义大队'
                        when instr(SQBM,'410198')=1 then '七大队大队'
                        when instr(SQBM,'410197')=1 then '八大队大队'
                        when instr(SQBM,'410189')=1 then '车管中心'
                        when instr(SQBM,'410100')=1 then '郑州市车辆管理所'
                        when instr(SQBM,'410187')=1 then '郑州交警支队电子警察'
                        when instr(SQBM,'410195')=1 then '十大队'
                        else '其他' end) sqbm,
              count(1),hpzl,trunc(sqsj, 'MM') 
            from (
                select sqbm,t.HPZL hpzl,t.SQSJ sqsj
                FROM veh_temp_view_002 c, vio_operate_check_view_002 t
                WHERE t.sqbm like '4101%'
                     AND t.hpzl in ('01','02')
                     AND t.hpzl = c.hpzl
                     AND substr(t.hphm, 2, 7) = c.hphm
                     AND t.shjg = '1'
                     AND c.syxz IN ('B', 'C', 'D', 'E', 'F', 'G', 'R', 'T')
                     AND t.sqsj >= trunc(ADD_MONTHS(current_date, -12), 'dd') and t.sqsj < trunc(current_date, 'dd')
            ) 
            group by trunc(sqsj, 'MM'), sqbm, hpzl
        """,
        'sparksql_count': """
        select count(*)
        from (
                select sqbm,t.HPZL hpzl,t.SQSJ sqsj
                FROM veh_temp_view_002 c, vio_operate_check_view_002 t
                WHERE t.sqbm like '4101%'
                     AND t.hpzl in ('01','02')
                     AND t.hpzl = c.hpzl
                     AND substr(t.hphm, 2, 7) = c.hphm
                     AND t.shjg = '1'
                     AND c.syxz IN ('B', 'C', 'D', 'E', 'F', 'G', 'R', 'T')
                     -- AND t.sqsj >= trunc('2018-08-09 00:00:00', 'DD') 
                     -- and t.sqsj < trunc('2019-08-09 00:00:00', 'DD')
                      and t.sqsj >= timestamp('2018-08-09 00:00:00.0')
                      and t.sqsj < timestamp('2019-08-05 00:00:00.0')
            ) 

        """,
        'sparksql_count_veh': """
            select *
            from veh_temp_view_002
            -- where ccdjrq <= date('2019-08-05 00:00:00.0')
            -- where ccdjrq <= to_date('2019-08-05')
            -- where ccdjrq <= timestamp('2019-08-05 00:00:00.0')
            order by ccdjrq desc


        """,
        'sparksql_count_vio_opt_check': """
            select count(*) 
            from vio_operate_check_view_002
            where sqsj < timestamp('2019-08-05 00:00:00.0')
            and sqsj >= timestamp('2018-08-09 00:00:00.0')
        """,
    }
}


def execute(func, params):
    return func(**params)


def get_sql(which, seconde=None):
    return sqls[which]['sparksql_count']


def use_case_2(which_sql):
    """

    :return:
    """
    # todo
    st = datetime.now()

    # from pyspark import SparkConf
    from pyspark import SparkContext
    from pyspark import SQLContext
    st_1 = datetime.now()
    sql = get_sql(which_sql)
    st_2 = datetime.now()

    print("Got sql: {sql}".format(sql=sql))

    # conf = SparkConf().setAppName("testing").setMaster("local[2]")
    sc = SparkContext().getOrCreate()

    sqlcontext = SQLContext(sc)
    st_3 = datetime.now()

    df_veh = sqlcontext.read.load('/srv/BigData/dbdata_service/ffk/vehicle_to_190805_allf')
    df_vio_op_check = sqlcontext.read.load('/srv/BigData/dbdata_service/ffk/vio_operate_check_to_190805_allf_parquet')

    # 注意这里是csv不是parquet
    # df_veh = sqlcontext.read.load('/srv/BigData/dbdata_service/ffk/vehicle_to190804_allf', format="csv", sep=",", inferSchema="true", header="true")
    # df_vio_op_check = sqlcontext.read.load('/srv/BigData/dbdata_service/ffk/vio_operate_check_to_190805_allf', format="csv", sep=",", inferSchema="true", header="true")

    st_4 = datetime.now()

    df_veh.createOrReplaceTempView('veh_temp_view_002')  # Create a view
    df_vio_op_check.createOrReplaceTempView('vio_operate_check_view_002')  # Create a view

    # df_veh.createGlobalTempView('veh_temp_view_002')
    # df_vio_op_check.createGlobalTempView('vio_operate_check_view_002')
    st_5 = datetime.now()

    # execute sql
    from pyspark.shell import spark
    df_veh_flow_key1 = spark.sql(sql)
    st_6 = datetime.now()

    df_veh_flow_key1.show()

    # 保存df结果到csv文件后返回给客户；u'd
    # new_rdd = df_veh_flow_key1.rdd.map(lambda x: (x[0], x))
    # dict = new_rdd.collectAsMap()

    # def print_rows(row):
    #     data = json.loads(row)
    #     for key in data:
    #         print("{key}:{value}".format(key=key, value=data[key]))
    # results = df_veh_flow_key1.toJSON()
    # results.foreach(print_rows)

    print('turn to json')
    results = df_veh_flow_key1.toJSON().map(lambda j: json.loads(j)).collect()
    print('got json', results)
    for i in results:
        print(i)
        # print(i["c1"], i["c6"])
    # data = df.toPandas().to_csv('mycsv.csv')

    # Spark 1.3
    # df_veh_flow_key1.save('mycsv.csv', 'com.databricks.spark.csv')
    # Spark 1.4+
    # df_veh_flow_key1.write.format('com.databricks.spark.csv').save('mycsv.csv')
    # Spark 2.0+
    # df_veh_flow_key1.write.csv('mycsv.csv')
    # pyspark.sql.utils.AnalysisException: u'path hdfs://hacluster/user/TestUser001/mycsv.csv already exists.;'
    # Send result to http

    import requests
    resp = requests.post('http://10.57.98.251:8008/some/url/404/', json=results)
    print(resp)
    st_7 = datetime.now()
    print('运行时间统计：\nLoad sql: {0} '
          '\nGet sqlcontext: {1}'
          '\nLoad data: {2}'
          '\nCreate table or view: {3}'
          '\nExecute sql: {4}'
          '\nShow result: {5}'.format(st_2 - st_1, st_3 - st_2, st_4 - st_3, st_5 - st_4, st_6 - st_5, st_7 - st_6))


try:
    # Submit your spark task
    # /opt/hadoopclient/Spark2x/spark/bin/spark-submit /home/var/project/SparkProjectTest/Usage_read_parquet.py
    st = datetime.now()

    # Choose a function to execute
    func = use_case_2
    params = {'which_sql': 'key3'}

    execute(func, params)

    print(" Spend Time: ", (datetime.now() - st).seconds)
except Exception as e:
    raise
