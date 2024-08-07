class 营销部门:
    # 开拓市场 = 0
    # 资格认证 = 0
    # 质量认证 = 0
    # 广告投资 = 0
    # 其他 = 0
    # 备注 = ""

    def __init__(self, 开拓市场=0, 资格认证=0, 质量认证=0, 广告投资=0, 其他=0, 备注=""):
        self.开拓市场 = -开拓市场
        self.资格认证 = -资格认证
        self.质量认证 = -质量认证
        self.广告投资 = -广告投资
        self.其他 = -其他
        self.备注 = 备注

    def 合计(self):
        return sum([self.开拓市场, self.资格认证, self.质量认证, self.广告投资, self.其他])


class 人力部门:
    # 招聘 = ""
    # 薪资 = 0
    # 辞退 = 0
    # 培训 = 0
    # 涨薪 = 0
    # 激励 = 0
    # 其他 = 0
    # 备注 = ""

    def __init__(self, 招聘="", 薪资=0, 辞退=0, 培训=0, 涨薪=0, 激励=0, 其他=0, 备注=""):
        self.招聘 = ""
        self.薪资 = -薪资
        self.辞退 = -辞退
        self.培训 = -培训
        self.涨薪 = -涨薪
        self.激励 = -激励
        self.其他 = -其他
        self.备注 = 备注

    def 合计(self):
        return sum([self.薪资, self.辞退, self.培训, self.涨薪, self.激励, self.其他])


class 生产部门:
    # 原材料延迟付款 = 0
    # 生产线 = 0
    # 产品设计 = 0
    # 原材料 = 0
    # 开产费用 = 0
    # 产线维修费 = 0
    # 转产费 = 0
    # 出售资产 = 0
    # 折旧费 = 0
    # 其他 = 0
    # 备注 = ""
    # 库存余量 = 0  # 仅用于计算权益

    def __init__(self, 原材料延迟付款=0, 生产线=0, 产品设计=0, 原材料=0, 开产费用=0, 产线维修费=0, 转产费=0, 出售资产=0, 折旧费=0, 其他=0, 备注="", 库存余量=0):
        self.原材料延迟付款 = -原材料延迟付款
        self.生产线 = -生产线
        self.产品设计 = -产品设计
        self.原材料 = -原材料
        self.开产费用 = -开产费用
        self.产线维修费 = -产线维修费
        self.转产费 = -转产费
        self.出售资产 = 出售资产
        self.折旧费 = -折旧费
        self.其他 = -其他
        self.备注 = 备注
        self.库存余量 = 库存余量

    def 合计(self):
        return sum([self.生产线, self.产品设计, self.原材料延迟付款, self.开产费用, self.产线维修费, self.转产费, self.出售资产, self.折旧费, self.其他])

    def 预算(self):
        return sum([self.生产线, self.产品设计, self.原材料, self.开产费用, self.产线维修费, self.转产费, self.出售资产, self.折旧费, self.其他])
