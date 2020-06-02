from datetime import datetime


class Timecode:
	def __init__(self, log_path, encoding='utf-8'):
		self.log_file = open(log_path, 'a', encoding=encoding)
		self.begin = self.func_time()
		print(self.begin, " - First time")

	def func_time(self):
		time = datetime.utcnow()
		return time

	def __enter__(self):
		return self

	def write_log(self, action):
		self.log_file.write(f'{datetime.utcnow()}: {action}\n')

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type is not None:
			self.write_log(f'error: {exc_val}')
			self.write_log("GoodBye")
		end = self.func_time()
		print(end, "- Second time")
		dif = end - self.begin
		print(dif, "- Difference between times")
		self.log_file.close()


if __name__ == '__main__':
	with Timecode('my_log') as log:
		log.write_log('Begin: ')
		x = 1
		while x < 1000000:
			x = x + 1
		print(x, " - Just print from some code")
		log.write_log('created x')
		log.write_log('That"s All!')
