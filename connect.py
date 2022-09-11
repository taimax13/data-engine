import matplotlib
import seaborn as seaborn
import pandas as pd
import matplotlib.pyplot as plt
from pandasql import sqldf

matplotlib.use('TkAgg')


class Connect:
    def __init__(self, file_name):
        self.file_name = file_name
        self.sd = seaborn.load_dataset(file_name)
        self.pd = pd.read_csv(file_name)

    def get_table(self):
        return self.pd.head()

    def get_data_types(self):
        return self.pd.dtypes

    def get_table_info(self):
        return self.pd.info()

    def get_table_info(self):
        return self.pd.describe()

    def get_headers(self):
        return list(self.pd.columns)

    def grouped_first_order_plot(self):
        headers = self.get_headers()
        for col_name in headers:
            self.group_by(col_name)
            try:
                dp = seaborn.displot(data=self.pd, x=col_name)
                plt.plot = dp
                plt.show()
            except:
                print("Indigestible {}".format(col_name))

    def correlation_first_order(self):
        headers = self.get_headers()
        counter = len(headers) - 1
        for col_name in headers:
            for x in range(counter):
                try:
                    self.correlation_groped(col_name, headers[x])
                except:
                    print("Indigestible {}".format(col_name))
            headers.remove(col_name)

    def group_by(self, name):
        return list(self.pd.groupby(name))

    def correlation_groped(self, cor1, cor2):
        ax = self.pd.hist(column=cor1, by=cor2, bins=3, sharex=True, sharey=True)
        plt.hist = ax
        plt.show()

    def count_in_field(self, name):
        return self.pd[name].value_counts()

    def select_distinct(self, col1, col2):
        q = """SELECT DISTINCT {}, {} FROM df;""".format(col1, col2)
        pysqldf = lambda q: sqldf(q, globals())
        return pysqldf(q)

    def view_pie_per_colonm(self):
        for key in self.pd.keys():
            q=self.pd[key].value_counts()
            print("###### {} #######".format(key))
            #print(q.max())
            #print(q.min())
            #print(q.mean())
            pie = q.plot.pie(figsize=(5, 5))
            plt.pie = pie
            plt.show()


    def print_info(self):
        self.pd.head()
        print(self.get_table_info())
        #q=self.pd.plot.scatter(x="id", y="age", alpha=0.5)
        #plt.plot=q
        #plt.show()
        plot=self.pd.plot()
        plt.plot=plot
        plt.show()
        self.view_pie_per_colonm()



       # groupby = self.pd.groupby(['age', 'sex'])['alive']#, 'sex'])['alive']#.value_counts()
       # print(self.pd.describe())

       # df = groupby.filter(lambda x: x['age'])
        #print(groupby.keys())



        #q = """SELECT DISTINCT age, fare FROM df;"""
        #pysqldf = lambda q: sqldf(q, globals())
        #a_df = pysqldf(q)

        self.pd.groupby('embark_town').agg({'age': min, 'fare': max})
        ##visualisation

        #print(ax)

    # print(self.group_by("age"))
    # print(self.count_in_field("age"))
    # self.print_table()
    # self.print_table_info()
    # Use a breakpoint in the code line below to debug your script.
    # print(self.titanic_pd.info())
    # print(self.titanic_pd.info())
    # print(self.is_alive())

    # sex= titanic_seaborn.sex
    # embark_town = titanic_seaborn.embark_town

    # series = pd.Series(data=sex, index=embark_town)
    # print(series)

    # print(series.loc['Southampton'])

    ##how many women to all was there %% survived
    # print(titanic.groupby(['sex'])['alive'].value_counts())
    ## same by class
    # print(titanic.groupby(['age'])['alive'])  #.value_counts())
    ## embarked by town

    ## adult

    ## was alone

    # print(titanic_seaborn.who.value_counts().plot)

    ##
    # print(titanic.head())
    # print("Who was on deck")
    # print(titanic.deck.unique())
    # print([titanic.pclass==1])
