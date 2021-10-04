#!env/bin/python

from bitstring import BitArray, pack
import time

class Graph():
    def __init__(self, filePath=None, size=4):
        self.array = list()
        if filePath is None:
            self.init_array(size)

        print("starting graph")


    def init_array(self, size: int):
        """ Generate a blank array based on the size
        for size 4 array will look like this 
        [[0],
         [0,0],
         [0,0,0]]

           1 2 3 4
         2 0 
         3 0 0
         4 0 0 0
        """
        for i in range(1, size):
            a = [0 for i in range(0, i)]
            self.array.append(a)
        return self

    def array_to_binary(self):
        bit_string = BitArray('')

        # Number of files in the graph
        length = len(self.array) + 1
        # encode length in 3byte/24bit uint
        bit_string += pack('uint:24', length)


        for i in range(0, length-1):
            bstr = ''.join(str(e) for e in self.array[i])
            bit_string += BitArray(bin=bstr)

        return bit_string 

    def binary_to_array(self):
        pass


def main():
    graph = Graph(size=1000)
    start = time.time()
    graph.array_to_binary()
    print(time.time() - start)
   

if __name__ == "__main__":
    main()
