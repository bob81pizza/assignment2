import unittest
from BankApplication import Bank, BankAccount, Transaction
from unittest.mock import MagicMock, patch

class testBank(unittest.TestCase):

	'''Create Bank object'''
	def setUp(self):
		self.b = Bank()


	'''
	Test to ensure the instantiated Bank b is not null
	'''
	def testInit(self):
		self.assertIsNotNone(self.b)


	'''
	Test to ensure that b is an instance of Bank
	'''
	def testClassType(self):
		self.assertIsInstance(self.b, Bank)


	'''
	Test to ensure an exception is raised if you try to get 
	an account that doesn't exist.
	Try to get an account while the bank has no accounts
	'''
	def testGetAccountFailure(self):
		self.assertRaises(Exception, self.b.getAccount,2)


	'''
	Test to ensure that after adding 1 account and then getting an account
	with account # = 1, a BankAccount object is returned
	'''
	def testGetAccountClassType(self):
		self.b.addAccount()
		self.assertIsInstance(self.b.getAccount(1),BankAccount)


	'''
	Test removeAccount to ensure that when the bank has no accounts, removing one
	will not throw an error and the bank will still have no accounts.
	'''
	def testRemoveNoAccounts(self):
		#ensure account list is empty
		self.assertEqual(len(self.b.bankAccounts),0)
		self.b.removeAccount(1)
		#ensure account list is still empty
		self.assertEqual(len(self.b.bankAccounts),0)


	'''
	USES MOCK
	Test removeAccount to ensure that when the bank has 1 account, after removing
	the 1 account, the bank will have zero accounts. Uses mock to return the correct
	account number
	'''
	def testRemoveOneAccount(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 1
			self.b.addAccount()

			#ensure account list's size is 1
			self.assertEqual(len(self.b.bankAccounts),1)

			#remove account
			self.b.removeAccount(1)

			#ensure account list's size is 0
			self.assertEqual(len(self.b.bankAccounts),0)



	'''
	USES MOCK
	Test to ensure that getAccount can be duplicated. Get account, deposit money into it, set account = None,
	get account again, and make sure the balance is the amount deposited
	'''
	def testGetAccountTwice(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 1
			self.b.addAccount()
			a = self.b.getAccount(1)
			a.balance = 10
			a = None

			#Assert that a has been set to None
			self.assertIsNone(a)

			#Get the same account and assert the balance is still 10
			a = self.b.getAccount(1)
			self.assertEqual(a.balance,10)


	'''
	USES MOCK
	Tests to ensure that when addAccount is called,
	getNextAccountNumber method is called from within addAccount
	'''
	def testAddAccountUsingMock(self):
		real = Bank()
		real.getNextAccountNumber = MagicMock()
		real.addAccount()
		real.getNextAccountNumber.assert_called_with()


	'''
	Test to ensure that adding 1 account makes the Bank have 1 account in its list
	of BankAccounts.
	'''
	def testAddFirstAccount(self):
		self.b.addAccount()
		self.assertEqual(len(self.b.bankAccounts),1)


	'''
	Test to ensure that adding 3 accounts in succession makes the Bank have 3 accounts
	in its list of BankAccounts
	'''
	def testAddThreeAccounts(self):
		for i in range(3):
			self.b.addAccount()
		self.assertEqual(len(self.b.bankAccounts),3)


	'''
	USES MOCK
	Test to ensure isvalidAccountNumber uses BankAccount.getAccountNumber correctly and
	returns True if it is found
	'''
	def testIsValidAccountNumberMock(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			result = self.b.isValidAccountNumber('result')
			self.assertTrue(result)


	'''
	USES MOCK
	Test to ensure isValidAccountNumber uses BankAccount.getAccountNumber correctly and returns
	False if it is not found
	'''
	def testNotValidAccountNumberMock(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			result = self.b.isValidAccountNumber('10')
			self.assertFalse(result)


	'''
	Test to ensure getting the next account number with no accounts returns 1
	'''
	def testGetNextAccountNumberWithNoAccounts(self):
		self.assertEqual(self.b.getNextAccountNumber(),1)


	'''
	Test to ensure getting the next account number after creating 2 accounts returns 3
	'''
	def testGetNextAccountNumberWithTwoAccounts(self):
		self.b.addAccount()
		self.b.addAccount()
		self.assertEqual(self.b.getNextAccountNumber(),3)


	'''
	Test to ensure that calling empytAllAccounts with only accounts with zero balances will have
	the accounts still have zero balances
	'''
	def testEmptyAllAccountsZeroBalance(self):
		self.b.addAccount()
		self.b.addAccount()
		self.b.addAccount()
		for i in self.b.bankAccounts:
			self.assertEqual(i.balance,0)


	'''
	Test to ensure that calling emptyAllAccounts with accounts that have balances, the ending balances
	will all be zero
	'''
	def testEmptyAllAccountsNonZeroBalances(self):
		self.b.addAccount()
		self.b.addAccount()
		self.b.addAccount()

		for i in self.b.bankAccounts:
			i.balance += 10

		#Ensure balances are all 10
		for i in self.b.bankAccounts:
			self.assertEqual(i.balance,10)

		self.b.emptyAllAccounts()

		#Ensure all balances are 0
		for i in self.b.bankAccounts:
			self.assertEqual(i.balance,0)
	
	
	'''
	USES MOCK
	Test to ensure integer deposits correctly increase the balance.
	'''
	def testIntegerDeposit(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.deposit(10)
			self.assertEqual(account.balance,20)
	
	
	'''
	USES MOCK
	Test to ensure an exception is raised if you try to deposit a negative value.
	Try to deposit a negative integer value.
	'''
	def testNegativeDeposit(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.deposit(-10)
			self.assertRaises(Exception, account.deposit,-10)
	
	
	'''
	USES MOCK
	Test to ensure decimal deposits correctly increase the balance.
	'''
	def testDecimalDeposit(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.deposit(0.50)
			self.assertEqual(account.balance,10.50)
	
	
	'''
	USES MOCK
	Test to ensure very large deposits correctly increase the balance.
	'''
	def testLargeDeposit(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.deposit(2147483650)
			self.assertEqual(account.balance,2147483660)
			
	
	'''
	USES MOCK
	Test to ensure very small deposits correctly increase the balance.
	'''
	def testSmallDeposit(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.deposit(0.001)
			self.assertEqual(account.balance,10.001)
	
	
	'''
	USES MOCK
	Test to ensure integer withdrawals correctly decrease the balance.
	'''
	def testIntegerWithdraw(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.withdraw(5)
			self.assertEqual(account.balance,5)
	
	
	'''
	USES MOCK
	Test to ensure an exception is raised if you try to deposit a negative value.
	Try to withdraw a negative integer value.
	'''
	def testNegativeWithdraw(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.withdraw(-5)
			self.assertRaises(Exception, account.withdraw,-5)
	
	
	'''
	USES MOCK
	Test to ensure decimal withdrawals correctly decrease the balance.
	'''
	def testDecimalWithdraw(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.withdraw(0.50)
			self.assertEqual(account.balance,9.50)
	
	
	'''
	USES MOCK
	Test to ensure an exception is raised when an overdraft is attempted.
	Try to overdraft the account by one dollar.
	'''
	def testOverdraft(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.withdraw(11)
			self.assertRaises(Exception, account.withdraw,11)
	
	
	'''
	USES MOCK
	Test to ensure very small withdrawals correctly decrease the balance.
	'''
	def testSmallWithdraw(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			account.withdraw(0.001)
			self.assertEqual(account.balance,9.999)
	
	
	'''
	USES MOCK
	Test to ensure getBalance returns the correct balance.
	'''
	def testGetBalanceAccuracy(self):
		with patch('BankApplication.BankAccount') as mock:
			instance = mock.return_value
			instance.getAccountNumber.return_value = 'result'
			self.b.addAccount()
			account = self.b.getAccount('result')
			account.balance = 10
			self.assertEqual(account.getBalance,10)
	
	
	'''
	Test to ensure an exception is raised if you try to access an account using non-numeric characters.
	Try to get an account using a text string.
	'''
	def testNonNumericAccountNumber(self):
		text = "LetMeIn"
		self.assertRaises(Exception, self.b.getAccount,text)
	
	
	'''
	Test to ensure an exception is raised if you try to access an account using null.
	Try to get an account by submitting no characters.
	'''
	def testNullAccountNumber(self):
		self.assertRaises(Exception, self.b.getAccount,None)
	
	
	'''
	Test to ensure an exception is raised if you try to access an account using rudimentary hacking techniques.
	Try to get an account by submitting "True".
	'''
	def testTrueAccountNumber(self):
		self.assertRaises(Exception, self.b.getAccount,True)



if __name__ == '__main__':
	unittest.main(verbosity=2)
