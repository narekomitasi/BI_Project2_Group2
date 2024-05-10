USE ORDERS_RELATIONAL_DB;

CREATE TABLE Categories (
    CategoryID INT,
    CategoryName VARCHAR(255),
    Description TEXT
);

CREATE TABLE Customers (
    CustomerID VARCHAR(10),
    CompanyName VARCHAR(255),
    ContactName VARCHAR(255),
    ContactTitle VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(255),
    Region VARCHAR(255),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    Phone VARCHAR(50),
    Fax VARCHAR(50)
);


CREATE TABLE Employees (
    EmployeeID INT,
    LastName VARCHAR(255),
    FirstName VARCHAR(255),
    Title VARCHAR(255),
	TitleOfCourtesy VARCHAR(255),
    BirthDate DATE,
    HireDate DATE,
    Address VARCHAR(255),
    City VARCHAR(255),
    Region VARCHAR(255),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    HomePhone VARCHAR(50),
    Extension VARCHAR(10),
    Notes TEXT,
    ReportsTo INT,
	PhotoPath TEXT
);

CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    UnitPrice DECIMAL(10, 2),
    Quantity INT,
    Discount REAL
);

CREATE TABLE Orders (
    OrderID INT,
    CustomerID VARCHAR(10),
    EmployeeID INT,
    OrderDate DATE,
    RequiredDate DATE,
    ShippedDate DATE,
    ShipVia INT,
    Freight DECIMAL(10, 2),
    ShipName VARCHAR(255),
    ShipAddress VARCHAR(255),
    ShipCity VARCHAR(255),
    ShipRegion VARCHAR(255),
    ShipPostalCode VARCHAR(255),
    ShipCountry VARCHAR(100),
	TerritoryID INT
);


CREATE TABLE Products (
    ProductID INT,
    ProductName VARCHAR(255),
    SupplierID INT,
    CategoryID INT,
    QuantityPerUnit VARCHAR(255),
    UnitPrice DECIMAL(10, 2),
    UnitsInStock INT,
    UnitsOnOrder INT,
    ReorderLevel INT,
    Discontinued BIT
);

CREATE TABLE Region (
    RegionID INT,
    RegionDescription VARCHAR(255)
);

CREATE TABLE Shippers (
    ShipperID INT,
    CompanyName VARCHAR(255),
    Phone VARCHAR(50)
);

CREATE TABLE Suppliers (
    SupplierID INT,
    CompanyName VARCHAR(255),
    ContactName VARCHAR(255),
    ContactTitle VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(255),
    Region VARCHAR(255),
    PostalCode VARCHAR(20),
    Country VARCHAR(100),
    Phone VARCHAR(50),
    Fax VARCHAR(50),
    HomePage TEXT
);

CREATE TABLE Territories (
    TerritoryID VARCHAR(20),
    TerritoryDescription VARCHAR(255),
    RegionID INT
);

