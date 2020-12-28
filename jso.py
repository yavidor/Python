import pandas as pd
js = pd.read_json("StreamingHistory0.json").append(pd.read_json("StreamingHistory1.json")).append(pd.read_json("StreamingHistory2.json")).groupby(['artistName', 'trackName']).sum().div(3600000).sort_values(['msPlayed']).query('msPlayed > .1')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(js)
js.to_csv("songs.csv")