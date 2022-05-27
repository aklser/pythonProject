from pyecharts.charts import Bar, Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType

line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1000px", height="300px"))
    .add_xaxis(["3", "2", "23"])
    .add_yaxis("a", [12, 3, 435])
    .add_yaxis("b", [1, 334, 45])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
                         datazoom_opts=opts.DataZoomOpts(is_show=True))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
)
line.render("test.html")
line.render_notebook()
