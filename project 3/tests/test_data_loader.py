from src.data.data_loader import load_csv


def test_load_csv_returns_dataframe(tmp_path):
    csv_path = tmp_path / "sample.csv"
    csv_path.write_text("a,b\n1,2\n", encoding="utf-8")
    df = load_csv(csv_path)
    assert len(df) == 1
