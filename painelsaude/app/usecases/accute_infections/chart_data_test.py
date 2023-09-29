from .chart_data import get_chart_data

def test_get_chart_data():
    date_range = ['2021-05-01', '2021-06-01']
    chart_date = get_chart_data(date_range=date_range)
    assert 216 == chart_date['count'].sum()
