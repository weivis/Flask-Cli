# coding: utf-8
def config_startprint(app, runConfig):
    """
        启动打印
    """
    
    print();print();print()
    print("--"*60)

    logo()
    
    import datetime
    from env import ENV
    from app.Config import BaseConfig, config

    if runConfig == "production":
        print("线上运行模式 >")
        print("启动时间      :",datetime.datetime.now())
        print("Run in       :  <",ENV,"> Config")
        print()

    else:
        print("开发模式运行 >")
        print("配置文件      : ",ENV," Config")
        print("启动时间      :",datetime.datetime.now())
        print("Live Docs    : ","http://" + BaseConfig.RUNSERVER_IP + ":" + str(BaseConfig.RUNSERVER_PORT) + "/docs/api/")
        print("DEBUG Active : ", config[ENV].DEBUG)
        print()

def logo():

    print(" ______   __         ______     ______     __  __     ______     __         __  ")
    print("/\  ___\ /\ \       /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\ \       /\ \   ")
    print('\ \  __\ \ \ \____  \ \  __ \  \ \___  \  \ \  _"-.  \ \ \____  \ \ \____  \ \ \  ')
    print(" \ \_\    \ \_____\  \ \_\ \_\  \/\_____\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ ")
    print("  \/_/     \/_____/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/  v0.4")

    print()
    print("感谢使用Flask-Cli脚手架(https://github.com/weivis/Flask-Cli), 脚手架作者WeiVi(https://www.weivird.com/)","正在启动中>")
    print('“我不知道第三次世界大战会用哪些武器，但第四次世界大战中人们肯定用的是木棍和石块。” ——阿尔伯特·爱因斯坦 (出自Alice Calaprice所著《The New Quotable Einstein》)')
    print("愿世界无战争")
    print()

def config_overstart():
    print()
    print("程序构建结束, 启动完成 >")
    print()