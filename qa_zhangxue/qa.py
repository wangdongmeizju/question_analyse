import pandas as pd

if __name__ == "__main__":
    file_name="questionnaire_export.xlsx"
    xls = pd.ExcelFile(file_name)
    print(xls.sheet_names[2])
    df = pd.read_excel(file_name,xls.sheet_names[2])
   #
    df_1=df[df["q1.1"] != "---" ]
    print(df_1["q1.1"])