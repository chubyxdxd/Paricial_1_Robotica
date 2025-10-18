import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fabricio/robotica/P_practico/yerko_pulgarcito/install/visual_pubsub'
