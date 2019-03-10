class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        count = 0
        final_host = {}
        final_local = {}
        for email in emails:
            info = email.split('@')
            local = info[0]
            host = info[1]
            send_local = local.split('+')[0]
            send_local = send_local.replace('.','')
            print send_local
            if host not in final_host:
                final_host[host] = send_local

        print len(final_host)
        return len(final_host)

    def toLowerCase(self, ss):
        for s in ss:
            s = s.lower()
            print s
        print ss
        print ss.lower()
        return ss
    
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_dic = {}
        for j in J:
            jewel_dic[j] = 0
        for s in S:
            if s in jewel_dic:
                jewel_dic[s] += 1
        count = 0
        
        for k in jewel_dic:
            count += jewel_dic[k]

        print count
        return count

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tmp = nums1 + nums2
        result = sorted(tmp) # sort(list) is much more fast than list.sort(),list.sort() won't return list
        mid = int(len(result)/2)
        if len(result) % 2 == 0:
            answer = (float(result[mid]) + float(result[mid-1]))/2
        else:
            answer = result[mid]
        return answer

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = 1
        rj = 0
        rk = 0
        if len(s) == 1:
            return s
        
        for i in range(len(s)):
            j = i-1
            k = i+1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if k - j + 1 > m:
                    m = k - j + 1
                    rj = j
                    rk = k
                j -= 1
                k += 1
            if (i == 0 and j < 0) or (i == (len(s) - 2) and k == (len(s) - 1)):
                if s[i] == s[k]:
                    if k - i  + 1 > m:
                        m = k - i + 1
                        rj = i
                        rk = k
        
        for i in range(len(s)):
            j = i
            k = i+1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if k - j + 1 > m:
                    m = k - j + 1
                    rj = j
                    rk = k
                j -= 1
                k += 1
                
        return s[rj:rk+1]
    
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        print int(s.strip())
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        width = 0
        max_width = 0
        area = 0
        max_area = 0

        for i in xrange(len(height)):
            for j in xrange(len(height)):
                if i == j:
                    continue
                if height[i] <= height[j]:
                    if width < abs(j-i):
                        width = abs(j-i)

            area = width * height[i]
            if max_area < area:
                max_area = area
            width = 0
                       
        print max_area

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        IV IX
        XL XC
        CD CM
        """
        result = 0
        jump = False
        letter = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in xrange(len(s)):
            if jump == True:
                jump = False
                continue
            if i+1 == len(s):
                print letter[s[i]]
                result += letter[s[i]]
            else:
                if s[i] == "I":
                    if s[i+1] == "V":
                        result += 4
                        jump = True
                    elif s[i+1] == "X":
                        result += 9
                        jump = True
                    else:
                        result += 1

                elif s[i] == "X":
                    if s[i+1] == "L":
                        result += 40
                        jump = True
                    elif s[i+1] == "C":
                        result += 90
                        jump = True
                    else:
                        result += 10

                elif s[i] == "C":
                    if s[i+1] == "D":
                        result += 400
                        jump = True
                    elif s[i+1] == "M":
                        result += 900
                        jump = True
                    else:
                        result += 100
                else:
                    result += letter[s[i]]
        print result
        return result
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        leetcode lee leetcodes
        """
        prefix = strs[0]
        for i in xrange(len(strs)-1):
            j = 0
            while j < min(len(prefix), len(strs[i+1])):
                if prefix[j] == strs[i+1][j]:
                    j += 1
                else:
                    break

            prefix = strs[i][0:j]

        print prefix

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        mark = []
        flag = False
        i = 0
        j = len(nums) - 1
        
        while j - i >= 2:
                k = i + 1
                while k < j:
                    tmp = nums[i] + nums[j] + nums[k]
                    if tmp > 0:
                        j -= 1
                        break
                    elif tmp == 0:
                        if [nums[i], nums[j], nums[k]] not in result:
                            result.append([nums[i], nums[j], nums[k]])
                            i += 1
                            break
                    elif tmp < 0:
                        k += 1
                if tmp < 0:
                    i += 1
                
        print result


s = Solution()
s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
s.toLowerCase("HELLO")
s.numJewelsInStones("aA", "aAAbbbb")
s.findMedianSortedArrays([1,2],[1,3])
s.longestPalindrome("adam")
s.myAtoi("       123")
s.maxArea([1,8,6,2,5,4,8,3,7])
s.romanToInt("LVIII")
s.longestCommonPrefix(["leetcode","leet","leetcodes","leeeee"])
s.longestCommonPrefix(["leetcode","asd","111"])
s.threeSum([0, 0, 0, 0])
