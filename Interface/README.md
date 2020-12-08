# python版接口自动化测试框架（unittest + 关联 + excle + ddt）

## 设计思路
- unittest + 关联 + excle + ddt

## 目录结构介绍
- bin：可执行文件，程序入口
- conf：配置文件，各种路径配置、ip、端口等
- data：测试数据excel
- lib：工具库
- reprot：测试报告
- test_case：测试用例
- log：日志文件
- README.md：说明文件


## 主要技术栈
- requests
- unittest
- ddt
- xlrd

## 待扩展功能
- **数据初始化**：比如要登录，保证有正确的账号，新增数据，要保证被新增的数据不存在；其实，业务数据基本上在流程测试过程中就依赖获取到了
- **测试结果反写excel**：非必须功能

