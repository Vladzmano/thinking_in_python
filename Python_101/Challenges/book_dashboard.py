import unittest

def display_sorted_books(book_ids, overdue_ids):
    found = False

    def helper(id):
        nonlocal found  # Utilizamos nonlocal para acceder a la variable found en el alcance exterior
        if id in overdue_ids:
            found = True
            return (0, id)
        return (1, id)

    book_ids.sort(key=helper)
    return found

class TestDisplaySortedBooks(unittest.TestCase):

    def test_no_overdue_books(self):
        book_ids = [1001, 1003, 1004, 1005, 1007, 1008, 1009]
        overdue_ids = {1002, 1006}
        self.assertFalse(display_sorted_books(book_ids, overdue_ids))

    def test_some_overdue_books(self):
        book_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
        overdue_ids = {1002, 1006}
        self.assertTrue(display_sorted_books(book_ids, overdue_ids))

if __name__ == '__main__':
    unittest.main()

