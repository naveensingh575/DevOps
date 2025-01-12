"""3. String replacement
a) Create a new variable called `build_version` and assign it the value of "10.1.18".
b) From the above string replace the third (only the third) segment with 34.
c) After replacement the version should look like 10.1.34 """

build_version = "10.1.18"
build_version = build_version.replace('18','34')
print(build_version)

#error as string are immutable
"""build_version[5] = 3
build_version[6] = 4

print(build_version)"""

