class FreqStack:

    def __init__(self):
        # Store {freq:[stack of values]} in hashmap
        self.group = {}
        # Store {val:freq}
        self.freq_map = {}
        # Store a max freq variable
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        # Store {val:freq}
        if val not in self.freq_map:
            self.freq_map[val] = 1
        else:
            self.freq_map[val] += 1
        
        # Extract the frequency of the val
        freq = self.freq_map[val]

        # Add it to the group map
        if freq not in self.group:
            self.group[freq] = []
        
        self.group[freq].append(val)

        # Update max_freq 
        self.max_freq = max(freq, self.max_freq)
        

    def pop(self) -> int:
        popped_val = self.group[self.max_freq].pop()
        self.freq_map[popped_val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return popped_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()