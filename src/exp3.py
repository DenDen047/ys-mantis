import os
from collections import OrderedDict

import numpy as np
import plotly.graph_objects as go
from loguru import logger

from utils.plot_style import plotly_scientific_style

DATA = OrderedDict([
    ('オオ1', [3, 1, 1, 1, 3, 1, 1, 1, 2, 3, 3, 1, 2, 1, 1, 1, 9, 1, 2, 1, 1, 1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ('オオ3', [0, 0, 0, 0, 11, 15, 7, 0, 3, 1, 0, 5, 2]),
    ('オオ4', [1, 3, 1, 4, 1, 2, 3, 3, 1, 2, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ('オオ5', [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1, 1, 0, 0, 0, 0, 4, 1, 0, 0, 0, 5, 1, 4, 2, 0, 5]),
    ('オオ6', [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0]),
    ('オオ7', [0, 0, 0, 0, 2]),
    ('ハラ2', [2, 2, 15, 1, 1, 3, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
])  # fmt: skip


if __name__ == "__main__":
    labels = list(DATA.keys())
    values = [np.mean(DATA[label]) for label in labels]
    errors = [np.std(DATA[label]) for label in labels]
    logger.info(f"means: {[float(v.round(2)) for v in values]}")

    fig = go.Figure(
        data=[
            go.Bar(
                x=labels,
                y=values,
                error_y=dict(type="data", array=errors, visible=True),
            )
        ]
    )

    fig.update_layout(
        xaxis_title="Species",
        yaxis_title="Average Number of Strikes",
    )

    fig = plotly_scientific_style(fig)
    # PDFでファイル出力
    os.makedirs("output", exist_ok=True)
    fig.write_image("output/exp3.pdf", format="pdf")
    logger.info("PDFファイルを 'exp3_plot.pdf' として保存しました。")

    fig.show()
