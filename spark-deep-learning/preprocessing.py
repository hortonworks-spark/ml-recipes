import scipy.io
mat = scipy.io.loadmat("/Users/yliang/data/hortonworks/deep-learning/data/cars_annos.mat")
annotations = mat["annotations"][0]
class_names = mat["class_names"][0]

dictionary = {}

for annotation in annotations:
	url = annotation[0][0][8:14]
	class_id = annotation[5][0][0]
	class_name = class_names[class_id - 1][0]
	dictionary[url] = class_name

print(dictionary)

import csv
import collections

with open("/Users/yliang/data/hortonworks/deep-learning/data/id2class.order", "wb") as csv_file:
	writer = csv.writer(csv_file)
	od = collections.OrderedDict(sorted(dictionary.items()))
	for key, value in od.iteritems():
		writer.writerow([key, value])



# for annotation in annotations:
# 	url = annotation[0][0]
# 	class_id = annotation[5][0][0]
# 	dictionary[url] = class_id
