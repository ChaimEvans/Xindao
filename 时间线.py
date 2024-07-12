from 季度 import *
from 贷款 import *
import 配置
from plt_image import *


class 时间线:
    def __init__(self):
        self.所有季度: list[季度] = []
        self.所有贷款 = []
        for i in range(16):
            self.所有季度.append(季度(i, self))

    def 新增贷款(self, 贷):
        self.所有贷款.append(贷)
        self.所有季度[贷.申请季ID].贷款 = 贷.贷款额度

    def 获取当前未还贷款总额(self, 季ID):
        return sum(d.贷款额度 for d in self.所有贷款 if (季ID >= d.申请季ID and not d.是否已还清(季ID)))

    def 综合费用表(self, 起始ID, 季ID) -> (list, list):
        季ID += 1
        data = []
        data.append(-sum(j.生产部门.生产线 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.生产部门.产品设计 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.生产部门.原材料 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.生产部门.开产费用 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.生产部门.产线维修费 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.生产部门.转产费 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.生产部门.折旧费 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.生产部门.其他 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.营销部门.开拓市场 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.营销部门.资格认证 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.营销部门.质量认证 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.营销部门.广告投资 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.营销部门.其他 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.人力部门.薪资 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.人力部门.辞退 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.人力部门.培训 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.人力部门.涨薪 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.人力部门.激励 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.人力部门.其他 for j in self.所有季度[起始ID:季ID]))
        贷款合计 = sum(d.贷款额度 for d in self.所有贷款 if d.是否已还清(季ID))
        data.append(贷款合计)
        data.append(-sum(j.还款 for j in self.所有季度[起始ID:季ID]) - 贷款合计)
        data.append(-sum(j.违约金 for j in self.所有季度[起始ID:季ID]))
        data.append(-sum(j.其他 for j in self.所有季度[起始ID:季ID]))
        labels = ["生产线", "产品设计", "原材料", "开产费用", "产线维修费", "转产费", "折旧费", "其他(生产)",
                  "开拓市场", "资格认证", "质量认证", "广告投资", "其他(营销)",
                  "薪资", "辞退", "培训", "涨薪", "激励", "其他(人力)",
                  "贷款本金", "贷款利息", "违约金", "其他(财务)"]
        return labels, data

    def 绘制综合费用图(self, 起始ID, 季ID, 综合费用表=None) -> Image:
        labels, data = None, None
        if 综合费用表 is None:
            labels, data = self.综合费用表(起始ID, 季ID)
        else:
            labels, data = 综合费用表
        data = [max(0, i) for i in data]
        总投入 = sum(data)
        if 总投入 == 0:
            return Image.new("RGBA", (640, 480), 1)
        data = [i / 总投入 for i in data]
        return draw_pie(data, labels)

    def 获取固定资产(self, 季ID):
        return sum(季.生产部门.生产线 + 季.生产部门.原材料 - 季.生产部门.库存余量 for 季 in self.所有季度[:季ID + 1])

    def 刷新(self):
        贷款temp = self.所有贷款.copy()
        for 季 in self.所有季度:
            季.贷款 = 0
            季.还款 = 0
            for 贷 in 贷款temp:
                if 季.季度ID < 贷.申请季ID:
                    continue
                elif 季.季度ID == 贷.申请季ID:
                    季.贷款 = 贷.贷款额度
                还款, 结束 = 贷.获取当前还款(季.季度ID)
                季.还款 -= 还款
                if 结束:
                    贷款temp.remove(贷)
            季.刷新()


if __name__ == '__main__':
    _时间线_ = 时间线()
    _时间线_.刷新()
    print(_时间线_)
