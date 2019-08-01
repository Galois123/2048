# from redis import StrictRedis
# import logging


# class BaseConfig(object):

    # """
    # 基本配置类
    # """

    # DEBUG = True
    # # 配置secret_key
    # SECRET_KEY = "I1PyYz2ifL3wbT8/50kvNNx5VnwR782uQhXNEB/3pRfH1t7xYF21bhzvwmix/1eU"

    # # 数据库的配置信息
    # SQLALCHEMY_DATABASE_URI = "mysql://root:rainbow@localhost:3306/my_info"
    # # 设置数据库跟踪
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # # 在请求结束时候，如果指定此配置为 True ，那么 SQLAlchemy 会自动执行一次 db.session.commit()操作
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # # redis 配置
    # REDIS_HOST = "127.0.0.1"
    # REDIS_PORT = 6379

    # # flask_session配置信息
    # # 指定session保存到redis中
    # SESSION_TYPE = "redis"
    # SESSION_USE_SIGNER = True  # 让cookie中的session_id被加密处理
    # SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用redis实例
    # PERMANENT_SESSION_LIFETIME = 86400


# class DevelopConfig(BaseConfig):

    # """
    # 开发环境
    # """
    # DEBUG = True
    # # 记录日志的等级
    # LOG_LEVEL = logging.DEBUG


# class ProductConfig(BaseConfig):

    # """
    # 生产环境
    # """
    # DEBUG = False
    # LOG_LEVEL = logging.WARNING


# config_dict = {
    # 'develop': DevelopConfig,
    # 'product': ProductConfig
# }
