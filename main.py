import pandas as pd
import os

def delete_blank_rows(file_path):
    # Determine the new file name with "_no_blanks.xlsx" appended
    base, ext = os.path.splitext(file_path)
    new_file_path = base + "_no_blanks" + ext

    # Create a new Excel writer object
    with pd.ExcelWriter(new_file_path, engine='openpyxl') as writer:
        # Load the Excel file
        with pd.ExcelFile(file_path) as xls:
            # Iterate over all sheets
            for sheet_name in xls.sheet_names:
                # Load each sheet as a DataFrame
                df = pd.read_excel(xls, sheet_name)

                # Remove rows where all cells are NaN (blank)
                df.dropna(how='all', inplace=True)

                # Write the modified DataFrame to the new Excel file
                df.to_excel(writer, sheet_name=sheet_name, index=False)

if __name__ == "__main__":
    file_path = input("Enter the path to your Excel file: ")
    delete_blank_rows(file_path)
    print("Blank rows deleted successfully. New file created without blank rows.")
