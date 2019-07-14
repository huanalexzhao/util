# util
customize algorithms and data structure
## Heap ##
Data Structure Description
<br>
create a heap by given tag `min` or `max`
```
heap = Heap("<TAG>")
```
insert a number
```
heap.insert(x)
```
access its priority number
```
heap.priority
```
extract the priority
```
x = heap.extract()
```
### Maintain Median ###
Given a serial of number output the median
```
m = Median()
m.add(x) 
...
m.median
```
