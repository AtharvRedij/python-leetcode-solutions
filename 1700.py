class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while sandwiches:
            sandwich = sandwiches.pop(0)
            preference_index = None

            for i, student_preference in enumerate(students):
                if sandwich == student_preference:
                    preference_index = i
                    break

            if preference_index is None:
                break
            else:
                counter = 0
                while counter < preference_index:
                    students.append(students.pop(0))
                    counter += 1

                students.pop(0)


        return len(students)
