angajat1 = {
    'nume': 'Ana-Maria Popescu',
    'departament': 'IT',
    'ID': 3409,
    'Salar': 4560,
}

angajat2 = {
    'nume': 'Marian Muntean',
    'departament': 'IT',
    'ID': 2235,
    'Salar': 4556,
}

angajat3 = {
    'nume': 'Maria Manea',
    'departament': 'HR',
    'ID': 1908,
    'Salar': 6755,
}

angajat4 = {
    'nume': 'Oana Popa',
    'departament': 'HR',
    'ID': 1977,
    'Salar': 5400,
}

angajat5 = {
    'nume': 'David Codru',
    'departament': 'Management',
    'ID': 1988,
    'Salar': 12900,
}

lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]

def give_employees_with_salary_above(employees: dict, salary: int) -> list[dict]:
    """
    Return a list of employees with salary above the given salary.
    """
    return [emp for emp in employees if emp['Salar'] > salary]

def give_list_of_employees_without_manager(employees: dict) -> list[dict]:
    """
    Return a list of employees without a manager.
    """
    return [emp for emp in employees if emp.get('departament') != "Management"]

def give_avg_salary_for_department(employees: dict, department: str) -> float:
    """
    Return the average salary for the given department.
    """
    return sum(emp['Salar'] for emp in employees if emp['departament'] == department) / len([emp for emp in employees if emp['departament'] == department])

if __name__ == "__main__":
    print(give_employees_with_salary_above(lista_dict, 5000))
    print(give_list_of_employees_without_manager(lista_dict))
    print(give_avg_salary_for_department(lista_dict, 'HR'))

    