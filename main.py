# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from makeAnalysis import MakeCreditAnalysis


def start():
    # Use a breakpoint in the code line below to debug your script.
    transactions_csv_file_path = "./interview_code_test/test_data/transaction_data_1.csv"
    analysis_1 = MakeCreditAnalysis(transactions_csv_file_path=transactions_csv_file_path, n=1)
    transactions_csv_file_path_1 = "./interview_code_test/test_data/transaction_data_2.csv"
    analysis_2 = MakeCreditAnalysis(transactions_csv_file_path=transactions_csv_file_path_1, n=3)
    transactions_csv_file_path_2 = "./interview_code_test/test_data/transaction_data_3.csv"
    analysis_3 = MakeCreditAnalysis(transactions_csv_file_path=transactions_csv_file_path_2, n=5)
    analysis_1.readFile()
    analysis_1.bubleSortData()
    analysis_1.removeRepeatedCustomerDayTrans()
    analysis_1.countAnalysis()
    analysis_1.sortAnalysedData()
    analysis_1.printItOut()
    analysis_2.readFile()
    analysis_2.bubleSortData()
    analysis_2.removeRepeatedCustomerDayTrans()
    analysis_2.countAnalysis()
    analysis_2.sortAnalysedData()
    analysis_2.printItOut()
    analysis_3.readFile()
    analysis_3.bubleSortData()
    analysis_3.removeRepeatedCustomerDayTrans()
    analysis_3.countAnalysis()
    analysis_3.sortAnalysedData()
    analysis_3.printItOut()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
