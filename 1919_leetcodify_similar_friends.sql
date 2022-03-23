# Write your MySQL query statement below
SELECT DISTINCT l1.user_id AS user1_id, l2.user_id AS user2_id
    FROM Listens l1 INNER JOIN Listens l2 ON l1.song_id=l2.song_id AND l1.day=l2.day AND l1.user_id<l2.user_id
    WHERE EXISTS (SELECT * FROM Friendship f WHERE l1.user_id=f.user1_id AND l2.user_id=f.user2_id)
    GROUP BY l1.user_id, l2.user_id, l1.day
    HAVING COUNT(DISTINCT(l1.song_id)) >= 3