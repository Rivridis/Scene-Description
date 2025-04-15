import nltk

hypothesis = ["This", "is", "an", "image", "showing", "a", "laptop", "computer","with", "its", "keyboard", "clearly", "visible"]
reference = ['This', 'is', 'an', 'image', 'of', 'a', 'laptop', 'computer', 'with','its','keyboard', 'visible', 'clearly']

BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)
print(BLEUscore)