from database import Database
import datetime

def export_database():
    print("="*60)
    print("   EXPORTING DATABASE - SESSION 3")
    print("="*60)
    
    db = Database(
        host='localhost',
        user='root',
        password='databasepwd123',
        database='student_db'
    )
    
    if not db.connect():
        print("\n✗ Failed to connect to database!")
        return
    
    sql_content = []
    
    sql_content.append("-- ============================================================")
    sql_content.append("-- Student Registration System - Database Backup")
    sql_content.append(f"-- Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    sql_content.append("-- ============================================================\n")
    
    sql_content.append("-- Create database")
    sql_content.append("CREATE DATABASE IF NOT EXISTS student_db;")
    sql_content.append("USE student_db;\n")
    
    print("\n[Step 1] Exporting users table structure...")
    create_table = db.fetch_query("SHOW CREATE TABLE users")
    if create_table:
        sql_content.append("-- Table structure for users")
        sql_content.append("DROP TABLE IF EXISTS users;")
        sql_content.append(create_table[0]['Create Table'] + ";\n")
    
    print("[Step 2] Exporting users table data...")
    users = db.fetch_query("SELECT * FROM users")
    if users:
        sql_content.append("-- Data for table users")
        sql_content.append("INSERT INTO users (id, username, password) VALUES")
        
        values = []
        for user in users:
            values.append(f"({user['id']}, '{user['username']}', '{user['password']}')")
        
        sql_content.append(",\n".join(values) + ";\n")
    
    db.disconnect()
    
    print("[Step 3] Writing to student_db.sql...")
    content = "\n".join(sql_content)
    with open("student_db.sql", "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"\n✓ Database exported to: student_db.sql")
    print(f"✓ File size: {len(content)} bytes")
    
    print("\n" + "="*60)
    print("✓ Export completed successfully!")
    print("="*60)
    
    print("\nTo restore the database, run:")
    print("  mysql -u root -p < student_db.sql")

if __name__ == "__main__":
    export_database()

