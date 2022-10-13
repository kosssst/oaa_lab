import rows as row

class table:
    name = ""
    columns = []
    column_params = []
    rows = []
    
    def __init__(self, table_name: str, table_columns: list, table_params: list) -> None:
        self.name = table_name
        self.columns = table_columns
        self.column_params = table_params
        
    def add_row(self, data: list) -> None:
        self.rows.append(row.row(data))