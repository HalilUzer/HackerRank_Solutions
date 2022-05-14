SELECT BST.N,
      CASE
      WHEN BST.P IS NULL THEN 'Root'
      WHEN BST.N IN (
          SELECT P
          FROM BST
      ) THEN 'Inner'
      ELSE 'Leaf'
      END
FROM BST
ORDER BY BST.N;