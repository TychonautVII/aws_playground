import numpy as np
import logging

# -------------------------
# Log to console and file
# -------------------------
LOG_FMT = '%(asctime)s|%(name)s|%(levelname)s|%(message)s'

handlers = [logging.FileHandler('source.log',mode='a'), logging.StreamHandler()]
logging.basicConfig(level=logging.INFO, format=LOG_FMT,handlers=handlers)
logger = logging.getLogger(__name__)

# -------------------------
# Functions
# -------------------------

def my_mean(xs):
	mean = sum(xs) / len(xs)
	return mean

def np_mean(xs):
	mean = np.mean(xs)
	return mean

def main():
	data = [1,2,3]
	logger.info("Starting Main")
	logger.info("my_mean {}".format(my_mean(data)))
	logger.info("np_mean {}".format(np_mean(data)))
	logger.info("Ending Main")

if __name__ == "__main__":
	main()

