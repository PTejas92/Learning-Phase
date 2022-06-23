text = """Domestic wearable brand Noise on Tuesday announced the launch of its first pair of smart eyewear ‘i1’. According to the companyl  Made in India smart eyewear i1 brings a host of features, including a Motion Estimation, Motion Compensation (MEMS) Mic for calling, magnetic Charging, and hands-free voice control, to offer style, comfort and a unique audio experience. 

The company said that Noise i1 is available at Rs 5,999. Consumers can purchase this limited edition device from gonoise website. "Noise i1 is a product tailored to the needs of people who are always ahead of the curve, whether it’s fashion or technology," the company claims."""

print(text)
print(len(text))
word2 = text.split()
print(word2)
print(len(text.split()))

word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)