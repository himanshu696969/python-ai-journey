class Solution:
    def printEvenOdd(self, start: int, end: int) -> None:
        even = []
        odd = []

        for num in range(start, end + 1):
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        print("Even Numbers:", even)
        print("Odd Numbers:", odd)


# User Input
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# Object Creation
obj = Solution()
obj.printEvenOdd(start, end)
