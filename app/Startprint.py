# coding: utf-8
def config_startprint(app):
    """
        启动打印
    """
    
    print("");print("");print("")
    print("---------------------------------------------------------------------------------------------")

    import datetime
    from app.RAM import AppRAM
    from app.Config import BaseConfig, config

    print("启动时间:",datetime.datetime.now())
    print("Run in       :  <",AppRAM.runConfig,"> Config")
    print("Live Docs    : ","http://" + BaseConfig.RUNSERVER_IP + ":" + str(BaseConfig.RUNSERVER_PORT) + "/docs/api/")
    print("DEBUG Active : ", config[AppRAM.runConfig].DEBUG)
    print("")
    print('“我不知道第三次世界大战会用哪些武器，但第四次世界大战中人们肯定用的是木棍和石块。” ——阿尔伯特·爱因斯坦')
    print("出自Alice Calaprice所著《The New Quotable Einstein》")

    print("");print("");print("")