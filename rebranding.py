from collections import defaultdict


def rebranding():
	n_m = input().split()
	n = int(n_m[0])
	m = int(n_m[1])

	brand_name = list(input())

	lowercase_letters = list(map(chr, range(97, 123)))
	origin_lowercase_letters = list(map(chr, range(97, 123)))


	for _ in range(0, m):
		x, y = input().split()
		if x != y:
			idx = lowercase_letters.index(x)
			idy = lowercase_letters.index(y)
			lowercase_letters[idx] = y
			lowercase_letters[idy] = x

	dictionnary = defaultdict(str)

	for i, letter in enumerate(origin_lowercase_letters):
		dictionnary[letter] = lowercase_letters[i]

	for i, letter in enumerate(brand_name):
		brand_name[i] = dictionnary[letter]
		
	print(''.join(brand_name))


if __name__ == '__main__':
	rebranding()
