
resource "aws_db_instance" "weak_db" {
  identifier = "weak-db"
  engine = "mysql"
  instance_class = "db.t2.micro"
  username = "admin"
  password = "admin123"  # ❗ Hardcoded weak password
  publicly_accessible = true  # ❗
}
