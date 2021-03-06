import jieba
import logging
logger = logging.getLogger()
logger.setLevel('DEBUG')
def parse_order():
    # 输入用户/流水线任务指令 螺母装配螺栓
    user_commands = input("input your order:")
    # 分词
    seg_list = list(jieba.cut(user_commands, cut_all=False))
    logging.debug('seg_list:' + str(seg_list))  # 精确模式

    begin_entity = seg_list[0]
    logging.info('begin_entity:' + str(begin_entity))
    final_entity = seg_list[len(seg_list) - 1]
    logging.info('final_entity:' + str(final_entity))

# publish entities
def talker_entity():
    pub = rospy.Publisher('entities', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rospy.loginfo(hello_str)
    pub.publish(hello_str)


if __name__ == '__main__':
    try:
        talker_entity()
    except rospy.ROSInterruptException:
        pass