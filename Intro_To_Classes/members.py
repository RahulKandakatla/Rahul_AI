

class Member:

    member_serial_number = 0

    def __init__(self, email, fname=None, lname=None,  age=None, address=None, salary=None):
        self.id = None
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.phone_number = None

        self.age = age
        self.address = address
        self.salary = salary
        self.__ssn = None
    
    #private method
    def __retrieve_ssn(self):
        print(self.__ssn)

    def retrieve_member_details(self):
        member_serial_number = 20
        #Retrieve details from database using Email
        return "details"
    
    def get_connection(self):
        import configparser
        # Initialize the config parser
        config = configparser.ConfigParser()
        config.read('credentials.cfg')
        import os
        #from dotenv import load_dotenv
        import psycopg2
        connection = None
        # Database connection details
        # Default PostgreSQL port
        # Establishing the connection
        try:
            connection = psycopg2.connect(
                dbname=config['postgres']['DB_NAME'],
                user=config['postgres']['DB_USER'],
                password=config['postgres']['DB_PASSWORD'],
                host=config['postgres']['DB_HOST'],
                port=config['postgres']['DB_PORT'],
                sslmode="require"
            )
            print("Database connection successful!")
            
        except Exception as e:
            print("Error connecting to the database:", e)
        return connection
        #save member to database

    def create_new_member(self):
        
        connection = self.get_connection()
        if(connection is not None):
            cursor = connection.cursor()
            cursor.execute(f"""
            INSERT INTO fi_members (first_name, last_name, email)
            VALUES (%s, %s, %s) RETURNING member_id ;
            """, (self.first_name,self.last_name, self.email))
            connection.commit()
            id = cursor.fetchone()[0]
            print(f"Record inserted successfully!: {id}")
        #raise exception if email already exists
        else:
            raise Exception ("connection could not be established")
        return "id of inserted row"
    

new_member = Member(email="rahul1234567890@gmail.com", fname="testclass", lname="testclass")

new_member.create_new_member()

"""print(new_member.member_serial_number)
print(Member.member_serial_number)

print(new_member.first_name)
#print(Member.first_name) #error

print(Member.retrieve_serial_number_class())
#print(new_member.retrieve_serial_number_class())

print(Member.retrieve_serial_number_static())
#print(new_member.Member.retrieve_serial_number_static())

#print(new_member.__ssn)"""