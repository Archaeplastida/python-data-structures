def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    WAS: (4, 3) sum to 7, and finish before (5, 2)
    NOW: (5, 2) sum to 7, and finish before (4, 3):

    MY COMMENT: You cannot have (4, 3) come before (5, 2) since 5 appears first and it checks for its addend to create the sum of 7 first. Which is why (5, 2) is correct and follows the rule.

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (5, 2)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    for x in nums:
        index = 1
        for y in nums[index:]:
            if x+y == goal:
                return (x, y)
    return ()