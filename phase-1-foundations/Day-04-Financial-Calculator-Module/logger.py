import datetime

def log_calculation(calculation_type, inputs, result, filename="calculations.log"):
    # 1. Get today's date in YYYY-MM-DD format
    today = datetime.datetime.now().strftime("%Y-%m-%d") 
    # 2. Format the exact string (Date | Type | Inputs | Result)
    log_entry = f"{today} | {calculation_type} | {inputs} | result={result}\n"
    # 3. Append the log entry to the log file  
    with open(filename, "a") as log_file:
        log_file.write(log_entry)