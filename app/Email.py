from flask import current_app
from app.Extensions import mail
from flask_mail import Message
from threading import Thread

class EmailConfig:
    """发送邮件模块存放个性配置
    
    EMAIL_TITLE_PREFIX:
        邮件标题前缀，如: `[我是前缀]` + 我是一封邮件
        发送后完整标题应该为 [我是前缀]我是一封邮件
    
    """
    EMAIL_TITLE_PREFIX = ''


def SeedEmail(sender, recipients, email_title, email_body='', email_html=''):
    """发送邮件

    Args:
        sender: Str, 发件人 和 MAIL_USERNAME 一致即可
        recipients: Any, 收件人
        email_title: Str, 邮件标题
        email_body: Str, 这个我也不是很懂
        email_html: Str, 邮件html内容

    Example:
        SeedEmail(
            sender='happys_wei@163.com',
            recipients=[happys_wei@163.com],
            email_title='[ 魔法少女伊莉雅应援站(illya-support.weivird.com) ]注册账户邮箱验证',
            email_body='请点击链接完成账户注册验证',
            email_html='<h3>点击以下链接完成账户注册验证</h3><a href="https://illya-support.weivird.com/auth/verify?vcode={0}">点击完成注册验证</a> 或 复制地址到浏览器打开http://localhost:8080/auth/verify?vcode={1}'.format(str(vcode), str(vcode))
        )

    """

    # 创建上下文
    app = current_app._get_current_object()

    # 创建邮件
    message = Message(EmailConfig.EMAIL_TITLE_PREFIX + email_title, sender=sender, recipients=recipients)
    message.body = email_body
    message.html = email_html
    
    # 异步提交
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()

def _send_async_mail(app, message):
    """异步发送邮件"""
    with app.app_context():
        mail.send(message)
        print('异步邮件发送成功>')