# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import connect as connect
import quote_spider as spider
# Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connect = connect.Connect('titanic')
    connect.print_info()
    #qs=spider.QuotesSpider()
    #qs.parse(qs.start_requests())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
