from data_storage import students
from grade_calc import calc_total, calc_percent

def show_stats():
    """Displays summary analytics for the class."""
    if not students:
        print("[!] No student records found.")
        return
        
    total_pct_sum = 0
    evaluated_count = 0
    top_scorer = ""
    highest_pct = -1.0

    for roll_no, data in students.items():
        if data["marks"]:
            tot = calc_total(data["marks"])
            pct = calc_percent(tot)
            total_pct_sum += pct
            evaluated_count += 1
            
            if pct > highest_pct:
                highest_pct = pct
                top_scorer = data["name"]
                
    if evaluated_count == 0:
        print("[!] No marks recorded yet across any student")
        return
        
    avg_pct = total_pct_sum / evaluated_count
    print("\n--- CLASS PERFORMANCE ANALYTICS ---")
    print(f" Total Students Evaluated : {evaluated_count}")
    print(f" Class Average Percentage : {avg_pct: .2f}%")
    print(f" Top Scorer               : {top_scorer} ({highest_pct: .2f}%)")
    print("-----------------------------------\n")