import plotly.graph_objects as go


def plotly_scientific_style(fig: go.Figure) -> go.Figure:
    """
    Style compliant with Nature journal figure requirements
    ref: https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/
    """
    fig.update_layout(
        template="simple_white",
        font={
            "family": "Helvetica, Arial",
            "size": 28,  # 300dpi環境での7pt相当（7 * 300/72 ≈ 29）
            "color": "black",
        },
        # 軸の設定（線を太く、目盛りを外側に）
        xaxis={
            "ticks": "outside",
            "tickwidth": 3,  # 線も太く調整
            "ticklen": 8,
            "showline": True,
            "linewidth": 3,  # 軸線も太く調整
            "linecolor": "black",
        },
        yaxis={
            "ticks": "outside",
            "tickwidth": 3,
            "ticklen": 8,
            "showline": True,
            "linewidth": 3,
            "linecolor": "black",
        },
        title={"font": {"size": 28}},
        legend={
            "font": {"size": 24}  # 凡例は少し小さめでもOK
        },
        width=1000,
        height=800,
        # 余白調整（文字が大きくなるのではみ出さないように自動調整）
        margin=dict(l=80, r=40, t=40, b=80),
    )
    return fig
