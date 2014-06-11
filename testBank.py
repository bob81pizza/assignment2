import unittest
from BankApplication import Bank, BankAccount, Transaction
from unittest.mock import MagicMock

class testBank(unittest.TestCase):
	def setUp(self):
		self.b = Bank()

	'''
	Test to ensure the instantiated b is not null
	'''
	def testInit(self):
		self.assertIsNotNone(self.b)

	'''
	Test to ensure that b is an instance of Bank
	'''
	def testClass(self):
		self.assertIsInstance(self.b,Bank)

	'''
	Test to ensure an exception is raised if you try to get 
	an account that doesn't exist
	'''
	def testGetAccount(self):
		self.assertRaises(Exception, self.b.getAccount,2)

	'''
	USES MOCK
	Tests to ensure that getNextAccountNumber method is called from within addAccount

	'''
	def testMock(self):
		real = Bank()
		real.getNextAccountNumber = MagicMock()
		real.addAccount()
		real.getNextAccountNumber.assert_called_with()




if __name__ == '__main__':
	unittest.main(verbosity=2)