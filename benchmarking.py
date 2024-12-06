import sys
import pandas as pd

def calculate_kpis(file_path):
    try:
        # Load the Excel file
        data = pd.ExcelFile(file_path)
        
        # Assuming the Excel file has specific sheets for each KPI
        response_data = data.parse('ResponseTime')
        throughput_data = data.parse('Throughput')
        status_data = data.parse('Status')
        cpu_data = data.parse('CPU')
        memory_data = data.parse('Memory')

        # KPI Calculations
        avg_response_time = response_data['ResponseTime'].mean()
        total_throughput = throughput_data['Requests'].sum()
        success_rate = (status_data['Success'].sum() / status_data['Total'].sum()) * 100
        failure_rate = (status_data['Failure'].sum() / status_data['Total'].sum()) * 100
        avg_cpu_usage = cpu_data['CPUUsage'].mean()
        avg_memory_usage = memory_data['MemoryUsage'].mean()

        # Print KPIs
        print(avg_response_time)
        print(total_throughput)
        print(success_rate)
        print(failure_rate)
        print(avg_cpu_usage)
        print(avg_memory_usage)

    except Exception as e:
        print("Error occurred while processing the file:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python kpi_calculator.py <path_to_excel_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    calculate_kpis(file_path)
