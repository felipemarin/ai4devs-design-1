from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Internet
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.storage import LocalStorage

with Diagram("Diagrama de Infraestructura LTI", show=True):
    usuario = User("Usuario")

    with Cluster("Frontend"):
        frontend = Server("React App")

    with Cluster("Backend"):
        backend = Server("Node.js API")
        cache = Redis("Redis Cache")

    with Cluster("Base de Datos"):
        db = PostgreSQL("PostgreSQL")

    with Cluster("Almacenamiento"):
        storage = LocalStorage("Archivos")

    internet = Internet("Internet")
    load_balancer = ELB("Load Balancer")

    usuario >> internet >> load_balancer >> frontend
    frontend >> backend
    backend >> db
    backend >> cache
    backend >> storage
