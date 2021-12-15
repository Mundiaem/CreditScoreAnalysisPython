import csv
from datetime import datetime
from operator import itemgetter


class MakeCreditAnalysis:
    data = []
    transaction_data = []
    analysisResults = {}

    def __init__(self, transactions_csv_file_path, n):
        self.path = transactions_csv_file_path
        self.n = n

    def readFile(self):
        file = open(self.path)
        csv_dict_reader = csv.DictReader(file)
        rows = []
        self.data = list(csv_dict_reader)

        # for l in mydata:
        #     dict_from_csv = dict(l)
        #     rows.append(dict(dict_from_csv))
        #
        # print(f"This is the data {rows}")
        file.close()

    def bubleSortData(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.data) - 1):
                if self.data[i]['Transaction Date'] > self.data[i + 1]['Transaction Date']:
                    # Swap the elements
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]

                    # print(f"Sorting: {self.data[i]['Transaction Date']}")
                    # Set the flag to True so we'll loop again
                    swapped = True
        # print('****AFTER SWAPPING***')
        # [print(x) for x in self.data]

    def removeRepeatedCustomerDayTrans(self):
        #print(len(self.data))
        for i in range(len(self.data) - 1):
            date_0 = self.data[i]['Transaction Date']
            date_1 = self.data[i + 1]['Transaction Date']
            customer_0 = self.data[i]['Customer ID']
            customer_1 = self.data[i + 1]['Customer ID']
            if date_0 is date_1 and customer_0 is customer_1:
                pass
                # print("Same data")
            else:
                self.transaction_data.append(self.data[i])

        # print(len(self.transaction_data))
        # [print(x) for x in self.transaction_data]

    def countAnalysis(self):
        for i in range(len(self.data)):
            date_0 = self.data[i]['Transaction Date']
            customer_0 = self.data[i]['Customer ID']
            count = 0
            previous_date = ''
            if previous_date == '':
                previous_date = datetime.fromisoformat(date_0)
            # print(f"{i}. comparison: {previous_date}  {customer_0}  ")
            if customer_0 in self.analysisResults:
                # print(f"{customer_0} : Exists")
                pass
            else:
                for k in range(len(self.data)):
                    current_date = datetime.fromisoformat(self.data[k]['Transaction Date'])
                    difference_in_days = (previous_date - current_date).days
                    # print(f"difference in days {difference_in_days}")
                    if customer_0 == self.data[k]['Customer ID'] and difference_in_days == -1:
                        # print(f"Customer {customer_0} : {count} {difference_in_days}")
                        count += 1
                    previous_date = current_date
                self.analysisResults.update({customer_0: count})

               # print(f"analysis: {self.analysisResults}")
        return self.analysisResults

    def sortAnalysedData(self):
        self.analysisResults = dict(sorted(self.analysisResults.items(), key=itemgetter(1), reverse=True))
        # print(self.analysisResults)
        return self.analysisResults

    def printItOut(self):
        print(list(self.analysisResults.keys())[0:self.n])
