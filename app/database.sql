DELIMITER $$
	CREATE PROCEDURE getReport(in amount int)
	BEGIN
	/* CODE GOES HERE */
    SELECT customer.fname as 'First Name', customer.lname as 'Last Name', SUM(icost) as 'Total Cost of Purchases'
    FROM CUSTOMER 
    JOIN BUY
    JOIN ITEM
    ON CUSTOMER.CID = BUY.CID
    AND BUY.IID = ITEM.IID
    WHERE SUM(icost) > amount;
	END $$
DELIMITER ;

DELIMITER $$
USE CompuStore $$
	CREATE DEFINER=`root` @`localhost`
    PROCEDURE `search`(IN itemName varchar(30))
	BEGIN
    SELECT item.iname
    FROM item
    WHERE item.iname LIKE '%itemName%';
    END $$
DELIMITER ;

/*Number of sales per branch*/
DELIMITER $$
USE CompuStore $$
    CREATE DEFINER=`root` @`localhost`
    PROCEDURE num_of_sales()
    BEGIN
    SELECT item.iname, buy.quantity
    FROM buy
    join item on buy.iid = item.iid;
    END $$
DELIMITER ;

DELIMITER $$
USE CompuStore1 $$
    CREATE DEFINER=`root` @`localhost`
    PROCEDURE num_of_sales()
    BEGIN
    SELECT item.iname, buy.quantity
    FROM buy
    join item on buy.iid = item.iid;
    END $$
DELIMITER ;

DELIMITER $$
USE CompuStore2 $$
    CREATE DEFINER=`root` @`localhost`
    PROCEDURE num_of_sales()
    BEGIN
    SELECT item.iname, buy.quantity
    FROM buy
    join item on buy.iid = item.iid;
    END $$
DELIMITER ;
/*Top Sales Codes*/
DELIMITER $$
USE CompuStore $$
    CREATE DEFINER=`root` @`localhost`
    PROCEDURE top_sales()
    BEGIN
    SELECT iname, icost as "Unit Price", SUM(icost) as "Total Cost of Amount Sold"
    FROM buy
    join item on item.iid = buy.iid
    GROUP BY iname,icost
    ORDER BY SUM(icost) DESC;
    END $$
DELIMITER ;

DELIMITER $$
USE CompuStore1 $$
    CREATE DEFINER=`root` @`localhost`
    PROCEDURE top_sales()
    BEGIN
    SELECT iname, icost as "Unit Price", SUM(icost) as "Total Cost of Amount Sold"
    FROM buy
    join item on item.iid = buy.iid
    GROUP BY iname,icost
    ORDER BY SUM(icost) DESC;
    END $$
DELIMITER ;

DELIMITER $$
USE CompuStore2 $$
    CREATE DEFINER=`root` @`localhost`
    PROCEDURE top_sales()
    BEGIN
    SELECT iname, icost as "Unit Price", SUM(icost) as "Total Cost of Amount Sold"
    FROM buy
    join item on item.iid = buy.iid
    GROUP BY iname,icost
    ORDER BY SUM(icost) DESC;
    END $$
DELIMITER ;


