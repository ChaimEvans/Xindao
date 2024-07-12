from 时间线 import *
from 各部门 import *
import 配置


class 季度:
    # 存
    # 季度ID = 0
    # 时间线 = None
    # # 写
    # 收入 = 0
    # 生产部门 = 生产部门()
    # 营销部门 = 营销部门()
    # 人力部门 = 人力部门()
    # 贷款 = 0
    # 还款 = 0
    # 折旧费 = 0
    # 违约金 = 0
    # 其他 = 0
    # 备注 = ""
    # # 读
    # 初始现金 = 0
    # 投入 = 0
    # 结算现金 = 0
    # 权益 = 0
    # 利润 = 0

    def __init__(self, 季度ID, _时间线_):
        self.季度ID = 季度ID
        self.时间线 = _时间线_
        self.收入 = 0
        self.生产部门 = 生产部门()
        self.人力部门 = 人力部门()
        self.营销部门 = 营销部门()
        self.贷款 = 0
        self.还款 = 0
        self.折旧费 = 0
        self.违约金 = 0
        self.其他 = 0
        self.备注 = ""
        # 读
        self.初始现金 = 0
        self.投入 = 0
        self.结算现金 = 0
        self.权益 = 0
        self.利润 = 0


    # def 配置生产部门(self, 生产线=0, 产品设计=0, 原材料=0, 开产费用=0, 产线维修费=0, 转产费=0, 折旧费=0, 其他=0,
    #                  备注=""):
    #     self.生产部门 = 生产部门(-self.时间线.所有季度[max(self.季度ID - 1, 0)].生产部门.原材料, 生产线, 产品设计,
    #                              原材料, 开产费用, 产线维修费, 转产费, 折旧费, 其他, 备注)

    def 刷新(self):
        if self.季度ID == 0:
            self.初始现金 = 配置.初始现金 + self.贷款
        else:
            self.初始现金 = self.时间线.所有季度[self.季度ID - 1].结算现金 + self.贷款

        if self.季度ID != 15:
            self.时间线.所有季度[self.季度ID + 1].生产部门.原材料延迟付款 = self.生产部门.原材料

        # 投入
        self.投入 = 0
        self.投入 += self.营销部门.合计()
        self.投入 += self.人力部门.合计()
        self.投入 += self.生产部门.合计()
        self.投入 += self.还款
        self.投入 += 配置.管理费
        self.投入 += self.违约金
        self.投入 += self.其他
        # 现金
        self.结算现金 = self.初始现金 + self.投入 + self.收入
        # 权益
        self.权益 = self.结算现金 - self.时间线.获取当前未还贷款总额(self.季度ID) - self.时间线.获取固定资产(self.季度ID)
        a = self.时间线.获取当前未还贷款总额(self.季度ID)
        b = self.时间线.获取固定资产(self.季度ID)
        # 利润
        self.利润 = self.收入 + self.投入
