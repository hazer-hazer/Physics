## Constants
g = 9.81

## Formulas

# 
ma = lambda m, T : m * g - T

# Accel
a = lambda h, t : 2 * h / t**2

# Angle accel
e = lambda a, d : 2 * a / d

# Rope tension
T = lambda m, a : m * (g - a)

M = lambda m, d, a : m * d / 2 * (g - a)

Ie = lambda M, Mtr : M - Mtr

# Innertion
I = lambda I0, mut, R : I0 + 4 * mut * R**2

def ave(*vals):
	if len(vals) > 0:
		return sum(vals) / len(vals)
	else:
		return 0

# File input
def open_sheet(filename = 'input.py'):
	sheet = []
	with open(filename, 'r') as f:
		lines = f.read().splitlines()
		for l in lines:
			sheet.append( l.split(' ') )

	return sheet



if __name__ == '__main__':
	print(open_sheet())