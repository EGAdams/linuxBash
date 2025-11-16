# Who you are
You are an expert Python Developer and seasoned user of the Gang of Four Design Pattern Principals.

# Relevant Source Code
## main.py
```python
class Application:
    def __init__( self ):
        self.browser_manager    = WebBrowserManager()
        self.duplicate_manager  = DuplicateManager( "links.txt" )
        self.link_analyzer      = LinkAnalyzer( self.browser_manager, self.duplicate_manager )

    def run( self ):
        try:                                                # go to the 1st page.
            self.browser_manager.navigate_to_page( "https://search.sunbiz.org/Inquiry/CorporationSearch/SearchResults?inquiryType=ZipCode&searchTerm=34609" )
            while True:
                try:
                    self.link_analyzer.analyze_initial_entity_row_links()
                except NoSuchElementException:
                    print( "No more pages to navigate or links to process." )
                    break

                self.link_analyzer.link_navigator.navigate_to_next() # navigate to next page

        except Exception as e:
            print( f"An unexpected error occurred: {str(e)}" )
        finally:
            self.browser_manager.quit()
            print( "Browser closed." )

if __name__ == "__main__":
    application_instance = Application()
    application_instance.run()

```
## web_browser_manager class
```python
class WebBrowserManager:
    def __init__(self):
        self.driver = self.initialize_driver()
    
    def initialize_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        return webdriver.Chrome(options=chrome_options)
    
    def navigate_to_page(self, url):
        self.driver.get(url)
    
    def find_elements(self, css_selector):
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector)
    
    def get_html_content(self, href):
        try:
            self.navigate_to_page(href)
            return self.driver.page_source  # Return the HTML content of the page
        except Exception as e:
            print(f"Failed to get content from {href}: {str(e)}")
            return None
    
    def click_next(self, css_selector):
        next_button = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        next_button.click()
    
    def quit(self):
        self.driver.quit()


```
## duplicate_manager class
```python
class DuplicateManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.duplicate_count = 0
        # overwrite the contents of the file if it exists
        # with open(self.filepath, 'w') as file:
        #     file.write('')   # wipe out the contents here
        self.load_existing_ids()
    
    def load_existing_ids(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                self.existing_ids = file.read().splitlines()
        else:
            self.existing_ids = []
    
    def check_duplicate(self, identifier):
        if identifier in self.existing_ids:
            self.duplicate_count += 1
            return True
        self.existing_ids.append( identifier )
        return False
    
    def add_to_file(self, identifier):
        with open(self.filepath, 'a') as file:
            file.write(identifier + '\n')
        self.existing_ids.append(identifier)

```
## data_extractor class
```python
class DataExtractor:
    def __init__( self ):
        print( "initialized data extractor... " )

    def pull_initial_entity_row( self, initial_entity_row ):
        href = initial_entity_row.get_attribute( "href" )
        title = initial_entity_row.text
        print("extracting data for title: " + title )

        # Navigate up to the parent row of the link
        parent_row = initial_entity_row.find_element(By.XPATH, "./ancestor::tr")

        # Extract text from each cell directly within the parent row
        cells = parent_row.find_elements(By.TAG_NAME, "td")

        # Ensure the correct number of cells are present before extracting data
        if len(cells) >= 4:
            document_id = cells[1].text.strip()  # Adjusted to correct index for document ID
            entity_status = cells[2].text.strip()  # Correct index for entity status
            zip_code = cells[3].text.strip()  # Correct index for zip code
        else:
            document_id = ""
            entity_status = ""
            zip_code = ""
            print("Error: Insufficient data in row.")

        return {
            "detail_page_link": href,
            "title": title,
            "document_id": document_id,
            "entity_status": entity_status,
            "zip_code": zip_code
        }

```
## link_analyzer class
```python
class LinkAnalyzer:
    def __init__(self, browser_manager, duplicate_manager):
        self.browser_manager        = browser_manager
        self.data_extractor         = DataExtractor( browser_manager )
        self.data_processor         = DataProcessor( duplicate_manager )
        self.link_navigator         = LinkNavigator( browser_manager )
        self.database_connection    = DatabaseConnection()
        self.new_data_processor     = NewDataProcessor( self.database_connection )

    def analyze_initial_entity_row_links( self ): # get all tr
        links = self.browser_manager.find_elements( "tr td.large-width a" )
        for link in links: # iterate tr
            data = self.data_extractor.pull_initial_entity_row( link ) # extract data 
            self.data_processor.process_data( data ) # remember it
            if ( not( self.database_connection.is_in_database( data[ "document_id" ]))):
                self.new_data_processor.process_new_data( data ) # not in db? insert...
```
## data_processor class
```python
class DataProcessor:
    def __init__( self, duplicate_manager ):
        self.duplicate_manager = duplicate_manager

    def process_data( self, data ):
        print( "processing data for document: ", data[ 'document_id' ])
        if not self.duplicate_manager.check_duplicate( data[ 'document_id' ]): # if it is not a duplicate,
            self.duplicate_manager.add_to_file( data[ 'document_id' ])         # add it to the file
            print(f"Added {data[ 'document_id' ]} to the file.")
            # print(json.dumps( data, indent=4 ))  # Print to verify
        else:
            print ( "must be a duplicate" )
```
## link_navigator class
```python
class LinkNavigator:
    def __init__(self, browser_manager):
        self.browser_manager = browser_manager

    def navigate_to_next(self):
        print( "navigating to next link... " )
        try:
            self.browser_manager.click_next(".navigationBarPaging a[title='Next List']")
        except NoSuchElementException:
            print("No more lists to process.")

```
## database_connection class
```python
class DatabaseConnection:
    def __init__(self):
        self.host = "awmassets.com"
        self.port = 3306
        self.username = input( "username: " ) # os.environ.get( "AWMASSETS_USERNAME" )
        self.password = input( "password: " ) # os.environ.get( "LADAMS_PASSWORD"    )
        self.database = "awmasset_sbcrawler"
        self.connection = None
        print ( "username set to: " + self.username )
        print ( "password set to: " + self.password )

    def connect(self):
        if self.connection is None:
            try:
                self.connection = pymysql.connect(
                    host=self.host,
                    port=self.port,
                    user=self.username,
                    password=self.password,
                    db=self.database,
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
            except pymysql.MySQLError as e:
                print(f"Error connecting to MySQL Platform: {e}")
                raise e
            
    def getDirtyRecords(self):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM hernando_data WHERE report_status = 'new'"
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows
              
    def select_by_document_number(self, document_number):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM hernando_data WHERE document_number = %s"
            cursor.execute(sql, (document_number,))
            row = cursor.fetchone()
            self.close
            return row

    def is_in_database(self, document_number):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM hernando_data WHERE document_number = %s"
            cursor.execute(sql, (document_number,))
            row = cursor.fetchone()
            self.close()
            return row is not None


    def insert(self, data):
        self.connect()
        with self.connection.cursor() as cursor:
            # Prepare SQL query to INSERT a record into the database.
            sql = """
            INSERT INTO hernando_data (title, detail_page_link, time, document_number, status, zip_code, report_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            try:
                # Execute the SQL command
                cursor.execute(sql, (
                    data['title'],
                    data['detail_page_link'],
                    str(int(time.time())),
                    data['document_id'],
                    data['entity_status'],
                    data['zip_code'],
                    data['report_status']
                ))
                # Commit your changes in the database
                self.connection.commit()
            except pymysql.MySQLError as e:
                print(f"Failed to insert data: {e}")
                self.connection.rollback()
                raise e

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

# Usage
if __name__ == "__main__":
    db = DatabaseConnection()
    data = {
        "detail_page_link": "https://search.sunbiz.org/Inquiry/CorporationSearch/SearchResultDetail?inquirytype=ZipCode&directionType=Initial&searchNameOrder=1433DELEONSTREET%20L140000694490&aggregateId=flal-l14000069449-0604e20f-8f3e-4b56-b67d-c79c10b97193&searchTerm=34609&listNameOrder=100PROOFARTWORKS%20P110000275730",
        "title": "1433 DE LEON STREET LLC",
        "document_id": "L14000069449",
        "entity_status": "INACT",
        "zip_code": "34609",
        "report_status": "new"
    }
    try:
        db.insert(data)
        print("Data inserted successfully.")
    finally:
        db.close()

```
## new_data_processor class
```python
class NewDataProcessor:
    def __init__( self, database_connection_arg ):
        self.database_connection = database_connection_arg
        
    def process_new_data( self, data ):
        print( "processing data..." )
        data[ "report_status" ] = "new"
        # dump the data before the db insert...
        print( json.dumps( data, indent=4 ))
        self.database_connection.insert( data )
        
```
# Your Task
Please let me know how we could use the Strategy Pattern for the data processing.


# Your Task
Please let me know what you think of the design of this system.  Could it use more or different design patterns?  Does each class have only one responsibility?  What objects would you add if any to simplify the system more?