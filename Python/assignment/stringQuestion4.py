"""4. String split
a) Now split the above build version to get its individual segments and store them in a
list variable "segments".
b) Print the elements of segments list using index notation.
c) Print them in reverse now, again using index notation."""


build_version = "10.1.18"
segment = build_version.split('.')
print(segment)
#print(f"length of list {len(segment)}")
def displayList(listName):
    i = 0
    while i < len(listName):
        print(listName[i])
        i += 1

displayList(segment)
segment.reverse()
print(f"revese string {segment}")
displayList(segment)