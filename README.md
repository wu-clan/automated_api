# python接口自动化测试框架

## 设计思路
- python3 + selenium3 + unittest + ddt + requests

## 目录结构介绍
- config/: 文件路径配置
- database/: 测试用例模板文件及数据库和发送邮箱配置文件
- db_fixture/: 初始化接口测试数据
- lib/: 程序核心模块。包含有excel解析读写、发送邮箱、发送请求、生成最新测试报告文件
- package/: 存放第三方库包。如HTMLTestRunner，用于生成HTML格式测试报告
- report/: 生成接口自动化测试报告
- testcase/: 用于编写接口自动化测试用例
- run_demo.py: 执行所有接口测试用例的主程序


