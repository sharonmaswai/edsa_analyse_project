from analyse import analyse

def test_metrics_dict():
    assert analyse.dictionary_of_metrics(gauteng)=={'max': 39660.0, 'mean': 26244.42, 'median': 24403.5, 'min': 8842.0, 'std': 10400.01, 'var': 108160153.17}, 'Failed'

def test_summary():
    assert analyse.five_num_summary(gauteng)=={'max': 39660.0, 'median': 24403.5,'min': 8842.0,'q1': 18653.0,'q3': 36372.0}, 'Failed'
def test_date_parse():
    assert date_parser([:3])==['2019-11-29', '2019-11-29', '2019-11-29'], 'Failed'
    assert date_parser([:-3])== ['2019-11-20', '2019-11-20', '2019-11-20'], 'Failed'