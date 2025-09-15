# tests/test_cli.py
from typer.testing import CliRunner

from ai_project.cli import app

runner = CliRunner()


def test_preprocess_ok():
    r = runner.invoke(app, ["preprocess"])
    assert r.exit_code == 0
    assert "preprocess: ok" in r.stdout


def test_train_ok():
    r = runner.invoke(app, ["train"])
    assert r.exit_code == 0
    assert "train: ok" in r.stdout


def test_infer_ok():
    r = runner.invoke(app, ["infer", "--x", "7"])
    assert r.exit_code == 0
    # 依你 CLI 的輸出調整這行字串檢查：
    assert "pred" in r.stdout
