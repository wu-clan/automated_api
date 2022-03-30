#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.common.log import log
from src.core.conf import settings
from src.core.path_settings import HTML_REPORT


class SendMail:

    def _get_report(self):
        """获取最新测试报告"""
        self.dirs = os.listdir(HTML_REPORT)
        self.dirs.sort()
        report = str(self.dirs[-1])
        log.info(f'获取测试报告: {report}')
        return report

    def _take_messages(self):
        """生成邮件的内容，和html报告附件"""
        self.msg = MIMEMultipart()
        self.msg['Subject'] = settings.RESULT_TITLE
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        # 读取要发送的附件
        _filename_name = self._get_report()
        with open(os.path.join(HTML_REPORT, _filename_name), 'rb') as f:
            mail_body = str(f.read())

        # 邮件正文
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # 邮件附件
        att1 = MIMEText(mail_body, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = f'attachment; filename={_filename_name}'
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self._take_messages()
        try:
            smtp = smtplib.SMTP(settings.EMAIL_HOST_SERVER, settings.EMAIL_PORT, timeout=settings.EMAIL_TIMEOUT)
            smtp.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
            smtp.sendmail(settings.EMAIL_USER, settings.EMAIL_TO, self.msg.as_string())
        except Exception as e:
            log.error(f'测试报告邮件发送失败: \n {e}')
        else:
            smtp.close()
            log.success("测试报告邮件发送成功")


send_email = SendMail()

if __name__ == '__main__':
    send_email.send()
