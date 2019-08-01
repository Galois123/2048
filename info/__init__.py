from flask import Flask
# 配置数据库
# db = SQLAlchemy()
# sess = Session()


def create_app():
    # 创建一个Flask实例
    app = Flask(__name__)
    app.debug = True

    from .modules.index import index_blu
    app.register_blueprint(index_blu)

    return app
