--  lists all cities contained in the database hbtn_0d_usa

SELECT hbtn_0d_usa.cities.id, hbtn_0d_usa.cities.name, hbtn_0d_usa.states.name ORDER BY hbtn_0d_usa.cities.id DESC;