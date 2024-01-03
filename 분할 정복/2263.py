import sys

sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
inorder_dict = {i: idx for idx, i in enumerate(inorder)}
postorder = list(map(int, input().split()))


def preorder(in_head, post_head, count):
    if count <= 0:
        return

    root = postorder[post_head + count - 1]
    print(root, end=" ")

    if count == 1:
        return

    root_index = inorder_dict[root]

    left_subtree_count = root_index - in_head
    preorder(in_head, post_head, left_subtree_count)

    right_subtree_count = count - left_subtree_count - 1
    preorder(root_index + 1, post_head + left_subtree_count, right_subtree_count)


preorder(0, 0, n)
