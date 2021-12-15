# python接口自动化测试框架

## 设计思路
- python3 + unittest + ddt + requests

## 目录结构介绍
- common/: 公共类
- core/: 配置
- data/: 测试数据
- db/: 数据库相关操作
- log/: 日志文件
- packages/: 存放第三方库包。如HTMLTestRunner，用于生成HTML格式测试报告
- report/: 生成接口自动化测试报告
- testcase/: 用于编写接口自动化测试用例
- utils/: 工具包
- run_*.py: 执行所有接口测试用例的主程序


