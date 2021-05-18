from flask import json, jsonify
import time

def ReturnRequest(returns):
    """全局返回请求结果

    Args:
        returns:
            code: int, 业务码
            msg: str, 业务消息 如果参数为空时默认返回"成功"
            data: json, 接口返回数据

    Returns:
        jsonify(json)
        example:
            {'code':200, 'msg': 成功,'data': None}
    
    """

    code, msg, data = returns

    if not msg:
        msg = '成功'
    jso = {'code':code, 'msg': msg,'data': data}

    # 打印每个请求的返回结果
    print('Return : ' + str(code) + ' => ' + str(jso))
    return jsonify(jso)