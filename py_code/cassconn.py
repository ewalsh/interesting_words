from cassandra.cluster import Cluster

#if __name__ == "__main__":

# define cassandra connection function
def create_session(host, port, db = ''):
    cluster = Cluster([host],port=port)
    session = cluster.connect(db,wait_for_all_pools=True)
    return(session)


session = create_session('172.29.0.2', 9042, 'iwords')
