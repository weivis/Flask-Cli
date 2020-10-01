# coding: utf-8
def config_errorhandler(app):
    """
        载入异常请求处理
    """

    # 错误页面配置
    @app.errorhandler(404)
    def page_not_found(e):
        return str(e)