import numpy as np 
import operator
# import Queue
# Dataset Creation
def createDataSet():
	# do not forget '[]' outside the data
	# The input variable of np.array should be a list of lists
	group = np.array([
		[1.0, 1.1], 
		[1.0, 1.0], 
		[0.0, 0.0], 
		[0.0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels

# Pick out the smallest k elements by scanning the data
# Temporary elements are stored in a queue
#	which is not properly implemented in Python
def pick_min_k_ele(data, k):
	ret = []
	ret.append([data[0], 0])
	for i in range(len(data)):
		if not len(ret) == 0:
			if data[i] < ret[0][0]:
				if len(ret) == k:
					# Do not forget to input the position where 
					# elements to be popped.
					ret.pop(0)
				else:
					pass
				ret.append([data[i], i])
			else:
				pass
		else:
			pass
	return ret

# dataset could be in any size of a matrix
def knn_classify(inX, dataSet, lables, k):
	data_dim = dataSet.shape;

	# The ```tile()``` function is to shape the given matrix into 
	# certain dimension and size.
	# np.tile(Matrix, (int n, int m, int h, ...))
	# where second input variable represents 
	# times of duplication in coordinate direction
	data_diff = np.tile(inX, (data_dim[0], 1)) - dataSet
	# ```np.sum()``` is used to get the sum of values in certain dimension
	# np.sum(axis = int dim);
	# HOWEVER, **Transpose** in of 1-D matrix has no effect
	# Therefore, finally it gives a 1 * n matrix, which is a list
	dist = (data_diff ** 2).sum(axis = 1) ** 0.5

	# Simply sorting might not be a good way
	# scan the dataSet and simply pick out the smallest k elements
	k_near_list = pick_min_k_ele(dist, k)

	# Voting
	vote_count = {} 
	for dist_ind in k_near_list:
		vote = label[dist_ind[1]]
		# dict.get(key, default_value) here returns " int 0" when the 
		# key does not exist, no need for key checks
		vote_count[vote] = vote_count.get(vote, 0) + 1

	# Methods given in the text book simply used Sort, which is O(nlogn)
	# in complexity. There is no need for such auxilury operation
	# However, I have not yet found proper way to scan a dict object
	# I simply cast the dict_key(list) into a list and go it through with
	# a complexity of O(n)
	
	key_list = list(vote_count.keys())
	max_val = vote_count[key_list[0]]
	max_label = key_list[0]
	for i in range(len(key_list) - 1):
		if vote_count[key_list[i + 1]] > max_val:
			max_val = vote_count[ key_list[ i + 1 ] ]
			max_label = key_list[i+1]

	return max_label

if __name__ == '__main__':
	group, label = createDataSet()
	print(knn_classify([0,0], group, label, 3))