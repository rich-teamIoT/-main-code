USE journallpnu;
INSERT INTO users VALUES (1, 'testinglogin', 'testingname', 'testingemail', 'testingpassword'), (2, 'testl', 'testn', 'teste', 'testp'), (3, 'one', 'two', 'three', 'four'),
(4, 'login', 'name', 'email', 'password'), (5, 'logintest', 'nametest', 'emailtest', 'passwordtest'), (6, 'olapol', 'Olha_Polishchuk', 'olapol6@gmail.com', '12345'), (7, 'yanad', 'Yana_Didun', 'yanad@gmail.com', '12345678'), (8, 'valyaroz', 'Valentyna_Rozumovych', 'valyaroz@gmail.com', '87654321'), (9, 'nazark', 'Nazar_Kulyk', 'nazark@gmail.com', '11111111');
INSERT INTO group_information VALUES (1, '1', '1', 'KN-124', 'IKTA', 'Zenoviy_Veres'), (2, '1', '1', 'KN-125', 'IKTA', 'Zenoviy_Veres');
INSERT INTO student VALUES ('6', '1', 'Olha', 'Polishchuk'), ('7', '1', 'Yana', 'Didun'), ('8', '1', 'Valentina', 'Rozumovych'), ('9', '1', 'Nazar', 'Kulyk');
INSERT INTO discipline VALUES (1, 'Math_analysis', 'Higher mathematics', 'lecture', 'Rybytska_O.M.'), (2, 'Programming', 'EOM', 'lab', 'Dzelendzyak_U.U'), (3, 'Physics', 'Physics', 'practice', 'Kusnezh_V.V.');
INSERT INTO attendance VALUES ('6', '1', '2', '+', '2016-12-12'), ('7', '1', '1', '-', '2016-10-12'), ('6', '1', '3', '-', '2016-09-10');
INSERT INTO progress VALUES ('6', '1', '3', '4', '2016-11-09'), ('7', '1', '2', '5', '2016-12-10'), ('7', '1', '2', '5', '2016-09-09'); 