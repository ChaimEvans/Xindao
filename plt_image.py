import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PIL import Image

matplotlib.use('Agg')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'


def draw_pie(x, labels, autopct='%1.1f%%') -> Image:
    plot, ax = plt.subplots()
    ax.pie(x=x, labels=labels, autopct=autopct)
    # ax.legend(labels)
    canvas = FigureCanvas(plot)
    canvas.draw()
    image = Image.frombuffer("RGBA", canvas.get_width_height(), canvas.buffer_rgba())
    plt.close()
    return image


def draw_plot(x, y) -> Image:
    fig, ax = plt.subplots()
    ax.plot(x, y)
    canvas = FigureCanvas(fig)
    canvas.draw()
    image = Image.frombuffer("RGBA", canvas.get_width_height(), canvas.buffer_rgba())
    plt.close()
    return image


def draw_plots(x, ys: list[list], legend, rotation=-30) -> Image:
    fig, ax = plt.subplots()
    ax.set_xticks([i for i in range(len(x))], labels=x, rotation=rotation)
    for y in ys:
        ax.plot(y)
    ax.legend(legend)
    canvas = FigureCanvas(fig)
    canvas.draw()
    image = Image.frombuffer("RGBA", canvas.get_width_height(), canvas.buffer_rgba())
    plt.close()
    return image
