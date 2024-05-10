import config
import tasks
import logging1

class RelationalDataFlow:
    def __init__(self):
        self.conn_relational = tasks.connect_db_create_cursor("Database1")
        logging1.log_message('info', 'Database connection initialized')

    def close_connection(self):
        self.conn_relational.close()
        logging1.log_message('info', 'Database connection closed')

    def exec(self):
        logging1.log_message('info', 'Starting execution of relational data flow')
        
        logging1.log_message('info', 'Inserting into Categories')
        tasks.insert_into_Categories(self.conn_relational, 'Categories', 'ORDERS_RELATIONAL_DB', 'dbo', config.data_dir)
        
        logging1.log_message('info', 'Inserting into Customers')
        tasks.insert_into_Customers(self.conn_relational, 'Customers', 'ORDERS_RELATIONAL_DB', 'dbo', config.data_dir)
        
        logging1.log_message('info', 'Inserting into Employees')
        tasks.insert_into_Employees(self.conn_relational, 'Employees', 'ORDERS_RELATIONAL_DB', 'dbo', config.data_dir)
        
        logging1.log_message('info', 'Inserting into Suppliers')
        tasks.insert_into_Suppliers(self.conn_relational, 'Suppliers', 'ORDERS_RELATIONAL_DB', 'dbo', config.data_dir)
        
        logging1.log_message('info', 'Inserting into Shippers')
        tasks.insert_into_Shippers(self.conn_relational, 'Shippers', 'ORDERS_RELATIONAL_DB', 'dbo', config.data_dir)
        
        logging1.log_message('info', 'Inserting into Region')
        tasks.insert_into_Region(self.conn_relational, 'Region', 'ORDERS_RELATIONAL_DB', 'dbo', config.data_dir)
        
        logging1.log_message('info', 'Inserting into Products')
        tasks.insert_into_Products(self.conn_relational, 'Products', 'ORDERS_RELATIONAL_DB', 'dbo', config.data_dir)
        
        logging1.log_message('info', 'Inserting into Orders')
        tasks.insert_into_Orders(self.conn_relational, 'Orders', 'ORDERS_RELATIONAL_DB', 'dbo', config.data_dir)
        
        logging1.log_message('info', 'Inserting into OrderDetails')
        tasks.insert_into_OrderDetails(self.conn_relational, 'OrderDetails', 'ORDERS_RELATIONAL_DB', 'dbo', config.data_dir)
        
        logging1.log_message('info', 'Completed execution of relational data flow')

inst = RelationalDataFlow()
inst.exec()
inst.close_connection()