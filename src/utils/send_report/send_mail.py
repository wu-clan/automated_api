#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from XTestRunner.config import RunResult

from src.common.log import log
from src.common.test_report import render_email_test_report
from src.core.conf import settings


class SendMail:

    def __init__(self, filename: str):
        self.filename = filename

    def take_messages(self):
        """ 生成邮件内容和html报告附件 """
        msg = MIMEMultipart()
        msg['Subject'] = settings.RESULT_TITLE
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        msg['From'] = settings.TESTER_NAME

        # 邮件正文
        content = render_email_test_report(**{
            'title': settings.RESULT_TITLE,
            'tester': settings.TESTER_NAME,
            'start_time': str(RunResult.start_time),
            'end_time': str(RunResult.end_time),
            'duration': str(RunResult.duration),
            'pass': str(RunResult.passed),
            'pass_rate': str(RunResult.pass_rate),
            'fail': str(RunResult.failed),
            'failure_rate': str(RunResult.failure_rate),
            'error': str(RunResult.errors),
            'error_rate': str(RunResult.error_rate),
            'skip': str(RunResult.skipped),
            'skip_rate': str(RunResult.skip_rate),
        })
        text = MIMEText(content, _subtype='html', _charset='utf-8')
        msg.attach(text)

        # 邮件附件
        att = MIMEText(str(open(self.filename, 'rb').read()), 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment', filename=f'{Path(self.filename).name}')
        msg.attach(att)

        return msg

    def send(self):
        """ 发送邮件 """
        try:
            if settings.EMAIL_SSL:
                smtp = smtplib.SMTP_SSL(host=settings.EMAIL_SERVER, port=settings.EMAIL_PORT)
            else:
                smtp = smtplib.SMTP(host=settings.EMAIL_SERVER, port=settings.EMAIL_PORT)
            smtp.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
            smtp.sendmail(settings.EMAIL_USER, settings.EMAIL_TO, self.take_messages().as_string())
            smtp.quit()
        except Exception as e:
            log.error(f'测试报告邮件发送失败: {e}')
        else:
            log.success("测试报告邮件发送成功")
