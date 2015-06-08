SELECT * FROM frequency
WHERE docid = '10398_txt_earn';

SELECT term FROM frequency
WHERE docid = '10398_txt_earn' and count = 1;

SELECT term FROM frequency
WHERE docid = '10398_txt_earn' and count = 1
OR docid = '925_txt_earn' and count = 1;

SELECT count(*) FROM frequency
WHERE term = 'parliament';

SELECT * FROM frequency
Group by term
Having count(docid) + count > 300;

SELECT count(*) FROM frequency x, frequency y
WHERE x.term = 'transactions'
AND y.term = 'world'
AND x.docid = y.docid;

SELECT count(*) FROM frequency x
INNER JOIN frequency y
ON
x.term = 'transactions'
AND y.term = 'world'
AND x.docid = y.docid;


SELECT sum(mul) FROM (SELECT x.row_num as row_num, y.col_num as col_num, x.value*y.value as mul FROM a x
JOIN b y
ON
x.col_num = y.row_num) 
WHERE row_num = 2 
AND col_num = 3
GROUP BY row_num, col_num;

-- h
SELECT row_num, col_num, sum(mul) FROM (SELECT x.docid as row_num, y.docid as col_num, x.count*y.count as mul FROM frequency x
JOIN frequency y
ON
x.term = y.term)
--WHERE row_num < col_num 
GROUP BY row_num, col_num;

-- i

SELECT row_num, sum(mul) AS s FROM (
SELECT x.docid AS row_num, y.docid AS col_num, x.count*y.count AS mul FROM 
(SELECT * FROM frequency
UNION
SELECT 'q' AS docid, 'washington' AS term, 1 AS count 
UNION
SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
UNION 
SELECT 'q' AS docid, 'treasury' AS term, 1 AS count) x
JOIN (SELECT * FROM frequency
UNION
SELECT 'q' AS docid, 'washington' AS term, 1 AS count 
UNION
SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
UNION 
SELECT 'q' AS docid, 'treasury' AS term, 1 AS count) y
ON
x.term = y.term)
GROUP BY row_num
ORDER BY s DESC;




