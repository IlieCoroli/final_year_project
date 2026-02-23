import pandas as pd
import numpy as np
import plotly.express as px

class VisualisationEngine:
    def __init__(self):
        # Nice, vivid palette for categorical colors (dates, categories, etc.)
        self.palette = px.colors.qualitative.Set2

    def xy_chart(self, chart_type: str, df: pd.DataFrame, x: str, y: str, color: str | None = None):
        if df is None or df.empty:
            raise ValueError("Dataset is empty.")

        template = "plotly_dark"

        if chart_type == "Bar":
            fig = px.bar(
                df, x=x, y=y, color=color,
                template=template,
                color_discrete_sequence=self.palette
            )
        elif chart_type == "Line":
            fig = px.line(
                df, x=x, y=y, color=color,
                template=template,
                color_discrete_sequence=self.palette
            )
        elif chart_type == "Scatter":
            fig = px.scatter(
                df, x=x, y=y, color=color,
                template=template,
                color_discrete_sequence=self.palette
            )
        else:
            raise ValueError(f"Unknown chart type: {chart_type}")

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend_title_text=color if color else None
        )
        return fig

    def histogram(self, df: pd.DataFrame, column: str, bins: int):
        if df is None or df.empty:
            raise ValueError("Dataset is empty.")

        fig = px.histogram(
            df, x=column, nbins=bins,
            template="plotly_dark",
            color_discrete_sequence=self.palette
        )
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        return fig

    def correlation_heatmap(self, df: pd.DataFrame, columns: list[str]):
        if df is None or df.empty:
            raise ValueError("Dataset is empty.")
        if not columns:
            raise ValueError("Select at least one numeric column.")

        corr = df[columns].corr(numeric_only=True)

        fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            template="plotly_dark"
        )
        fig.update_layout(
            title="Correlation Heatmap",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
        return fig
