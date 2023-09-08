"""
预约
"""
from libs.info import infos
from libs.source import ZWYT

if __name__ == '__main__':
    # action工作流
    # 获取secrets里面的数据
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    devName = os.getenv('DEVNAME')
    periods = os.getenv('PERIODS')

    if username and password and devName and periods:
        try:
            # 初始化类示例，传入用户名、密码、时间段
            yy = ZWYT('action', username, password, periods)
            
            # 调用预约函数预约，传入预约座位号
            yy.reserve(devName)  
        except Exception as e:
            print(e)





    # 本地运行
    # 遍历 info 信息，获取每个用户的昵称、预约座位号、用户名、密码、时间段
    for stu in infos:
        try:
            # 初始化类示例，传入昵称、用户名、密码、时间段
            yy = ZWYT(stu['name'], stu['sno'], stu['pwd'], stu['periods'])
            
            # 调用预约函数预约，传入预约座位号
            yy.reserve(stu['devName'])  
        except Exception as e:
            print(e)
            continue
