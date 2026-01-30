from multiprocessing import Pool
import subprocess

output_file = "./output"

def execute_code(file, arg):
	with open(f"output_{arg}.txt", "w") as f:
		subprocess.run([file, str(arg)], stdout=f)

if __name__ == '__main__':
	Pool().starmap(execute_code, [[output_file, i] for i in range(1,11)])
