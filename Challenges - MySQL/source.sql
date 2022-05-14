SET @max := (
SELECT MAX(K.yeah)
FROM (
SELECT COUNT(C.challenge_id) AS yeah
FROM HACKERS AS H
INNER JOIN CHALLENGES AS C
ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, H.name
) AS K
);



SELECT H.hacker_id, H.name, COUNT(C.challenge_id) AS cn
FROM HACKERS AS H
INNER JOIN CHALLENGES AS C
ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, H.name
HAVING cn = @max OR cn NOT IN (
                    SELECT T.num1
                        FROM(
                            SELECT H1.hacker_id AS hacker_id1, COUNT(C1.challenge_id) AS num1
                            FROM HACKERS AS H1
                            INNER JOIN CHALLENGES AS C1
                            ON H1.hacker_id = C1.hacker_id
                            GROUP BY H1.hacker_id, H1.name
                            ) AS T
                        GROUP BY T.num1
                        HAVING COUNT(T.num1) > 1
                        )
ORDER BY cn DESC, H.hacker_id;