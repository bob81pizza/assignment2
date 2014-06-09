import unittest
from BankApplication import Bank, BankAccount

class testThis(unittest.TestCase):
	def setUp(self):
		self.b = Bank()

	def test1(self):
		self.assertEqual(self.b.getNextAccountNumber(),1)
		self.assertEqual(self.b.getNextAccountNumber(),2)

	def test2(self):
		#self.assertEqual(self.b.getNextAccountNumber(),2)
		pass

	def test3(self):
		b2 = BankAccount(4)
		self.assertEqual(b2.getAccountNumber(),4)

if __name__ == '__main__':
	unittest.main(verbosity=2)