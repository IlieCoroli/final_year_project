import shutil
import plotly.io as pio

class ExportManager:
    def csv_bytes(self, df) -> bytes:
        if df is None:
            return b""
        return df.to_csv(index=False).encode("utf-8")

    def fig_png_bytes(self, fig) -> bytes:
        if fig is None:
            raise ValueError("No figure provided.")

        # Ensure Kaleido knows where Chromium is on Streamlit Cloud
        chrome_path = (
            shutil.which("chromium")
            or shutil.which("chromium-browser")
            or shutil.which("google-chrome")
        )
        if chrome_path:
            pio.kaleido.scope.chromium_executable = chrome_path

        # Ensure export uses the same styling as UI
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        return fig.to_image(format="png", engine="kaleido")
