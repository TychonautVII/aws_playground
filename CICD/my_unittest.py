import unittest
import source
import logging
# -------------------------
# Log to console and file
# -------------------------
LOG_FMT = '%(asctime)s|%(name)s|%(levelname)s|%(message)s'

handlers = [logging.FileHandler('test.log',mode='a'), logging.StreamHandler()]
logging.basicConfig(level=logging.INFO, format=LOG_FMT,handlers=handlers)
logger = logging.getLogger(__name__)

# -------------------------
# Log to console and file
# -------------------------
class TestSource(unittest.TestCase):
	# Create test environment / Fixtures
	def setUp(self):
		# This is run seperately for every test
		logger.info("Setting Up for Test")
		self.data = [1,2,3]
		self.answer = 2

	def tearDown(self):
		# This is run seperately for every test
		logger.info("Shutting Down After Test")

	# Tests
	def test_my_mean(self):
		self.assertEqual(source.my_mean(self.data),self.answer)

	def test_numpy(self):
		self.assertEqual(source.np_mean(self.data),self.answer)

if __name__ == "__main__":
	# unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(TestSource)
	unittest.TextTestRunner(verbosity=2).run(suite)