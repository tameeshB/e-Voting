import pymysql

# Pre-Docker deploy debug:
# https://stackoverflow.com/a/59591269/2736932
pymysql.version_info = (1, 3, 13, "final", 0)

pymysql.install_as_MySQLdb()