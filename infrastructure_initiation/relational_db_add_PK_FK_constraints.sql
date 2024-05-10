USE ORDERS_RELATIONAL_DB;

ALTER TABLE dbo.Categories ADD CONSTRAINT PK_Categories PRIMARY KEY (CategoryID);
ALTER TABLE dbo.Customers ADD CONSTRAINT PK_Customers PRIMARY KEY (CustomerID);
ALTER TABLE dbo.Employees ADD CONSTRAINT PK_Employees PRIMARY KEY (EmployeeID);
ALTER TABLE dbo.[Order Details] ADD CONSTRAINT PK_OrderDetails PRIMARY KEY (OrderID, ProductID);
ALTER TABLE dbo.Orders ADD CONSTRAINT PK_Orders PRIMARY KEY (OrderID);
ALTER TABLE dbo.Products ADD CONSTRAINT PK_Products PRIMARY KEY (ProductID);
ALTER TABLE dbo.Region ADD CONSTRAINT PK_Region PRIMARY KEY (RegionID);
ALTER TABLE dbo.Shippers ADD CONSTRAINT PK_Shippers PRIMARY KEY (ShipperID);
ALTER TABLE dbo.Suppliers ADD CONSTRAINT PK_Suppliers PRIMARY KEY (SupplierID);
ALTER TABLE dbo.Territories ADD CONSTRAINT PK_Territories PRIMARY KEY (TerritoryID);

ALTER TABLE dbo.Employees ADD CONSTRAINT FK_Employees_ReportsTo FOREIGN KEY (ReportsTo) REFERENCES dbo.Employees (EmployeeID);
ALTER TABLE dbo.[Order Details] ADD CONSTRAINT FK_OrderDetails_OrderID FOREIGN KEY (OrderID) REFERENCES dbo.Orders (OrderID);
ALTER TABLE dbo.[Order Details] ADD CONSTRAINT FK_OrderDetails_ProductID FOREIGN KEY (ProductID) REFERENCES dbo.Products (ProductID);
ALTER TABLE dbo.Orders ADD CONSTRAINT FK_Orders_CustomerID FOREIGN KEY (CustomerID) REFERENCES dbo.Customers (CustomerID);
ALTER TABLE dbo.Orders ADD CONSTRAINT FK_Orders_EmployeeID FOREIGN KEY (EmployeeID) REFERENCES dbo.Employees (EmployeeID);
ALTER TABLE dbo.Orders ADD CONSTRAINT FK_Orders_ShipVia FOREIGN KEY (ShipVia) REFERENCES dbo.Shippers (ShipperID);
ALTER TABLE dbo.Orders ADD CONSTRAINT FK_Orders_TerritoryID FOREIGN KEY (TerritoryID) REFERENCES dbo.Territories (TerritoryID);
ALTER TABLE dbo.Products ADD CONSTRAINT FK_Products_CategoryID FOREIGN KEY (CategoryID) REFERENCES dbo.Categories (CategoryID);
ALTER TABLE dbo.Products ADD CONSTRAINT FK_Products_SupplierID FOREIGN KEY (SupplierID) REFERENCES dbo.Suppliers (SupplierID);
ALTER TABLE dbo.Territories ADD CONSTRAINT FK_Territories_RegionID FOREIGN KEY (RegionID) REFERENCES dbo.Region (RegionID);
