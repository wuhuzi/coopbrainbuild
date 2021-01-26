from py2neo import Graph, Node, Relationship, NodeMatcher
import pymysql
import json


class CreateGraph(object):
    def __init__(self):
        # 建立连接
        link = Graph("http://localhost:7474", username="neo4j", password="123456")
        # 打开数据库连接
        self.db = pymysql.connect("localhost", "root", "123456", "coopbrainback")
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
        self.graph = link
        self.matcher = NodeMatcher(self.graph)
        self.data = None

    # 清空图数据库
    def clean_node(self):
        self.graph.delete_all()

    def close_mysql(self):
        # 关闭数据库连接
        self.db.close()

    # 查询MySQL数据库
    def retrieve_sing_object(self, state):
        # 使用 execute()  方法执行 SQL 查询
        sql = ("SELECT * FROM cbb_single_object WHERE is_build_flag = %d" % state)
        self.cursor.execute(sql)
        # 使用 fetchall() 方法获取数据.
        self.data = self.cursor.fetchall()

    # 查询MySQL数据库
    def retrieve_object_relation_object(self):
        # 使用 execute()  方法执行 SQL 查询
        sql = 'SELECT b.object_lable_name,b.object_name,c.object_lable_name,c.object_name,a.relation_name,a.relation_attribute FROM cbb_object_relation_object AS a LEFT JOIN cbb_single_object AS b ON a.object_one_id = b.id LEFT JOIN cbb_single_object AS c ON a.object_two_id = c.id WHERE a.is_build_flag = 0 '
        self.cursor.execute(sql)
        # 使用 fetchall() 方法获取数据.
        self.data = self.cursor.fetchall()

    # 更新MySQL数据库
    def update_data(self, db_name, state):
        # 使用 execute()  方法执行 SQL 查询
        self.cursor.execute("UPDATE %s SET is_build_flag = 1 WHERE is_build_flag = %d" % (db_name, state))
        self.db.commit()

    # 查找节点
    def find_node(self, node_label, node_name):
        node = self.matcher.match(
            node_label,
            name=node_name
        ).first()
        return node

    # 结点定义
    def create_node(self):
        if self.data is not None:
            for node_data in self.data:
                node_properties = json.loads(node_data[4])
                node = Node(node_data[2], name=node_data[3], **node_properties)
                self.graph.create(node)

    # 更新结点属性
    def update_node(self):
        if self.data is not None:
            for node_data in self.data:
                node = self.find_node(node_data[2], node_data[3])
                node_properties = json.loads(node_data[4])
                node.update(node_properties)
                self.graph.push(node)

    # 建立关系
    def create_rel(self):
        if self.data is not None:
            for rel_data in self.data:
                node1 = self.find_node(rel_data[0], rel_data[1])
                node2 = self.find_node(rel_data[2], rel_data[3])
                rel_properties = json.loads(rel_data[5])
                if node1 is not None and node2 is not None:
                    node1_to_node2 = Relationship(node1, rel_data[4], node2, **rel_properties)
                    self.graph.create(node1_to_node2)

    # 建立节点关系
    # def create_node_rel(self):
    #     if self.data is not None:
    #         for node_data in self.data:
    #             node1 = self.find_node(node_data[2], node_data[3])
    #             if node1 is None:
    #                 node1 = self.create_node(node_data)
    #                 print(node1)
    #             node2 = self.find_node(data.node2.node_label, data.node2.node_name)
    #             if node2 is None:
    #                 node2 = self.create_node(data.node2)
    #             self.create_rel(node1, data.rel, node2)


c = CreateGraph()
# c.clean_node()
c.retrieve_sing_object(0)
c.create_node()
c.update_data("cbb_single_object", 0)
c.retrieve_sing_object(2)
c.update_node()
c.update_data("cbb_single_object", 2)
c.retrieve_object_relation_object()
# c.create_node_rel()
c.create_rel()
c.update_data("cbb_object_relation_object", 0)
c.close_mysql()
