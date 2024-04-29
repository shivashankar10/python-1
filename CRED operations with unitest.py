class Employee:
    def _init_(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

class EmployeeDatabase:
    def _init_(self):
        self.employees = {}

    def create_employee(self, emp_id, name, department):
        if emp_id in self.employees:
            raise ValueError("Employee ID already exists")
        self.employees[emp_id] = Employee(emp_id, name, department)

    def read_employee(self, emp_id):
        if emp_id not in self.employees:
            raise ValueError("Employee ID does not exist")
        return self.employees[emp_id]

    def update_employee(self, emp_id, name=None, department=None):
        if emp_id not in self.employees:
            raise ValueError("Employee ID does not exist")
        employee = self.employees[emp_id]
        if name:
            employee.name = name
        if department:
            employee.department = department

    def delete_employee(self, emp_id):
        if emp_id not in self.employees:
            raise ValueError("Employee ID does not exist")
        del self.employees[emp_id]

# Unit tests
import unittest

class TestEmployeeDatabase(unittest.TestCase):
    def setUp(self):
        self.db = EmployeeDatabase()
        self.db.create_employee(1, "John Doe", "HR")
        self.db.create_employee(2, "Jane Smith", "IT")

    '''def test_create_employee(self):
        self.db.create_employee(3, "Alice Johnson", "Finance")
        self.assertIn(3, self.db.employees)'''

    def test_read_employee(self):
        employee = self.db.read_employee(1)
        self.assertEqual(employee.name, "John Doe")

    def test_update_employee(self):
        self.db.update_employee(1, name="Johnathan Doe")
        employee = self.db.read_employee(1)
        self.assertEqual(employee.name, "Johnathan Doe")

    def test_delete_employee(self):
        self.db.delete_employee(1)
        self.assertNotIn(1, self.db.employees)

if __name__ == '__main__':
    unittest.main()