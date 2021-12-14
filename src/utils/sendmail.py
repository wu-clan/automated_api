#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.core.settings import EMAIL_FROM, EMAIL_HOST_SERVER, EMAIL_PASSWORD, EMAIL_TO, EMAIL_USER, RESULT_TITLE, \
    TEST_REPORT_PATH
from src.common.log import logger


class SendMail:

    def _get_report(self):
        """获取最新测试报告"""
        self.dirs = os.listdir(TEST_REPORT_PATH)
        self.dirs.sort()
        report = self.dirs[-1]
        logger.info(f'The report name is: {report}')
        return report

    def _take_messages(self):
        """生成邮件的内容，和html报告附件"""
        self.msg = MIMEMultipart()
        self.msg['Subject'] = RESULT_TITLE
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        # 读取要发送的附件
        with open(os.path.join(TEST_REPORT_PATH, self._get_report()), 'rb') as f:
            mail_body = str(f.read())

        # 邮件正文
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # 邮件附件
        att1 = MIMEText(mail_body, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self._take_messages()
        try:
            smtp = smtplib.SMTP(EMAIL_HOST_SERVER, 25)
            smtp.login(EMAIL_USER, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_FROM, EMAIL_TO, self.msg.as_string())
            smtp.close()
            logger.success("测试报告邮件发送成功")
        except Exception as e:
            logger.error('测试报告邮件发送失败\n', e)


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
