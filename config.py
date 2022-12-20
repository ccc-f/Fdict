# 公司信息
company_domain = 'xx.com'
company_short_name = 'xx'
company_city_short_name = 'gz'
# 公司相关代码 证卷代码 或者 股票代码 或者 客服电话号码 或者 邮政编码 或者 公司成立的时间
company_code = []
# 工号
jobNo = ''
# 已知账号，不知道可以不写
username = ''
# 密码的最小位数
min_pwd = 0
# 密码的最大位数
max_pwd = 50
# 在已生成的密码前面全都添加 ! ， 密码翻倍
is_add_pre = False
add_pre = ['!',]
# 在已生成的密码后面全都添加 ! ， 密码翻倍
is_add_suf = False
add_suf = ['!']
# 根据已知工号生成用户名如 1234 会遍历四位数生成一系列用户名为 公司简称+工号
build_jobNo_username = False
build_other_username = False