import unittest
from BankApplication import Bank, BankAccount, Transaction
from unittest.mock import MagicMock

class testBank(unittest.TestCase):

	'''Create Bank object'''
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
	def testAddAccountUsingMock(self):
		real = Bank()
		real.getNextAccountNumber = MagicMock()
		real.addAccount()
		real.getNextAccountNumber.assert_called_with()


	'''Test to ensure that adding 1 account makes the Bank have 1 account in its list
	of BankAccounts.
	'''
	def testAddFirstAccount(self):
		self.b.addAccount()
		self.assertEqual(len(self.b.bankAccounts),1)


	'''Test to ensure that adding 3 accounts in succession makes the Bank have 3 accounts
	in its list of BankAccounts
	'''
	def testAddThreeAccounts(self):
		for i in range(3):
			self.b.addAccount()
		self.assertEqual(len(self.b.bankAccounts),3)

	




if __name__ == '__main__':
	unittest.main(verbosity=2)
