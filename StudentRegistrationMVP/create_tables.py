from database import Database

def main():
    print("="*60)
    print("   CREATING DATABASE TABLES - SESSION 2")
    print("="*60)
    
    db = Database(
        host='localhost',
        user='root',
        password='databasepwd123',
        database='student_db'
    )
    
    if db.connect():
        print("\n[Creating Tables...]")
        db.create_tables()
        
        print("\n[Verifying Tables...]")
        tables = db.fetch_query("SHOW TABLES")
        
        if tables:
            print("\n✓ Tables in database:")
            for table in tables:
                print(f"   - {list(table.values())[0]}")
            
            print("\n[Users Table Structure:]")
            columns = db.fetch_query("DESCRIBE users")
            
            if columns:
                print(f"\n{'Field':<15} {'Type':<20} {'Null':<8} {'Key':<8} {'Extra':<15}")
                print("-" * 75)
                for col in columns:
                    print(f"{col['Field']:<15} {col['Type']:<20} {col['Null']:<8} {col['Key']:<8} {col['Extra']:<15}")
        
        db.disconnect()
        
        print("\n" + "="*60)
        print("✓ Database setup completed successfully!")
        print("="*60)
    else:
        print("\n✗ Failed to connect to database")

if __name__ == "__main__":
    main()


