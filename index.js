const lengthOfLastWord = function (s) {
	s = s.trim();
	let count = 0;
	let char = s[s.length - 1];
	while (char !== " ") {
		count++;
		if (count === s.length) break;
		char = s[s.length - count - 1];
	}
	return count;
};
