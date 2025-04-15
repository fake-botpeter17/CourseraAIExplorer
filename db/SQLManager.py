from sqlite3 import Connection, Cursor, connect
from typing import Any, Self

class TableNotFound(Exception):
    """Raised when the specified table is not present in the selected Database."""
    def __init__(self, message :str) -> None:
        super().__init__(message)

class  TableInitializationError(Exception):
    """Raised when the table initialization parameters are invalid."""
    def __init__(self, message :str) -> None:
        super().__init__(message)

class SQLite:
    def __init__(self :Self, db_file : str) -> None:
        """Establishes connection to the specified database and returns the Cursor object."""
        self.__db_file: str = db_file
        self.__con: Connection = connect(database = self.__db_file)
        self.__cursor: Cursor = self.__con.cursor()
        self.__current_table: str | None = None

    def __enter__(self :Self) -> Cursor:
        return self.__cursor

    def __exit__(self, exp_type, exp, traceback) -> None:
        if self.__con: self.__con.close()

    def createTable(self, tName :str, tCols :tuple[str, ...], tConstraints :list[tuple[str, ...]]) -> bool:
        """Creates a table for the specified parameters."""
        if len(tCols) != len(tConstraints):
            raise TableInitializationError("Column to Constraint relation must be one-to-one!")
        base_str: str = f"create table {tName}("
        for i,column in enumerate(tCols):
            base_str += str(column)
            for constraint in tConstraints[i]:
                base_str += str(" " + constraint)
            if i < len(tCols) - 1:
                base_str += ", "
        base_str += ")"

        self.__cursor.execute(base_str)
        self.__con.commit()
        return True
        
    def insertValue(self, *args) -> None:
        if not self.__current_table:
            raise TableInitializationError("No table selected! Use selectTable() to select.")
        query = f"insert into {self.__current_table} values ({"?, " * (len(args) - 1)}?);"
        self.__cursor.execute(query, args)

    def selectTable(self, tName :str) -> None:
        if tName in self.getTables():
            self.__current_table = tName
            return
        raise TableNotFound(f"Table {tName} doesn't exist.")

    def getCurrentTable(self) -> str | None:
        return self.__current_table

    def commit(self) -> None:
        """Commit the current transaction."""
        self.__con.commit()

    def getTables(self) -> list:
        self.__cursor.execute("select name from sqlite_master where type='table';")
        tables: list[str] | None = self.__cursor.fetchall()
        return [x[0] for x in tables if tables]

    def close(self) -> None:
        """Closes the connection to the database if still connected."""
        if self.__con:
            self.__con.commit()
            self.__con.close()

    def viewTable(self, project :list[str] | None = None, constraints :list[str] | None = None):
        if not self.__current_table:
            raise TableInitializationError("No table selected! Use selectTable() to select.")
        q = "select "
        if project:
            q += ", ".join(project) + " "
        else:
            q += "* "
        q += f"from {self.__current_table}"
        if constraints:
            q += " where " + " and ".join(constraints)
        self.__cursor.execute(q)
        return self.__cursor.fetchall()
    
def initCourseDB() -> SQLite:
    """
    Initializes the Course database with the specified file name.
    """
    db = SQLite("courses.db")
    db.createTable(
        tName="Courses", 
        tCols=("id", "name", "type", "sub_courses", "desc", "certVal"),
        tConstraints=[("integer", "primary key"), ("text",), ("text",), ("text",), ("text",), ("text",)]
        )