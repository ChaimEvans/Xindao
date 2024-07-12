import 配置


class 直接融资:
    def __init__(self, 当前季ID, 贷款额度):
        self.申请季ID = 当前季ID
        self.贷款额度 = 贷款额度
        self.总利息 = 配置.利率_直接融资 / 12 * 贷款额度 * 3 * 配置.期数_直接融资

    def 是否已还清(self, 当前季ID) -> bool:  # 付本金季为还清
        if 当前季ID >= self.申请季ID + 配置.期数_直接融资:
            return True
        return False

    def 是否已结束(self, 当前季ID) -> bool:  # 付本金后一季为结束
        if 当前季ID > self.申请季ID + 配置.期数_直接融资:
            return True
        return False

    def 获取当前还款(self, 当前季ID):
        if 当前季ID == self.申请季ID:
            return 0, False
        if self.是否已结束(当前季ID):
            return 0, True
        还款 = (self.总利息 + self.贷款额度) / 配置.期数_直接融资
        结束 = False
        if 当前季ID == self.申请季ID + 配置.期数_直接融资:
            结束 = True
        return 还款, 结束


class 短期贷款:
    def __init__(self, 当前季ID, 贷款额度):
        self.申请季ID = 当前季ID
        self.贷款额度 = 贷款额度
        self.总利息 = 配置.利率_短期贷款 / 12 * 贷款额度 * 3 * 配置.期数_短期贷款

    def 是否已还清(self, 当前季ID) -> bool:
        if 当前季ID >= self.申请季ID + 配置.期数_短期贷款:
            return True
        return False

    def 是否已结束(self, 当前季ID) -> bool:
        if 当前季ID > self.申请季ID + 配置.期数_短期贷款:
            return True
        return False

    def 获取当前还款(self, 当前季ID):
        if 当前季ID == self.申请季ID:
            return 0, False
        if self.是否已结束(当前季ID):
            return 0, True
        if 当前季ID == self.申请季ID + 配置.期数_短期贷款:
            return self.总利息 + self.贷款额度, True
        return 0, False


class 长期贷款:
    def __init__(self, 当前季ID, 贷款额度):
        self.申请季ID = 当前季ID
        self.贷款额度 = 贷款额度
        self.总利息 = 配置.利率_长期贷款 * 贷款额度 * 配置.期数_长期贷款

    def 是否已还清(self, 当前季ID) -> bool:
        if 当前季ID >= self.申请季ID + 配置.期数_长期贷款:
            return True
        return False

    def 是否已结束(self, 当前季ID) -> bool:
        if 当前季ID > self.申请季ID + 配置.期数_长期贷款:
            return True
        return False

    def 获取当前还款(self, 当前季ID):
        if 当前季ID == self.申请季ID:
            return 0, False
        if self.是否已结束(当前季ID):
            return 0, True
        还款 = self.总利息 / 配置.期数_长期贷款
        结束 = False
        if 当前季ID == self.申请季ID + 配置.期数_长期贷款:
            还款 += self.贷款额度
            结束 = True
        return 还款, 结束
