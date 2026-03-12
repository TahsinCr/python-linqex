from linqex import Enumerable

class EmployeeDirectory:
    """
    Demonstrates how to use PyLINQ to join disparate data sources 
    (e.g., matching a list of Users from a REST API to a list of Departments from a Database).
    """

    def __init__(self):
        self.employees = [
            {"emp_id": 1, "name": "Alice", "dept_id": 101},
            {"emp_id": 2, "name": "Bob",   "dept_id": 102},
            {"emp_id": 3, "name": "Eve",   "dept_id": 101},
            {"emp_id": 4, "name": "Dave",  "dept_id": 999} # Department doesn't exist
        ]
        
        self.departments = [
            {"id": 101, "name": "Engineering", "location": "Building A"},
            {"id": 102, "name": "Sales",       "location": "Building B"},
            {"id": 103, "name": "Marketing",   "location": "Building C"}
        ]

    def get_employee_department_mapping(self):
        """
        Performs an Inner Join between Employees and Departments.
        Employees without a valid department (like Dave) are automatically excluded.
        """
        emp_stream = Enumerable(self.employees)
        dept_stream = Enumerable(self.departments)

        mapped_data = emp_stream.join(
            inner=dept_stream,
            # outer_key: What property on Employee matches the Department?
            outer_key=lambda emp: emp["dept_id"],
            # inner_key: What property on Department matches the Employee?
            inner_key=lambda dept: dept["id"],
            # selector: How should the combined result look?
            selector=lambda emp, dept: {
                "employee_name": emp["name"],
                "department_name": dept["name"],
                "office": dept["location"]
            }
        ).to_list()

        return mapped_data

if __name__ == "__main__":
    directory = EmployeeDirectory()
    results = directory.get_employee_department_mapping()
    
    for row in results:
        print(f"{row['employee_name']} works in {row['department_name']} ({row['office']})")
