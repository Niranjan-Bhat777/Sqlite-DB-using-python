import sqlite3

# connect to database

conn = sqlite3.connect('ctmovie.db')

#create a cursor

na = conn.cursor()

#create a table

na.execute("""CREATE TABLE ctmovie (
            name text,
            lead_actor text,
            lead_actress text,
            year_of_release integer,
            director text
            ) """)

#Adding records into the table

an =[
    ('Moggina Manasu         ','Yash        ','Radika Pandit     ',2008,'Shashank'),
    ('Rocky                  ','Yash        ','Bianca Desai      ',2008,'S.K. Nagendra'),
    ('Kallara Santhe         ','Yash        ','Haripriya         ',2009,'Sumana Kittur'),
    ('Modalasala             ','Yash        ','Bhama             ',2010,'Purushotham C. Somanathapura'),
    ('Rajadhani              ','Yash        ','Sheena Shahabadi  ',2011,'Sowmya Sathyan N.R'),
    ('Kirataka               ','Yash        ','Oviya             ',2011,'Pradeep Raj'),
    ('Lucky                  ','Yash        ','Ramya             ',2012,'Dr. Suri'),
    ('Jaanu                  ','Yash        ','Deepa Sannidhi    ',2012,'Preetham Gubbi'),
    ('Drama                  ','Yash        ','Radika Pandit     ',2012,'Yograj Bhat'),
    ('Googly                 ','Yash        ','Krithi Kharbanda  ',2013,'Pavan Wadeyar'),
    ('Raja Huli              ','Yash        ','Meghana Raj       ',2013,'Guru Deshpande'),
    ('Gajakesari             ','Yash        ','Amulya            ',2014,'Krishna'),
    ('Mr and Mrs Ramachari   ','Yash        ','Radika Pandit     ',2014,'Santhosh Anandram'),
    ('Masterpiece            ','Yash        ','Shanvi Srivatsava ',2015,'Manju Mandavya'),
    ('Santhu Straight Forward','Yash        ','Radika Pandit     ',2016,'Mahesh Rao'),
    ('K.G.F Chapter 1        ','Yash        ','Srinidhi Shetty   ',2018,'Prashanth Neel'),
    ('K.G.F Chapter 2        ','Yash        ','Srinidhi Shetty   ',2022,'Prashanth Neel')
    ]

na.executemany("INSERT INTO ctmovie VALUES (?,?,?,?,?)",an)

#commit our commnd

conn.commit()

#close our connection

conn.close()
