class TimeMap:
#the plan: keep a list and a dictionary (hashmap), every time I need to set a new element, I will append the timestamp to the list and use a tuple made of the key and the timestamp as key of my dictionary and the value as a value, when I get a request via the get method to return a value, I first check if the pair of key, timestamp is in my dictionary, if it is I will return it, if not, i will perform a binary search in my list to find the closer element smaller and use that as a timestamp (key for my dict) instead, if there's no such element (if the timestamp given to me is smaller than the smallest timestamp i have) I return an empty string

#the plan: when I set a key, value, timestamp is to have a dictionary whose key maps to the given key, the value of the dict is going to be made of 2 things, first thing is a list of all timestamps given for that particular key the second thing is another dictionary that maps each one of the timestamps to their particular value
#when we recieve a get request, we go the key given to us in our dictionary, if it's not there we return empty list,
#if it's there we check for the timestamps of that particular key, we find either an exact match, in which case we just return the value associated with it in our nested dict, or, alternatively the closest possible smaller element to what we have and we use that one as the key in our nested dict, if all our timestamps are smaller than what's given, we also return an empty list
    def __init__(self):
        self.dico = dict()
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dico:
            self.dico[key][0].append(timestamp)
            self.dico[key][1][timestamp] = value
        else:
            list_of_timestamps = [timestamp]
            self.dico[key] = [list_of_timestamps, {timestamp: value}]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dico and timestamp >= self.dico[key][0][0]:
     
            return self.dico[key][1][self.binarySearch(self.dico[key][0], timestamp)]
        else:
            return ""

    
    def binarySearch(self, alist, target):
        l, r = 0, len(alist) - 1

        while l<=r:
            m = (l + r)//2
            if alist[m] == target:
                return target
            elif target > alist[m]:
                l = m + 1
            elif target < alist[m]:
                r = m - 1

        return alist[r]



        
