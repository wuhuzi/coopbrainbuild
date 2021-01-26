from py2neo import Graph, Node, Relationship, NodeMatcher
import pymysql
import json


class CreateGraph(object):
    def __init__(self):
        # 建立连接
        link = Graph("http://localhost:7474", username="neo4j", password="123456")
        self.graph = link
        self.matcher = NodeMatcher(self.graph)
        self.data = None

    # 清空图数据库
    def clean_node(self):
        self.graph.delete_all()

    # 查询MySQL数据库
    def select_data(self):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "123456", "coopbrainback")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT * FROM cbb_object_relation_object WHERE is_build_flag=0")
        # 使用 fetchall() 方法获取数据.
        self.data = cursor.fetchall()
        print(self.data[0][1])
        # 关闭数据库连接
        db.close()

    # 更新MySQL数据库
    def update_data(self):
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "123456", "coopbrainback")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("UPDATE cbb_object_relation_object SET is_build_flag = 1 WHERE is_build_flag = 0")
        db.commit()
        # 关闭数据库连接
        db.close()

    # 查找节点
    def find_node(self, node_label, node_name):
        node = self.matcher.match(
            node_label,
            name=node_name
        ).first()
        return node

    # 结点定义
    def create_node(self, node_data):
        node_properties = json.loads(node_data[4])
        node = Node(node_data[2], name=node_data[3], **node_properties)
        self.graph.create(node)
        return node

    # 建立关系
    def create_rel(self, node1, rel, node2):
        rel_properties = rel.rel_property
        node1_to_node2 = Relationship(node1, rel.name, node2, **rel_properties)
        self.graph.create(node1_to_node2)

    # 建立节点关系
    def create_node_rel(self):
        if self.data is not None:
            for node_data in self.data:
                node1 = self.find_node(node_data[2], node_data[3])
                if node1 is None:
                    node1 = self.create_node(node_data)
                    print(node1)
                # node2 = self.find_node(data.node2.node_label, data.node2.node_name)
                # if node2 is None:
                #     node2 = self.create_node(data.node2)
                # self.create_rel(node1, data.rel, node2)


c = CreateGraph()
# c.clean_node()
c.select_data()
# c.create_node_rel()
# c.update_data()
