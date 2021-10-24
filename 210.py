class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        course_map = {}
        for c in range(numCourses):
            course_map[c] = []
        for p in prerequisites:
            course_map[p[0]] += [p[1]]
        course = []

        while len(course_map) > 0:
            curr_len = len(course)
            for i in course_map.keys():
                if len(course_map[i]) == 0:
                    course.append(i)
                    course_map.pop(i, None)
                    #remove prerequisites that contains i
                    for j in course_map.keys():
                        if i in course_map[j]:
                            course_map[j].remove(i)
            if curr_len == len(course):
                return []
        
        return course

    def findOrder_dfs(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        course = []

        return course

# def addOne(*num):
#     num += 1

# if __name__ == "__main__":
#     tr = 4

#     print(tr)