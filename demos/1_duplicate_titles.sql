mysql> SELECT count(*) FROM coursera_courses AS t1 LEFT JOIN coursetalk_avg_ratings AS t2 ON t1.name = t2.title;+----------+
| count(*) |
+----------+
|      932 |
+----------+
1 row in set (0.31 sec)

mysql> Select count(*) FROM coursera_courses;
+----------+
| count(*) |
+----------+
|      916 |
+----------+
1 row in set (0.00 sec)

mysql> select title, count(*) AS c FROM coursetalk_avg_ratings GROUP BY title ORDER BY c DESC limit 40; 
+------------------------------------------------------------+---+
| title                                                      | c |
+------------------------------------------------------------+---+
| Machine Learning                                           | 2 |
| Calculus One                                               | 2 |
| Competitive Strategy                                       | 2 |
| Natural Language Processing                                | 2 |
| The Emergence of the Modern Middle East - Part I           | 2 |
| Social Entrepreneurship                                    | 2 |
| Human-Computer Interaction                                 | 2 |
| Introduction to Classical Music                            | 2 |
| Introduction to Public Speaking                            | 2 |
| Initiation à la programmation (en Java)                    | 2 |
| New Models of Business in Society                          | 2 |
| Financial Engineering and Risk Management Part I           | 2 |
| Age of Jefferson                                           | 2 |
| Financial Engineering and Risk Management Part II          | 2 |
| Pre-Calculus                                               | 2 |
| Initiation à la programmation (en C++)                     | 2 |
| Get Organized: How to be a Together Teacher                | 2 |
| Introduction à la programmation orientée objet (en C++)    | 2 |
| Introduction à la programmation orientée objet (en Java)   | 2 |
| Chinese for Beginners                                      | 2 |
| An Introduction to Interactive Programming in Python       | 1 |
| A Beginner's Guide to Irrational Behavior                  | 1 |
| Epidemics - the Dynamics of Infectious Diseases            | 1 |
| Design: Creation of Artifacts in Society                   | 1 |
| Modern & Contemporary American Poetry                      | 1 |
| The Science of the Solar System                            | 1 |
| An Introduction to Operations Management                   | 1 |
| Greek and Roman Mythology                                  | 1 |
| Comic Books and Graphic Novels                             | 1 |
| Programming Languages                                      | 1 |
| Linear and Integer Programming                             | 1 |
| Algorithms: Design and Analysis, Part 1                    | 1 |
| The Modern World: Global History since 1760                | 1 |
| Know Thyself                                               | 1 |
| Calculus: Single Variable                                  | 1 |
| A Brief History of Humankind                               | 1 |
| Bioinformatics Algorithms (Part 1)                         | 1 |
| An Introduction to Financial Accounting                    | 1 |
| Archaeology's Dirty Little Secrets                         | 1 |
| The Bible's Prehistory, Purpose, and Political Future      | 1 |
+------------------------------------------------------------+---+
40 rows in set (0.00 sec)

