def calc_total(marks_dict):
    """Calculates sum of marks across all 4 subjects."""
    return sum(marks_dict.values())
    
def calc_percent(total_marks):
    """Calculates percentage based on 400 total possible marks."""
    return (total_marks / 400.0) * 100
    
def grade_calc(percentage):
    """Returns letter grade based on calculated percentage."""
    if percentage >= 90:
        return "S (Outstanding)"
    elif percentage >= 80:
        return "A (Excellent)"
    elif percentage >= 70:
        return "B (Good)"
    elif percentage >= 60:
        return "C (Average)"
    elif percentage >= 50:
        return "D (Pass)"
    else:
        return "F (Fail)"