import unitest

class NumbersTest(unitest.TestCase);

	def test_equal(self);
		self.assertEqual(1 + 1, 1)

if __name__ == '__main__';
	unitest.main()
