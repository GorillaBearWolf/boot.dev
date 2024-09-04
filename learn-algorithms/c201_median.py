def median_followers(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        return sorted_nums[n // 2]


# don't touch below this line


def test(nums):
    res = round(median_followers(nums))
    print(f"Follower counts: {nums}")
    print(f"Median follower count: {res}")
    print("----")


def main():
    test([7, 4, 3, 100, 2343243, 343434, 1, 2, 32])
    test([12, 12, 12])
    test([10, 200, 3000, 5000, 4])
    test([10, 200, 3000, 5000, 4, 6])


main()
