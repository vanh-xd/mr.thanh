import sys
import os
import pandas as pd
import requests
from datetime import datetime
from PyQt6 import QtWidgets, QtCore
from ui_mainwindow import Ui_MainWindow


class MainWindow124Ex(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow124Ex, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize dataframe
        self.df = None

        # Connect buttons to functions
        self.ui.btnLoadData.clicked.connect(self.load_data)
        self.ui.btnShowAll.clicked.connect(self.show_all_employees)
        self.ui.btnFilterByYear.clicked.connect(self.filter_by_birth_year)
        self.ui.btnTop3Oldest.clicked.connect(self.top_3_oldest)
        self.ui.btnFilterTesters.clicked.connect(self.filter_testers)
        self.ui.btnCountByRole.clicked.connect(self.count_by_role)

    def load_data(self):
        """Download data and add 5 more employees with different data"""
        try:
            # Create dataset directory if it doesn't exist
            os.makedirs('ex124/dataset', exist_ok=True)

            # Try to download the dataset
            try:
                url = "https://tranduythanh.com/datasets/employee.csv"
                self.ui.txtResults.append(f"Attempting to download from {url}...")
                response = requests.get(url)

                if response.status_code == 200:
                    # Save the file
                    with open('ex124/dataset/employee.csv', 'wb') as f:
                        f.write(response.content)
                    self.ui.txtResults.append("File downloaded successfully.")

                    # Try to read the file
                    try:
                        self.df = pd.read_csv('ex124/dataset/employee.csv')
                        self.ui.txtResults.append(f"CSV loaded with columns: {list(self.df.columns)}")
                    except Exception as e:
                        self.ui.txtResults.append(f"Error reading CSV: {str(e)}")
                        # Create a new dataframe if reading fails
                        self.create_default_dataframe()
                else:
                    self.ui.txtResults.append(f"Failed to download data. Status code: {response.status_code}")
                    # Create a new dataframe if download fails
                    self.create_default_dataframe()
            except Exception as e:
                self.ui.txtResults.append(f"Error downloading data: {str(e)}")
                # Create a new dataframe if download fails
                self.create_default_dataframe()

            # If we still don't have a dataframe, create one
            if self.df is None or self.df.empty:
                self.create_default_dataframe()

            # Rename columns to standardize (before adding new employees)
            column_mapping = {
                'ID': 'id', 'Id': 'id',
                'NAME': 'name', 'Name': 'name',
                'DOB': 'DoB', 'Dob': 'DoB', 'dob': 'DoB', 'birth_year': 'DoB',
                'ROLE': 'role', 'Role': 'role',
                'GENDER': 'gender', 'Gender': 'gender'
            }

            # Only rename columns that exist
            rename_dict = {old: new for old, new in column_mapping.items() if old in self.df.columns}
            self.df = self.df.rename(columns=rename_dict)

            # Ensure all required columns exist
            for col in ['id', 'name', 'DoB', 'role', 'gender']:
                if col not in self.df.columns:
                    if col == 'id':
                        self.df[col] = range(1, len(self.df) + 1)
                    elif col == 'DoB':
                        self.df[col] = '01/01/2000'  # Default value
                    else:
                        self.df[col] = 'Unknown'  # Default value for missing columns

            # Check if DoB column contains only years and convert to DD/MM/YYYY format
            if pd.api.types.is_numeric_dtype(self.df['DoB']):
                self.df['DoB'] = self.df['DoB'].astype(str).apply(lambda x: f'01/01/{x}')
            elif self.df['DoB'].str.len().max() <= 4:  # If all values are 4 chars or less (likely years)
                self.df['DoB'] = self.df['DoB'].apply(lambda x: f'01/01/{x}')

            # Add 5 more employees with different data
            new_employees = pd.DataFrame({
                'id': [len(self.df) + i + 1 for i in range(5)],
                'name': ['John Doe', 'Jane Smith', 'Robert Johnson', 'Emily Davis', 'Michael Brown'],
                'DoB': ['15/06/1995', '22/03/2001', '10/08/1988', '05/12/2001', '30/09/1975'],
                'role': ['Developer', 'Tester', 'Manager', 'Designer', 'Tester'],
                'gender': ['Male', 'Female', 'Male', 'Female', 'Male']
            })

            # Append new employees to the dataframe
            self.df = pd.concat([self.df, new_employees], ignore_index=True)

            # Keep only required columns
            self.df = self.df[['id', 'name', 'DoB', 'role', 'gender']]

            # Save the updated dataframe
            self.df.to_csv('ex124/dataset/employee.csv', index=False)

            # Display success message
            self.ui.txtResults.append("Data loaded successfully and 5 new employees added.")

            # Show all employees
            self.show_all_employees()

        except Exception as e:
            self.ui.txtResults.append(f"Error in load_data: {str(e)}")
            import traceback
            self.ui.txtResults.append(traceback.format_exc())

    def create_default_dataframe(self):
        """Create a default dataframe with sample data"""
        self.ui.txtResults.append("Creating default employee dataset...")
        self.df = pd.DataFrame({
            'id': [1, 2, 3, 4],
            'name': ['Tuấn Kiệt', 'Khánh Hưng', 'Gia Hân', 'Ngọc Tú'],
            'DoB': ['12/02/2000', '22/04/2003', '06/08/2002', '02/02/2001'],
            'role': ['Web Developer', 'Tester', 'Business Analyst', 'Mobile App Developer'],
            'gender': ['Male', 'Male', 'Female', 'Female']
        })
        self.ui.txtResults.append("Default dataset created.")

    def show_all_employees(self):
        """Export all Employee data to console screen and table"""
        if self.df is None or self.df.empty:
            self.ui.txtResults.append("No data available. Please load data first.")
            return

        # Display in console/text browser
        self.ui.txtResults.append("\n--- All Employees ---")
        self.ui.txtResults.append(str(self.df))

        # Display in table
        self.display_dataframe_in_table(self.df)

    def filter_by_birth_year(self):
        """Filter out Employees born in the specified year"""
        if self.df is None or self.df.empty:
            self.ui.txtResults.append("No data available. Please load data first.")
            return

        # Get the year from the line edit
        year_text = self.ui.lineEditInputFilterYear.text().strip()

        if not year_text:
            self.ui.txtResults.append("Please enter a birth year to filter.")
            return

        try:
            filter_year = int(year_text)
            # Extract year from DoB column (format: DD/MM/YYYY)
            filtered_df = self.df[self.df['DoB'].str.extract(r'(\d{4})$')[0].astype(int) == filter_year]

            # Display in console/text browser
            self.ui.txtResults.append(f"\n--- Employees Born in {filter_year} ---")

            if filtered_df.empty:
                self.ui.txtResults.append(f"No employees found born in {filter_year}.")
            else:
                self.ui.txtResults.append(str(filtered_df))

            # Display in table
            self.display_dataframe_in_table(filtered_df)

        except ValueError:
            self.ui.txtResults.append("Invalid year format. Please enter a valid year (e.g., 2001).")

    def top_3_oldest(self):
        """Export TOP 3 Employees with oldest age"""
        if self.df is None or self.df.empty:
            self.ui.txtResults.append("No data available. Please load data first.")
            return

        try:
            # Convert DoB to datetime for sorting
            self.df['temp_date'] = pd.to_datetime(self.df['DoB'], format='%d/%m/%Y', errors='coerce')

            # Sort by date ascending (oldest first) and get top 3
            oldest_df = self.df.sort_values(by='temp_date').head(3)

            # Remove temporary column
            oldest_df = oldest_df.drop('temp_date', axis=1)
            self.df = self.df.drop('temp_date', axis=1)

            # Display in console/text browser
            self.ui.txtResults.append("\n--- Top 3 Oldest Employees ---")
            self.ui.txtResults.append(str(oldest_df))

            # Display in table
            self.display_dataframe_in_table(oldest_df)
        except Exception as e:
            self.ui.txtResults.append(f"Error finding oldest employees: {str(e)}")

    def filter_testers(self):
        """Filter out Employees with Tester role"""
        if self.df is None or self.df.empty:
            self.ui.txtResults.append("No data available. Please load data first.")
            return

        filtered_df = self.df[self.df['role'] == 'Tester']

        # Display in console/text browser
        self.ui.txtResults.append("\n--- Employees with Tester Role ---")
        self.ui.txtResults.append(str(filtered_df))

        # Display in table
        self.display_dataframe_in_table(filtered_df)

    def count_by_role(self):
        """Count the number of Employees by Role"""
        if self.df is None or self.df.empty:
            self.ui.txtResults.append("No data available. Please load data first.")
            return

        role_counts = self.df['role'].value_counts()

        # Display in console/text browser
        self.ui.txtResults.append("\n--- Employee Count by Role ---")
        self.ui.txtResults.append(str(role_counts))

        # Create a dataframe for display in table
        role_df = pd.DataFrame({
            'Role': role_counts.index,
            'Count': role_counts.values
        })

        # Clear the table
        self.ui.tableEmployees.setRowCount(0)
        self.ui.tableEmployees.setColumnCount(2)
        self.ui.tableEmployees.setHorizontalHeaderLabels(["Role", "Count"])

        # Add data to table
        for i, (_, row) in enumerate(role_df.iterrows()):
            self.ui.tableEmployees.insertRow(i)
            for j, value in enumerate(row):
                self.ui.tableEmployees.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

    def display_dataframe_in_table(self, df):
        """Display a dataframe in the QTableWidget"""
        # Clear the table
        self.ui.tableEmployees.setRowCount(0)
        self.ui.tableEmployees.setColumnCount(len(df.columns))
        self.ui.tableEmployees.setHorizontalHeaderLabels(df.columns)

        # Add data to table
        for i, (_, row) in enumerate(df.iterrows()):
            self.ui.tableEmployees.insertRow(i)
            for j, value in enumerate(row):
                self.ui.tableEmployees.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow124Ex()
    window.show()
    sys.exit(app.exec())

