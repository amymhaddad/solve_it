export const compute = (s1, s2) => {
	if (s1 === s2) {
		return 0;
	}

	if (!s1) {
		throw new Error('left strand must not be empty');
	}
	if (!s2) {
		throw new Error('right strand must not be empty');
	}
	if (s1.length !== s2.length) {
		throw new Error('left and right strands must be of equal length');
	}

	let s1Arr = Array.from(s1);
	let s2Arr = Array.from(s2);

	let count = 0;

	s1Arr.forEach((char, i) => {
		if (char !== s2Arr[i]) {
			count += 1;
		}
	});
	return count;
};
