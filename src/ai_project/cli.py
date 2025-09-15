"""
AI 專案的命令列介面（CLI）
用法示例：
  uv run ai-cli preprocess
  uv run ai-cli train
  uv run ai-cli infer --x 3
"""

import typer

from .core import predict_value

app = typer.Typer(help="AI Project CLI")


@app.command()
def preprocess():
    """資料前處理（示範）。"""
    typer.echo("preprocess: ok")


@app.command()
def train():
    """模型訓練（示範）。"""
    typer.echo("train: ok")


@app.command()
def infer(x: int = 1):
    """推論（示範）。"""
    typer.echo({"pred": predict_value(x)})


if __name__ == "__main__":
    app()
