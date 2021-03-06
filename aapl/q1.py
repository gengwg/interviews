"""
Given a folder of build files that might look like this:

/Build-1.dmg
/Build-2.dmg
/Build-2.1.dmg
/Build-2.1.1.dmg
/Build-3.dmg
/Build-3.2.dmg
/Build-3.19.dmg

Write a script that takes a path to the folder as an argument, and prints the highest build number (just the number, i.e. 2.1.1)
Note:  The first digit can go up to 999 and should always be present, but the second and third can only go up to 99, and might not be         included.
"""

import re

builds = '/Build-1.dmg /Build-2.dmg /Build-2.1.dmg /Build-2.1.1.dmg /Build-3.dmg /Build-3.2.dmg /Build-3.19.dmg'

def compareVersion(version1, version2):
    v1Arr = version1.split(".")
    v2Arr = version2.split(".")
    len1 = len(v1Arr)
    len2 = len(v2Arr)
    for i in range(max(len1, len2)):
        v1Token = 0
        v2Token = 0
        if i < len1:
            v1Token = int(v1Arr[i])
        if i < len2:
            v2Token = int(v2Arr[i])
        if v1Token > v2Token:
            return 1
        if v1Token < v2Token:
            return -1
    return 0

def getHighestVersion(builds):
    highest = '0'
    pattern = re.compile(r'/Build-(.*).dmg')
    for build in builds.split():
        m = pattern.match(build)
        version = m.group(1)
        if compareVersion(version, highest) == 1:
            highest = version
    return highest

print getHighestVersion(builds)
