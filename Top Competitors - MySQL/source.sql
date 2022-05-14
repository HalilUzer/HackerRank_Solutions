SELECT H.hacker_id, H.name
FROM HACKERS AS H
INNER JOIN SUBMISSIONS AS S
ON S.hacker_id = H.hacker_id
INNER JOIN CHALLENGES AS C
ON C.challenge_id = S.challenge_id
INNER JOIN DIFFICULTY AS D
ON D.difficulty_level = C.difficulty_level
WHERE S.score = D.score 
GROUP BY  H.hacker_id, H.name
HAVING COUNT(H.hacker_id) > 1
ORDER BY  COUNT(H.hacker_id) DESC, H.hacker_id ASC;