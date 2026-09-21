def cal_total(marks):
    return sum(marks)

def cal_avg(marks):
    return sum(marks)/len(marks)

def cal_grade(avg):
    if avg*10 >= 90:
        return 'A+'
    elif avg*10 >= 80:
        return 'A'
    elif avg*10 >= 70:
        return 'B'
    elif avg*10 >= 60:
        return 'C'
    elif avg*10 >= 50:
        return 'D'
    else:
        return 'F'

