import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

def my_function(path) -> 'dataframe':
    """

        This function takes input as path to excel file and returns the datframe

        """
    # Define variable to load the dataframe
    df = pd.read_excel(path)

    # print(df.head(2))
    # print(df.shape)
    return df


def check_url(row):
        title=row['title']
        print(title)
        title = title.replace(" ", "+")
        url = "https://confluence.walmart.com/pages/viewpage.action?spaceKey=ASDAENG&title="
        new_link =url+title
        return new_link


def fetch_url(path):
        df = my_function(path)
        # k=df.apply(check_url, axis=1)
        df['url']=df.apply(lambda x:check_url(x), axis=1)
        # df['url']=k
        print(df['url'])

path = "/Users/p0k01v9/Downloads/Project1/data.xlsx"
fetch_url(path)