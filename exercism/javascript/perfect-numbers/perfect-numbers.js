export const classify = (number) => {
	if (number <= 0) throw 'Classification is only possible for natural numbers.';
	if (number <= 3) return 'deficient';

	let total_factors = factors(number);

	let sum = sum_factors(total_factors);
	if (isPerfect(sum, number)) return 'perfect';
	if (isAbundant(sum, number)) return 'abundant';
	else return 'deficient';
};

function isPerfect(sum, number) {
	return sum === number;
}

function isAbundant(sum, number) {
	return sum > number;
}

function factors(number) {
	let total_factors = [];
	let i = 2;

	while (i != number) {
		if (number % i === 0) {
			total_factors.push(i);
			i += 1;
		} else {
			i += 1;
		}
	}
	total_factors.push(1);
	return total_factors;
}

function sum_factors(factors) {
	return factors.reduce((acc, curr) => {
		return (acc += curr);
	});
}
