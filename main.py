import pandas as pd
import db as db
from inshorts import getNews


def fetchdata(cat_list):
    dflist = []
    for cat in cat_list:
        resp = getNews(cat)
        cat = resp["category"]
        data = resp["data"]
        df = pd.DataFrame(data, index=None)
        df["Category"] = cat
        dflist.append(df)
    maindf = pd.concat(dflist)
    db.append_row(maindf)


if __name__ == "__main__":
    category = ["technology", "startup", "science", "business", "world", "india"]
    fetchdata(category)
