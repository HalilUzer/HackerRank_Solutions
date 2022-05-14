SELECT W.id, WP.age, W.coins_needed, W.power
FROM WANDS AS W
INNER JOIN WANDS_PROPERTY AS WP
ON W.code = WP.code 
WHERE WP.is_evil <> 1 AND W.coins_needed = (
    SELECT MIN(X.coins_needed)
    FROM WANDS AS X
    INNER JOIN WANDS_PROPERTY AS XP
    ON X.code = XP.code 
    WHERE XP.age = WP.age AND X.power = W.power
)
ORDER BY W.power DESC, WP.age DESC;