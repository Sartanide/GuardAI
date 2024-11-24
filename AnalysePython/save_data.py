import csv

def saveDataCsv(results: list, filename: str = '-result-test.csv', save_path: str = ""):
    head = ['type', 'nombre de correct', 'total', 'pourcentage']
    rows = []
    for resultList, name in results:
        for key, result in resultList.items():
            percent = result[0] / result[1] * 100
            rows.append([str(key), str(result[0]), str(result[1]), str("%.3f" % percent) + "%"])
        print(rows)
        with open(save_path + name + "-" + filename + '.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(head)

            # write multiple rows
            writer.writerows(rows)
            f.close()