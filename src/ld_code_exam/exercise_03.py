# You are in a shopping game and each table contains interesting gift items that you can pick. Tables are numbered 1 through N and the tables are placed far apart. Your job is to start at any table and move in a sequence to pick up all possible items.Gift items may be repeated.
# Your goal is to grab maximum distinct gifts with minimum possible moves.  Note: Once you choose a starting table, you are allowed to move to the next table in a sequential manner i.e. If you start at table 5, you can move from table 5 to table 6, then to table 7, table 8 and so on without skipping until you decide to stop.
#
# We will represent the gifts in an array.
#
# Example 1:
# A[1] = “Gift1”
# A[2] = “Gift3”
# A[3] = “Gift1”
# A[4] = “Gift2”
# A[5] = “Gift1”
# A[6] = “Gift4”
# A[7] = “Gift3”
# A[8] = “Gift1”
# In the above example, if you started from table 4, you can grab all the 4 gifts in 4 steps A[4], A[5], A[6], A[7]
# Therefore, the answer is 4
#
# Example 2:
# A[1] = “Gift3”
# A[2] = “Gift5”
# A[3] = “Gift3”
# A[4] = “Gift2”
# A[5] = “Gift1”
# A[6] = “Gift3”
# A[7] = “Gift4”
# A[8] = “Gift2”
#
# In this example, the answer is 6 starting from A[2] through A[7].
#
# Write a function which takes an input array of N items and returns the smallest number of tables that you would visit in sequence to grab the most number of distinct gifts.


from collections import OrderedDict


def get_gifts_count(tables):
    distinct_gifts = set()
    for gift in tables:
        distinct_gifts.add(gift)
    return len(distinct_gifts)


def solution(tables):
    gifts_count = get_gifts_count(tables)

    gifts_picked = OrderedDict()
    min_moves = len(tables)
    for i in range(len(tables)):

        if tables[i] in gifts_picked:
            del gifts_picked[tables[i]]
        gifts_picked[tables[i]] = i

        # we have picked all gifts find the smallest index which can be given by first element in the OrderedDict
        if len(gifts_picked) == gifts_count:
            smallest_index = gifts_picked[next(iter(gifts_picked))]
            total_tables_visited = i - smallest_index + 1
            min_moves = min(min_moves, total_tables_visited)

    return min_moves
