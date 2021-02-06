import unittest

from com.va.week5.Elevator import Elevator


class TestElevator(unittest.TestCase):

    def test_up_default(self):
        elevator = Elevator(-1, 10, 0)
        self.assertEqual(elevator.up(), 1)

    def test_down_default(self):
        elevator = Elevator(-1, 10, 0)
        self.assertEqual(elevator.down(), -1)

    def test_goto_fifth(self):
        elevator = Elevator(-1, 10, 0)
        self.assertEqual(elevator.go_to(5), 5)

    def test_up_twice(self):
        """test up twice"""
        elevator = Elevator(-1, 10, 0)
        elevator.up()
        self.assertEqual(elevator.up(), 2)

    def test_down_twice(self):
        """test down twice"""
        elevator = Elevator(-1, 10, 0)
        elevator.down()
        self.assertEqual(elevator.down(), -1)

    def test_up_ninth(self):
        """test up should return top floor when elevator is at floor 9"""
        elevator = Elevator(-1, 10, 0)
        elevator.go_to(9)
        self.assertEqual(elevator.up(), 10)

    def test_up_tenth(self):
        """test up should return top floor when elevator is at floor 10"""
        elevator = Elevator(-1, 10, 0)
        elevator.go_to(10)
        self.assertEqual(elevator.up(), 10)

    def test_down_tenth(self):
        """test down should return -1 when elevator is at floor -1"""
        elevator = Elevator(-1, 10, 0)
        elevator.go_to(10)
        self.assertEqual(elevator.down(), 9)

    def test_down_bottom(self):
        """test down should return -1 when elevator is at floor -1"""
        elevator = Elevator(-1, 10, 0)
        elevator.go_to(-1)
        self.assertEqual(elevator.down(), -1)

    def test_goto_below_bottom(self):
        elevator = Elevator(-1, 10, 0)
        self.assertEqual(elevator.go_to(-2), -1)

    def test_goto_above_top(self):
        elevator = Elevator(-1, 10, 0)
        self.assertEqual(elevator.go_to(11), 10)







if __name__ == '__main__':
    unittest.main()

