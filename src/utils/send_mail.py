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

    def __init__(self, filename: str):
        self.filename = filename

    def take_messages(self):
        """生成邮件的内容，和html报告附件"""
        msg = MIMEMultipart()
        msg['Subject'] = settings.RESULT_TITLE
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        # 读取要发送的附件
        with open(os.path.join(HTML_REPORT, self.filename), 'rb') as f:
            mail_body = str(f.read())

        # 邮件正文
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg.attach(html)

        # 邮件附件
        att1 = MIMEText(mail_body, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = f'attachment; filename={self.filename}'
        msg.attach(att1)

        return msg

    def send(self):
        """发送邮件"""
        try:
            if settings.EMAIL_SSL:
                smtp = smtplib.SMTP_SSL(host=settings.EMAIL_SERVER, port=settings.EMAIL_PORT)
            else:
                smtp = smtplib.SMTP(host=settings.EMAIL_SERVER, port=settings.EMAIL_PORT)
            smtp.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
            smtp.sendmail(settings.EMAIL_USER, settings.EMAIL_TO, self.take_messages().as_string())
            smtp.quit()
        except Exception as e:
            log.error(f'测试报告邮件发送失败: \n {e}')
        else:
            log.success("测试报告邮件发送成功")
