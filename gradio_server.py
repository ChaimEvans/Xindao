import json
import pickle
import time
import gradio as gr
from 配置 import *
from 时间线 import *
from 各部门 import *
from 贷款 import *
from plt_image import *

# f"{i // 4 + 1}年{i % 4 + 1}季"
quarter_texts = ['1年1季',
                 '1年2季',
                 '1年3季',
                 '1年4季',
                 '2年1季',
                 '2年2季',
                 '2年3季',
                 '2年4季',
                 '3年1季',
                 '3年2季',
                 '3年3季',
                 '3年4季',
                 '4年1季',
                 '4年2季',
                 '4年3季',
                 '4年4季']
quarter_colors = ["#4fc160", "#63a5f1", "#ad63f1", "#f16363"]

tl = 时间线()

当前季 = 4

# 生产
块_生产 = []
生产线 = []
产品设计 = []
原材料 = []
开产费用 = []
产线维修费 = []
转产费 = []
库存余量 = []
出售资产 = []
折旧费 = []
其他_生产 = []
备注_生产 = []
预算_生产 = []  # 输出
# 营销
块_营销 = []
开拓市场 = []
资格认证 = []
质量认证 = []
广告投资 = []
其他_营销 = []
备注_营销 = []
预算_营销 = []  # 输出
# 人力
块_人力 = []
招聘 = []
薪资 = []
辞退 = []
培训 = []
涨薪 = []
激励 = []
其他_人力 = []
备注_人力 = []
预算_人力 = []  # 输出
# 财务
块_财务 = []
收入 = []
还贷 = []  # 输出
贷款类型 = []  #
贷款额度 = []  #
其他_财务 = []
备注_财务 = []
预算_财务 = []  # 输出

with gr.Blocks(theme=gr.themes.Soft(), title="启星财务系统") as demo:
    # gr.HTML("<div style='text-align: center;font-size: large;'>启星财务系统</div>")
    with gr.Row():
        with gr.Column():
            with gr.Row():
                QuarterSelector = gr.Checkboxgroup(choices=["1年", "2年", "3年", "4年"], type="index", label="筛选年份")
                with gr.Row():
                    保存按钮 = gr.Button("保存", icon="Save.svg")
                    加载按钮 = gr.Button("加载", icon="Open.svg")
            with gr.Tabs():
                with gr.TabItem("生产"):
                    for i in range(16):
                        gr.HTML(
                            f"<div style='background-color: {quarter_colors[int(i / 4)]}; color: white; padding: 5px; text-align: center; border-radius: 5px;'>{quarter_texts[i]}</div>")
                        with gr.Column(visible=False) as 块:
                            with gr.Row():
                                生产线.append(gr.Number(label="生产线"))
                                产品设计.append(gr.Number(label="产品设计"))
                                原材料.append(gr.Number(label="原材料"))
                            with gr.Row():
                                开产费用.append(gr.Number(label="开产费用"))
                                产线维修费.append(gr.Number(label="产线维修"))
                                转产费.append(gr.Number(label="转产费"))
                            with gr.Row():
                                库存余量.append(gr.Number(label="库存余量(仅影响权益)"))
                                出售资产.append(gr.Number(label="出售资产"))
                                折旧费.append(gr.Number(label="折旧费"))
                            with gr.Row():
                                其他_生产.append(gr.Number(label="其他"))
                                备注_生产.append(gr.Text(label="备注"))
                            with gr.Row():
                                预算_生产.append(gr.Label("未初始化", label="预算"))
                        块_生产.append(块)

                with gr.TabItem("营销"):
                    for i in range(16):
                        gr.HTML(
                            f"<div style='background-color: {quarter_colors[int(i / 4)]}; color: white; padding: 5px; text-align: center; border-radius: 5px;'>{quarter_texts[i]}</div>")
                        with gr.Column(visible=False) as 块:
                            with gr.Row():
                                开拓市场.append(gr.Number(label="开拓市场"))
                                资格认证.append(gr.Number(label="资格认证"))
                                质量认证.append(gr.Number(label="质量认证"))
                            with gr.Row():
                                广告投资.append(gr.Number(label="广告投资"))
                                其他_营销.append(gr.Number(label="其他"))
                            with gr.Row():
                                备注_营销.append(gr.Text(label="备注"))
                            with gr.Row():
                                预算_营销.append(gr.Label("未初始化", label="预算"))
                        块_营销.append(块)

                with gr.TabItem("人力"):
                    for i in range(16):
                        gr.HTML(
                            f"<div style='background-color: {quarter_colors[int(i / 4)]}; color: white; padding: 5px; text-align: center; border-radius: 5px;'>{quarter_texts[i]}</div>")
                        with gr.Column(visible=False) as 块:
                            with gr.Row():
                                招聘.append(gr.Text(label="招聘"))
                                薪资.append(gr.Number(label="薪资"))
                                辞退.append(gr.Number(label="辞退"))
                            with gr.Row():
                                培训.append(gr.Number(label="培训"))
                                涨薪.append(gr.Number(label="涨薪"))
                                激励.append(gr.Number(label="激励"))
                            with gr.Row():
                                其他_人力.append(gr.Number(label="其他"))
                                备注_人力.append(gr.Text(label="备注"))
                            with gr.Row():
                                预算_人力.append(gr.Label("未初始化", label="预算"))
                        块_人力.append(块)

                with gr.TabItem("财务"):
                    for i in range(16):
                        gr.HTML(
                            f"<div style='background-color: {quarter_colors[int(i / 4)]}; color: white; padding: 5px; text-align: center; border-radius: 5px;'>{quarter_texts[i]}</div>")
                        with gr.Column(visible=False) as 块:
                            with gr.Row():
                                收入.append(gr.Number(label="收入"))
                                其他_财务.append(gr.Number(label="其他"))
                                备注_财务.append(gr.Text(label="备注"))
                            with gr.Row():
                                贷款类型.append(
                                    gr.Radio(["融资", "短贷", "长贷"], value="融资", type="index", label="贷款类型"))
                                贷款额度.append(gr.Number(label="贷款额度"))
                            with gr.Row():
                                还贷.append(gr.Number(0, label="还贷"))
                                gr.Number(-配置.管理费, label="管理费")
                            with gr.Row():
                                预算_财务.append(gr.Label("未初始化", label="本季投入"))
                        块_财务.append(块)
        with gr.Column():
            with gr.Row():
                当前季选择器 = gr.Dropdown(quarter_texts, value=quarter_texts[当前季], type="index", label="当前季")
                gr.Button("导出(未实现)", icon="Export.svg")
            现金 = gr.Label("未初始化", label="现金")
            权益 = gr.Label("未初始化", label="权益")
            利润 = gr.Label("未初始化", label="利润")
            负债 = gr.Label("未初始化", label="负债")
            d = tl.综合费用表(0, 0)
            dd = [list(pair) for pair in zip(d[0], d[1])]
            with gr.Row():
                综合费用表1 = gr.DataFrame(dd[:12], label="综合费用表")
                综合费用表2 = gr.DataFrame(dd[12:] + [["", ""]], label="综合费用表")
            各部门投入占比 = gr.Image(draw_pie([1], ["未初始化"]), label="各部门投入占比")
            走势 = gr.Image(
                draw_plots(quarter_texts, [[i for i in range(16)], sorted([i for i in range(16)], reverse=True)],
                           ["1", "2"]), label="投入、利润走势")

            with gr.Tabs():
                with gr.TabItem("交流"):
                    聊天 = gr.Chatbot(label="交流")
                    聊天输入 = gr.Textbox(label="发送内容")
                    聊天记录 = [("按下回车键发送消息", "")]


                    def 事件_聊天输入(text):
                        global 聊天记录
                        if len(聊天记录) > 50:
                            聊天记录 = 聊天记录[-50:]
                        聊天记录.append((text, ""))
                        return [聊天记录, ""]


                    聊天输入.submit(fn=事件_聊天输入, inputs=聊天输入, outputs=[聊天, 聊天输入])
                with gr.TabItem("指令"):
                    Python指令 = gr.Code(label="Python指令", value="sum(j.生产部门.原材料 for j in tl.所有季度[:3])",
                                         language="python")
                    Python指令按钮 = gr.Button("运行", icon="Play.svg")
                    Python指令输出 = gr.TextArea(label="Python指令输出")
                    Python指令按钮.click(fn=lambda a: eval(a), inputs=Python指令, outputs=Python指令输出)


    # -----年份筛选------

    def select_quarter(indexs):
        ret = []
        for i in range(4):
            if i in indexs:
                for j in range(4):
                    ret.append(gr.update(visible=True))
            else:
                for j in range(4):
                    ret.append(gr.update(visible=False))
        return ret + ret + ret + ret


    QuarterSelector.change(fn=select_quarter,
                           inputs=QuarterSelector,
                           outputs=块_生产 + 块_营销 + 块_人力 + 块_财务
                           )

    # -----刷新------

    所有输出 = 预算_生产 + 预算_营销 + 预算_人力 + 预算_财务 + 还贷 + [现金, 权益, 利润, 负债, 综合费用表1, 综合费用表2,
                                                                       各部门投入占比, 走势]


    def 刷新数据():
        tl.刷新()
        data = []
        for i in range(16):
            data.append(f"￥{-tl.所有季度[i].生产部门.预算()}")
        for i in range(16):
            data.append(f"￥{-tl.所有季度[i].营销部门.合计()}")
        for i in range(16):
            data.append(f"￥{-tl.所有季度[i].人力部门.合计()}")
        for i in range(16):
            data.append(f"￥{-tl.所有季度[i].投入}")
        for i in range(16):
            data.append(-tl.所有季度[i].还款)
        data.append(f"￥{tl.所有季度[当前季].结算现金}")
        data.append(f"￥{tl.所有季度[当前季].权益}")
        data.append(f"￥{tl.所有季度[当前季].利润}")
        data.append(f"￥{tl.获取当前未还贷款总额(当前季)}")

        综合费用表data = tl.综合费用表((当前季 // 4) * 4, 当前季)

        dd = [list(pair) for pair in zip(综合费用表data[0], 综合费用表data[1])]
        data.append(dd[:12])
        data.append(dd[12:] + [["", ""]])

        data.append(tl.绘制综合费用图(0, 0, 综合费用表=综合费用表data))

        data.append(
            draw_plots(quarter_texts,
                       [[-j.投入 for j in tl.所有季度], [-j.利润 for j in tl.所有季度]],
                       ["投入", "利润"]))

        return data


    def 构建改动函数(季ID, 部门, 属性):
        def 改动函数(value):
            if (type(value) == int or type(
                    value) == float) and 属性 != "收入" and 属性 != "出售资产" and 属性 != "库存余量":
                value = -value
            if 部门 == "财务部门":
                setattr(tl.所有季度[季ID], 属性, value)
            else:
                setattr(getattr(tl.所有季度[季ID], 部门), 属性, value)
            return 刷新数据()

        return 改动函数


    def 设置用户输入事件(目标集合, 部门, 属性):
        for i, item in enumerate(目标集合):
            item.change(fn=构建改动函数(i, 部门, 属性),
                        inputs=item,
                        outputs=所有输出
                        )


    设置用户输入事件(生产线, "生产部门", "生产线")
    设置用户输入事件(产品设计, "生产部门", "产品设计")
    设置用户输入事件(原材料, "生产部门", "原材料")
    设置用户输入事件(开产费用, "生产部门", "开产费用")
    设置用户输入事件(产线维修费, "生产部门", "产线维修费")
    设置用户输入事件(转产费, "生产部门", "转产费")
    设置用户输入事件(库存余量, "生产部门", "库存余量")
    设置用户输入事件(出售资产, "生产部门", "出售资产")
    设置用户输入事件(折旧费, "生产部门", "折旧费")
    设置用户输入事件(其他_生产, "生产部门", "其他")
    设置用户输入事件(备注_生产, "生产部门", "备注")
    设置用户输入事件(开拓市场, "营销部门", "开拓市场")
    设置用户输入事件(资格认证, "营销部门", "资格认证")
    设置用户输入事件(质量认证, "营销部门", "质量认证")
    设置用户输入事件(广告投资, "营销部门", "广告投资")
    设置用户输入事件(其他_营销, "营销部门", "其他")
    设置用户输入事件(备注_营销, "营销部门", "备注")
    设置用户输入事件(招聘, "人力部门", "招聘")
    设置用户输入事件(薪资, "人力部门", "薪资")
    设置用户输入事件(辞退, "人力部门", "辞退")
    设置用户输入事件(培训, "人力部门", "培训")
    设置用户输入事件(涨薪, "人力部门", "涨薪")
    设置用户输入事件(激励, "人力部门", "激励")
    设置用户输入事件(其他_人力, "人力部门", "其他")
    设置用户输入事件(备注_人力, "人力部门", "备注")
    设置用户输入事件(收入, "财务部门", "收入")
    设置用户输入事件(其他_财务, "财务部门", "其他")
    设置用户输入事件(备注_财务, "财务部门", "备注")


    def 事件_当前季选择器(index):
        global 当前季
        当前季 = index
        return 刷新数据()


    当前季选择器.change(fn=事件_当前季选择器, inputs=当前季选择器, outputs=所有输出)


    # -----贷款------

    def 设置贷款(*输入):
        tl.所有贷款.clear()
        类型 = 输入[:16]
        额度 = 输入[16:]
        for i in range(16):
            if 额度[i] != 0:
                if 类型[i] == 0:
                    tl.所有贷款.append(直接融资(i, 额度[i]))
                elif 类型[i] == 1:
                    tl.所有贷款.append(短期贷款(i, 额度[i]))
                else:
                    tl.所有贷款.append(长期贷款(i, 额度[i]))
        return 刷新数据()


    贷款输入 = 贷款类型 + 贷款额度
    for i, item in enumerate(贷款类型):
        item.change(fn=设置贷款, inputs=贷款输入, outputs=所有输出)
    for i, item in enumerate(贷款额度):
        item.change(fn=设置贷款, inputs=贷款输入, outputs=所有输出)


    # -----初始化------

    def 初始化函数():
        data = []
        data += [-j.生产部门.生产线 for j in tl.所有季度]
        data += [-j.生产部门.产品设计 for j in tl.所有季度]
        data += [-j.生产部门.原材料 for j in tl.所有季度]
        data += [-j.生产部门.开产费用 for j in tl.所有季度]
        data += [-j.生产部门.产线维修费 for j in tl.所有季度]
        data += [-j.生产部门.转产费 for j in tl.所有季度]
        data += [-j.生产部门.折旧费 for j in tl.所有季度]
        data += [-j.生产部门.其他 for j in tl.所有季度]
        data += [j.生产部门.备注 for j in tl.所有季度]  # str
        data += [-j.营销部门.开拓市场 for j in tl.所有季度]
        data += [-j.营销部门.资格认证 for j in tl.所有季度]
        data += [-j.营销部门.质量认证 for j in tl.所有季度]
        data += [-j.营销部门.广告投资 for j in tl.所有季度]
        data += [-j.营销部门.其他 for j in tl.所有季度]
        data += [j.营销部门.备注 for j in tl.所有季度]  # str
        data += [j.人力部门.招聘 for j in tl.所有季度]  # str
        data += [-j.人力部门.薪资 for j in tl.所有季度]
        data += [-j.人力部门.辞退 for j in tl.所有季度]
        data += [-j.人力部门.培训 for j in tl.所有季度]
        data += [-j.人力部门.涨薪 for j in tl.所有季度]
        data += [-j.人力部门.激励 for j in tl.所有季度]
        data += [-j.人力部门.其他 for j in tl.所有季度]
        data += [j.人力部门.备注 for j in tl.所有季度]  # str
        data += [j.收入 for j in tl.所有季度]
        data += [-j.其他 for j in tl.所有季度]
        data += [j.备注 for j in tl.所有季度]  # str
        贷款类型data = ["融资" for i in range(16)]
        贷款额度data = [0 for i in range(16)]
        for d in tl.所有贷款:
            index = d.申请季ID
            if type(d) == 短期贷款:
                贷款类型data[index] = "短贷"
            elif type(d) == 长期贷款:
                贷款类型data[index] = "长贷"
            贷款额度data[index] = d.贷款额度
        data += 贷款类型data
        data += 贷款额度data
        data.append(quarter_texts[当前季])
        data.append(聊天记录)
        return data


    所有输出 = 生产线 + 产品设计 + 原材料 + 开产费用 + 产线维修费 + 转产费 + 折旧费 + 其他_生产 + 备注_生产 + 开拓市场 + 资格认证 + 质量认证 + 广告投资 + 其他_营销 + 备注_营销 + 招聘 + 薪资 + 辞退 + 培训 + 涨薪 + 激励 + 其他_人力 + 备注_人力 + 收入 + 其他_财务 + 备注_财务 + 贷款类型 + 贷款额度 + [
        当前季选择器, 聊天]

    demo.load(fn=初始化函数, outputs=所有输出)


    def 加载():
        global tl
        tl = 时间线()
        with open("save.pk", "rb") as fp:
            data = pickle.load(fp, encoding="utf8")
        # with open("save.json") as fp:
        #     data = json.load(fp)
        return data


    加载按钮.click(fn=加载, outputs=所有输出)


    def 保存():
        with open("save.pk", "wb") as fp:
            pickle.dump(初始化函数(), fp)
        # with open("save.json", mode="w") as fp:
        #     json.dump(初始化函数(), fp, ensure_ascii=False)
        gr.Info("完成")


    保存按钮.click(fn=保存)

demo.launch()

sum(j.生产部门.原材料 for j in tl.所有季度[:3])
