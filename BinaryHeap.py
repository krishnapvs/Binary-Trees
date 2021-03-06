# Binary Heap implementation for minimum Heap

class BinaryHeap:
	def __init__(self,):
		self.heapList=[0]
		self.currentsize=0

	def insert(self,item):
		self.heapList.append(item)
		self.currentsize+=1
		self.buildHeap(self.currentsize)

	def buildHeap(self,i):
		while (i/2) > 0:
			if self.heapList[i] >= self.heapList[i/2]:
				return
			temp=self.heapList[i]
			self.heapList[i]=self.heapList[i/2]
			self.heapList[i/2]=temp
			i=i/2

	def delMin(self):
		temp=self.heapList[1]
		self.heapList[1]=self.heapList[-1]
		self.currentsize -= 1
		del self.heapList[-1]
		self.heapify()
		return temp

	def heapify(self,i=1):		
		while ( i*2 =< self.currentsize):
			mc=self.minimum(i)
			if self.heapList[mc] < self.heapList[i]:
				temp=self.heapList[i]
				self.heapList[i]=self.heapList[mc]
				self.heapList[mc]=temp
			i=mc

	def minimum(self,i):
	#returns the minimum element
		if 2*i+1 > self.currentsize:
			return i*2
		else:
			if self.heapList[i*2] > self.heapList[i*2+1]:
				return i*2+1
			else:
				return i*2

	def buildHeap(self,alist):
	# creating a heap from a list start to end
		self.currentsize=len(alist)
		i=self.currentsize/2
		self.heapList=[0]+alist[:]
		while i>0:
			self.heapify(i)
			i = i-1
	



