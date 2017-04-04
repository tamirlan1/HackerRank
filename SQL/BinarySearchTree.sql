-- You are given a table, BST, containing two columns: N and P, where N represents the value of a node in BST, and P is the parent of N.

-- Write a query to find the node type of BST ordered by the value of the node. Output one of the following for each node:

-- Root: If node is root node.
-- Leaf: If node is leaf node.
-- Inner: If node is neither root nor leaf node.

SELECT DISTINCT M.N, CASE
WHEN M.P IS NOT NULL THEN 
    CASE WHEN C.N IS NOT NULL THEN 'Inner'
    ELSE 'Leaf' END
ELSE 'Root' END
FROM BST AS C
RIGHT JOIN BST AS M
ON C.P = M.N
ORDER BY M.N