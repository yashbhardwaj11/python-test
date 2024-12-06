import sys
import pandas as pd

def calculate_kpis(file_path):
    try:
        # Load the Excel file
        data = pd.read_excel(file_path)

        # Check if all required columns are present
        required_columns = [
            "Average Response Time (ms)", "Failed Responses",
            "Successful Responses", "CPU Usage (%)", "Memory Usage (MB)"
        ]
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Column '{column}' not found in the file.")

        # KPI Calculations
        avg_response_time = data["Average Response Time (ms)"].mean()
        throughput = data["Successful Responses"].sum()
        total_requests = throughput + data["Failed Responses"].sum()
        success_rate = (throughput / total_requests) * 100 if total_requests > 0 else 0
        failure_rate = (data["Failed Responses"].sum() / total_requests) * 100 if total_requests > 0 else 0
        avg_cpu_usage = data["CPU Usage (%)"].mean()
        avg_memory_usage = data["Memory Usage (MB)"].mean()

        # Print KPIs
        print("Average Response Time (ms):", avg_response_time)
        print("Throughput (Successful Responses):", throughput)
        print("Success Rate (%):", success_rate)
        print("Failure Rate (%):", failure_rate)
        print("Average CPU Usage (%):", avg_cpu_usage)
        print("Average Memory Usage (MB):", avg_memory_usage)

    except Exception as e:
        print("Error occurred while processing the file:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python kpi_calculator.py <path_to_excel_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    calculate_kpis(file_path)
