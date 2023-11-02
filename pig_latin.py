

def pig_latin_converter(sentence):

	words = sentence.split()#split into words
	pig_latin_words = []#store words into lists

	for word in words:
		if len(word) == 1:
			#just add 'ay' to the end of 1 letter words
			pig_latin_word = word + 'ay'
		else:
			#for multi letter words, move the first letter to the end and add 'ay'
			pig_latin_word = word[1:] + word[0] + 'ay'

		pig_latin_words.append(pig_latin_word)#add translated word to the list


	#Join pig latin words back into a sentence

	pig_latin_sentence = ' '.join(pig_latin_words)
	return pig_latin_sentence

#input

input = input("enter a sentence: ")

#function call

result = pig_latin_converter(input)

print('pig latin: ' , result)


