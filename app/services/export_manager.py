import shutil
import plotly.io as pio

class ExportManager:
    def csv_bytes(self, df):
        return df.to_csv(index=False).encode("utf-8")

    def fig_png_bytes(self, fig) -> bytes:
        # Make sure Kaleido knows where Chromium is on Streamlit Cloud
        chrome_path = (
            shutil.which("chromium")
            or shutil.which("chromium-browser")
            or shutil.which("google-chrome")
        )
        if chrome_path:
            pio.kaleido.scope.chromium_executable = chrome_path

        return fig.to_image(format="png", engine="kaleido")
