from csv import DictReader

def readNL2SQLresult(csv_path):
    output = []
    with open(csv_path) as file:
        csv_data = DictReader(file)

        for row in csv_data:
            row['SQL_correct'] = 'Success' if row['SQL_correct'] == 'TRUE' else 'Fail'
            row['Error_1_Invalid_Column_Ref'] = 'Success' if row['Error_1_Invalid_Column_Ref'] == 'TRUE' else 'Fail'
            row['Error_2_Invalid_Table_Ref'] = 'Success' if row['Error_2_Invalid_Table_Ref'] == 'TRUE' else 'Fail'
            output.append(row)
    return output