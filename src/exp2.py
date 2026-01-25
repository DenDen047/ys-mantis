import os
from collections import OrderedDict

import plotly.graph_objects as go
from loguru import logger

from utils.plot_style import plotly_scientific_style

DATA = OrderedDict([
    ('1', 146),
    ('2', 8),
    ('3', 2),
    ('4', 1),
])  # fmt: skip


if __name__ == "__main__":
    labels = list(DATA.keys())
    values = [DATA[label] for label in labels]  # それぞれ整数値
    errors = [0] * len(labels)  # 誤差は指定できない（単一値なので0）

    logger.info(f"values: {values}")

    fig = go.Figure(
        data=[
            go.Bar(
                x=labels,
                y=values,
            )
        ]
    )

    fig.update_layout(
        xaxis_title="ストライクを試みたタイミング",
        yaxis_title="観測回数",
    )

    fig = plotly_scientific_style(fig)
    # PDFでファイル出力
    os.makedirs("output", exist_ok=True)
    fig.write_image("output/exp2.pdf", format="pdf")
    logger.info("PDFファイルを 'exp2.pdf' として保存しました。")

    fig.show()
