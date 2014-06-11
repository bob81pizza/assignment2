import unittest
from BankApplication import Bank, BankAccount

class testBank(unittest.TestCase):
	def setUp(self):
		self.b = Bank()

	def testInit(self):
		self.assertIsNotNone(self.b)


if __name__ == '__main__':
	unittest.main(verbosity=2)